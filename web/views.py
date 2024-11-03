from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Usuario, Nave_Usuario, Nave, User, Tripulacion, Tripulacion_Usuario
from django.contrib import messages
from web.services import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def inicio(request):
    miUsuario = request.user.usuario
    return render(request, "inicio.html",{"Usuario": miUsuario})

def registro(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST['nombre']
        password = request.POST['contrasena']
        userCreado = User.objects.create_user(
            username=username,
            password=password,
            is_staff= False,
            is_superuser=False  
        )
        userCreado.save()
        miUsuario = Usuario.objects.create(acciones=100, poder=100, user = userCreado)
        miUsuario.save()
        minave = Nave.objects.get(id = 6)
        naveCreada= Nave_Usuario.objects.create(Usuario = miUsuario, Nave = minave, resistencia =minave.resistencia)
        naveCreada.save()

        return redirect('index')
    else:
        form = UserForm()
    return render(request, 'registro.html', {'form': form})

def ranking(request):
    listaJugadores = Usuario.objects.all()
    return render(request, "ranking.html", {"listaJugadores": listaJugadores})

def nave(request):
    miUsuario = request.user.usuario
    miNave = Nave_Usuario.objects.get(Usuario= miUsuario)
    resistencia = miNave.resistencia
    miNave = Nave.objects.get(id = miNave.id)
                
    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    listaMisTripulantes = list()
    for item in listaTripulantesdeUsuario:
        listaMisTripulantes.append(item.Tripulacion)
        miNave.ataque += item.Tripulacion.ataque
        miNave.defensa += item.Tripulacion.defensa


    return render(request, "nave.html",{"miNave":miNave, "misTripulantes": listaMisTripulantes, "resistencia": resistencia})

def reclutar(request):

    miUsuario = request.user.usuario

    listaTripulacion = Tripulacion.objects.all()
    listatripulantes = Tripulacion_Usuario.objects.filter(Usuario=miUsuario)

    # Obtener una lista de IDs de Tripulacion en listatripulantes
    tripulantes_ids = listatripulantes.values_list('Tripulacion_id', flat=True)

    # Excluir los tripulantes que ya están en listatripulantes
    listaTripulacion = listaTripulacion.exclude(id__in=tripulantes_ids).order_by("?")
    
    return render(request, "reclutar.html", {"tripulantes": listaTripulacion})


def reclutarTripulante(request):
    idTripulante = request.GET["id"]

    miTripulante = Tripulacion.objects.get(id = idTripulante)
    miUsuario = request.user.usuario
    if (miUsuario.oro >= miTripulante.precio):
        miUsuario.oro -= miTripulante.precio
        miTripulacion = Tripulacion_Usuario.objects.create(
            Tripulacion = miTripulante,
            Usuario = miUsuario
        )
        miUsuario.save()
        miTripulacion.save()
        EjecutaAccion(miUsuario,10)
    return redirect('inicio')

def batalla(request):

    if request.method == "POST":

        miUsuario = request.user.usuario
        idOponente = int(request.POST.get('atacar'))
        oponenteUser = User.objects.get(id=idOponente)
        oponenteUsuario = oponenteUser.usuario
        relatoBatalla = EjecutarBatalla(miUsuario, oponenteUsuario)
        EjecutaAccion(miUsuario, 20)

    return render(request, "batalla.html",{"relatoBatalla": relatoBatalla})

def explorar(request):
    miUsuario = request.user.usuario
    relatoExploracion=""
    if request.method == "POST":
        acciones = request.POST['acciones']
        relatoExploracion = EjecutarExplorar(miUsuario, acciones)

    return render(request, "explorar.html", {"mensaje":relatoExploracion})

def taller(request):
    miUsuario = request.user.usuario
    miNave = Nave_Usuario.objects.get(Usuario= miUsuario)
    resistenciaActual = miNave.resistencia
    miNave = Nave.objects.get(id = miNave.Nave.id)
    resistenciaTotal = miNave.resistencia
                
    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    listaMisTripulantes = list()
    for item in listaTripulantesdeUsuario:
        listaMisTripulantes.append(item.Tripulacion)
        miNave.ataque += item.Tripulacion.ataque
        miNave.defensa += item.Tripulacion.defensa
        miNave.radar += item.Tripulacion.radar


    return render(request, "taller.html",{"miNave":miNave, "resistenciaActual": resistenciaActual, "resistenciaTotal":resistenciaTotal})