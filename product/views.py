from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from cart.forms import CartAddProductForm
from .filters import ProductFilter

def landing_page(request):
    products=Product.objects.all().order_by('-created')[:5]
    categories=Category.objects.all()[:4]
    cart_product_form=CartAddProductForm()
    context={'products':products,'categories':categories,'form':cart_product_form}
    return render(request, 'product/landing.html',context)

def product_list(request, category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.all()
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        products=products.filter(category=category)
    products_filtered=ProductFilter(request.GET, queryset=products).qs
    context={'categories':categories, 'products':products,'category':category,'products_filtered':products_filtered}
    return render(request, 'product/product_list.html', context)


def product_detail(request,id, slug):
    product=get_object_or_404(Product, available=True, id=id, slug=slug)
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:3]
    cart_product_form=CartAddProductForm()
    context={'product':product, 'related_products':related_products,'form':cart_product_form}
    return render(request, 'product/product_detail.html', context)