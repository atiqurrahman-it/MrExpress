from django.shortcuts import render
from product_store.models import Product

# Create your views here.

def home_page(request):
    all_product=Product.objects.all().filter(status=True)
    data={
        "all_product":all_product,
    }
    return render(request,'pages/index.html',data)
