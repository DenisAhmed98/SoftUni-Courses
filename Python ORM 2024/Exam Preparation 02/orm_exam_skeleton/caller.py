import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order
# Create queries within functions


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = Profile.objects.filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    result = []

    if query is not None:
        result = "\n".join(
            f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.profile_orders.count()}"
            for p in query
        )
        return result

    return ""


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()

    if loyal_profiles is not None:
        return "\n".join(
            f"Profile: {p.full_name}, orders: {p.order_count}"
            for p in loyal_profiles
        )

    return ""


def get_last_sold_products():
    last_products = Order.objects.prefetch_related('products').last()

    if last_products is None or not last_products.products.exists():
        return ""

    products_r = ", ".join(last_products.products.order_by('name').values_list('name', flat=True))
    return f"Last sold products: {products_r}"


def get_top_products():
    top_products = Product.objects.annotate(products_count=Count('products_orders')).filter(
        products_count__gt=0).order_by('-products_count', 'name')[:5]

    if not top_products.exists():
        return ""

    product_lines = "\n".join(f"{p.name}, sold {p.products_count} times" for p in top_products)
    return f"Top products:\n" + product_lines


def apply_discounts():
    updated_orders_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False
    ).update(
        total_price=F('total_price') * 0.90
    )

    return f"Discount applied to {updated_orders_count} orders."


def complete_order() -> str:
    order = Order.objects.filter(
        is_completed=False
    ).order_by(
        'creation_date'
    ).first()

    if not order:
        return ""

    for product in order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    order.is_completed = True
    order.save()

    return "Order has been completed!"



