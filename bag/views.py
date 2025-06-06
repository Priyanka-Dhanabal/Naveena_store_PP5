from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to '
                    f'{bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """
    product = get_object_or_404(Product, pk=item_id)

    try:
        quantity = int(request.POST.get('quantity', 0))
    except (ValueError, TypeError):
        messages.error(request, "Invalid quantity.")
        return redirect(reverse('view_bag'))

    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to '
                f'{bag[item_id]["items_by_size"][size]}')
        else:
            if (item_id in bag and
                'items_by_size' in bag[item_id] and
                    size in bag[item_id]['items_by_size']):
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
                messages.success(
                    request,
                    f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            if item_id in bag:
                bag.pop(item_id)
                messages.success(
                    request,
                    f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item or specific size from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        bag = request.session.get('bag', {})

        if size:
            # Product with size
            if (
                item_id in bag and
                isinstance(bag[item_id], dict) and
                'items_by_size' in bag[item_id] and
                size in bag[item_id]['items_by_size']
            ):
                del bag[item_id]['items_by_size'][size]

                if not bag[item_id]['items_by_size']:
                    del bag[item_id]

                messages.success(
                    request,
                    f'Removed {product.name} (Size {size.upper()}) from your bag.'
                )
            else:
                messages.error(
                    request,
                    f'{product.name} (Size {size.upper()}) not found in your bag.'
                )
        else:
            # Product without size
            if item_id in bag:
                del bag[item_id]
                messages.success(
                    request,
                    f'Removed {product.name} from your bag.'
                )
            else:
                messages.error(
                    request,
                    f'{product.name} not found in your bag.'
                )

        request.session['bag'] = bag
        return redirect('view_bag')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
