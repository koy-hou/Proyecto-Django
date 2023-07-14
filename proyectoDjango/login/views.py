from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def root(request):
    return render(request,'login/login.html')

def login(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        if request.method == 'POST':
            
            user = Usuario.objects.filter(email=request.POST['email_login']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'first_name':usuario_registrado.first_name,
                        'last_name':usuario_registrado.last_name,
                        'email':usuario_registrado.email,
                        'rol':usuario_registrado.rol,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request,"Ingreso correcto!!!!")
                    return redirect('/login/success')
                else:
                    messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                    return redirect('/login/login')
            else:
                messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                return redirect('/login/')

def success(request):
    if 'usuario' not in request.session:
        return redirect('/login')
        
    return render(request, 'login/success.html')

def register(request):
    return render(request,'login/register.html')

def registerVal(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            errors = Usuario.objects.validador_campos(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)

                #Si se produce un error pero no queremos perder los datos....
                request.session['registro_nombre'] = request.POST['first_name']
                request.session['registro_apellido'] = request.POST['last_name']
                request.session['registro_email'] = request.POST['email']
                request.session['level_mensaje'] = 'alert-danger'
                return redirect('/login/register/')
            
            else:
                request.session['registro_nombre'] = ""
                request.session['registro_apellido'] = ""
                request.session['registro_email'] = ""

                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

                obj = Usuario.objects.create(first_name=first_name, last_name=last_name,email=email,password=password_hash)
                messages.success(request, "Usuario registrado con éxito!!!!")
                request.session['level_mensaje'] = 'alert-success'
                return redirect('/login/')
            
            # return redirect('/login/register/')

        return render(request, 'login/login.html')
    
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    messages.success(request,"Sesión cerrada correctamente!!!")
    return redirect('/login/')


def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    messages.success(request,"Sesión cerrada correctamente!!!")
    return redirect('/')