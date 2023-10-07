from django.shortcuts import render
from .models import Product  # Import the Product model

def index_view(request):
    # Fetch a list of products from the database
    products = Product.objects.all()

    # Pass the products to the template for rendering
    context = {'products': products}
    return render(request, 'index.html', context)