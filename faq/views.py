from django.shortcuts import render, redirect, reverse, get_object_or_404

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
