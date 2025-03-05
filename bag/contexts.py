from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        # If item_data is an integer, it means no size is associated, so it's just quantity
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'size': None  # No size for this product
            })
        else:
            # If item_data contains sizes, we need to handle sizes
            product = get_object_or_404(Product, pk=item_id)
            # Safely get 'items_by_size', default to an empty dictionary if not found
            items_by_size = item_data.get('items_by_size', {})

            for size, quantity in items_by_size.items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,  # The quantity for each size
                    'product': product,
                    'size': size,  # Size of the product
                })

    # Handle delivery cost
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    # Add all the necessary context variables
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
