from django.shortcuts import render
from products.models import Product
from .funciones import funcionCarrito
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import CartProduct
from AppHieloSeco.forms import Registro
from users.models import User
from.models import Cart
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cart(request):
    cart = funcionCarrito(request)
    return render(request,'carts/cart.html',{
        'cart' : cart
    })

def add(request):
    '''Funcion para añadir productos al carrito'''
    cart = funcionCarrito(request)
    product = get_object_or_404(Product,pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity',1))

    #cart.product.add(product, through_defaults={
        #'quantity': quantity
    #})

    product_cart=CartProduct.objects.crearActualizar(cart=cart,product=product,quantity=quantity) #le decimos al objeto de cartproduct que cree un carrito, un producto y la cantidad

    return render(request, 'carts/add.html',{
        'product':product,
    })

def remove(request):
    '''Funcion remover producto del carrito'''
    cart = funcionCarrito(request)
    product = get_object_or_404(Product,pk=request.POST.get('product_id'))

    cart.product.remove(product)

    return redirect('cart')





