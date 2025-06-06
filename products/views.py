from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Review
from django.db.models.functions import Lower
from .forms import ProductForm, ReviewForm


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    user_has_reviewed = Review.objects.filter(
        product=product, user=request.user).exists(
        ) if request.user.is_authenticated else False
    context = {
        'product': product,
        'reviews': reviews,
        'user_has_reviewed': user_has_reviewed,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """Add a new review for a product."""
    product = get_object_or_404(Product, pk=product_id)
    # Check if the user has already reviewed this product
    existing_review = Review.objects.filter(
        product=product, user=request.user
    ).first()
    # If a review exists, prevent a second review
    if existing_review:
        messages.error(request, "You have already reviewed this product.")
        return redirect("product_detail", product_id=product.id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                # Create the review object but do not save it yet
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                # After saving, show a success message
                messages.success(request, "Thank you for your review!")
                return redirect("product_detail", product_id=product.id)
            except IntegrityError:
                # If there's an integrity error, show an error message
                messages.error(
                    request,
                    "An error occurred while saving your review."
                    "Please try again.")
                return redirect("product_detail", product_id=product.id)
        else:
            messages.error(
                request,
                "There was an issue with your form submission."
                "Please correct the errors below.")
    else:
        form = ReviewForm()
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/add_review.html", context)


@login_required
def edit_review(request, product_id, review_id):
    """
    Edit an existing review for a specific product by the logged-in user.
    """
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(
        Review, pk=review_id, product=product, user=request.user
    )
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your review has been updated successfully!"
            )
            return redirect("product_detail", product_id=product.id)
    else:
        form = ReviewForm(instance=review)

    context = {
        "form": form,
        "product": product,
        "review": review,
    }
    return render(request, "products/edit_review.html", context)


@login_required
def delete_review(request, product_id, review_id):
    """Delete a specific review."""
    review = get_object_or_404(Review, pk=review_id, product_id=product_id)
    if review.user != request.user:
        # Ensure only the owner can delete their review
        messages.error(
            request,
            "You are not authorized to delete this review.")
        return redirect('product_detail', product_id=product_id)
    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect("product_detail", product_id=product_id)
    return render(
        request,
        "products/confirm_delete_review.html",
        {"review": review, "product": review.product}
     )
