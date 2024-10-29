from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


# Create your views here.

def index(request):
    return render(request, "index.html")

def registro(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST['nombre']
        email = request.POST['correo']
        password = request.POST['contrasena']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password  
        )
        user.save()
        return redirect('index')
    else:
        form = UserForm()
    return render(request, 'registro.html', {'form': form})

def ranking(request):
    listaJugadores = User.objects.all()
    return render(request, "ranking.html", {"listaJugadores": listaJugadores})