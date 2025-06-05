from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Faq
from .forms import FaqForm

# Create your views here.


def faq(request):
    """
    A view to render the FAQ page
    """

    faq_items = Faq.objects.all()
    context = {
        'faq_items': faq_items,
    }
    template = 'faq/faq.html'

    return render(request, template, context)


@login_required
def add_faq(request):
    """
    Add a question/answer to the faq page
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Successfully added Question!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request,
                'Failed to add Question. Please ensure the form is valid.',
            )
    else:
        form = FaqForm()

    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """
    Edit a question/answer from the FAQ page
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the FAQ page!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request,
                'Failed to update FAQ page. Please ensure the form is valid.',
            )
    else:
        form = FaqForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """
    Delete a question/answer from the FAQ page
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'Question deleted!')
    return redirect(reverse('faq'))
