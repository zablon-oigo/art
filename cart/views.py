from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # Modify the form instantiation to include the initial data for add_to_cart
    form_data = {'add_to_cart': True}
    form = CartAddProductForm(request.POST or None, initial=form_data)

    if form.is_valid():
        cd = form.cleaned_data
        # You can handle the quantity logic here based on your use case
        # For example, you might always add one item per click
        cart.add(item=product, quantity=1, override_quantity=cd['override'])

    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart=Cart(request)
    product=get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart=Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity':item['quantity'],
            'override':True

        })
    return render(request, 'cart/detail.html',{'cart':cart})

def product_list(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request, "cart/list.html", context)