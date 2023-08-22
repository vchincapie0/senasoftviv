from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth import logout
from .forms import Registro
from django.contrib.auth.models import User
from products.models import Product
from django.http import HttpResponseRedirect


def tienda(request):
    '''Funcion de la pagina principal de la tienda'''
    productos = Product.objects.all() #La variable incluye todos los productos almancenados en la bd
    return render(request, 'tienda.html',{
        'mensaje':'Paper ICE',
        'titulo':'Productos',
        'productos':productos,
    })

def login(request):
    '''Función que controla el login del usuario'''
    if request.user.is_authenticated:#si el usuario ya esta autenticado evita que pueda acceder a la pagina de logeo
        return redirect('tienda')

    username = request.POST.get('username')
    password = request.POST.get('password')

    usuarios = authenticate(username=username, password=password)
    if usuarios:
        lg(request,usuarios)
        messages.success(request,f'Bienvenido {usuarios.username}')
        #Si es usuario es autenticado correctamente, se le redireccionara a la pagina principal de la tienda, con el mensaje de bienvenida
        if request.GET.get('next'):
            return HttpResponseRedirect(request.GET['next'])#lo va a llevar a donde el usuario previamente quiso entrar
        return redirect('tienda')
    


    else:
        messages.error(request,'Usuario y/o contraseña incorrecto')
        
    return render(request, 'user/login.html',{})

def salir(request):
    '''Funcion para cerrar sesion del usuario'''
    logout(request)
    messages.success(request,'Sesión Finalizada')
    return redirect(login)

def registro(request):
    '''funcion que incluye el formulario de registro de un nuevo cliente'''
    if request.user.is_authenticated:#si el usuario ya esta autenticado evita que pueda acceder a la pagina de registro
        return redirect('tienda')

    form = Registro(request.POST or None) #Almacena lo que hay en la clase Registro del archivo forms
    if request.method=='POST' and form.is_valid():
       
       nombre = form.cleaned_data.get('nombre')
       apellido = form.cleaned_data.get('apellido')
       username = form.cleaned_data.get('username') 
       correo = form.cleaned_data.get('correo')
       password = form.cleaned_data.get('password')


       usuario = User.objects.create_user(username,correo,password) #almacena las variables creadas anteriormente con el metodo User
       usuario.last_name=apellido
       usuario.first_name=nombre
       usuario.save()

       if usuario:
           #Si el usuario es creado correctamente se redirecciona a la pagina principal de la tienda
           lg(request,usuario)
           messages.success(request,f'Bienvenido {nombre}')
           return redirect('tienda')

    return render(request,'user/registro.html',{
        'form':form
    })