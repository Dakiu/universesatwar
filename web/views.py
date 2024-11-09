from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Usuario, Nave_Usuario, Nave, User, Tripulacion, Tripulacion_Usuario, RegistroBatalla
from django.contrib import messages
from web.services import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def inicio(request):
    miUsuario = request.user.usuario
    ataquesHechos = list(RegistroBatalla.objects.filter(atacante_id = miUsuario.id))
    ataquesRecibidos = list(RegistroBatalla.objects.filter(defensor_id = miUsuario.id))
    bitacora = ataquesHechos + ataquesRecibidos
    return render(request, "inicio.html",{"usuario": miUsuario, "bitacora":bitacora})

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
        naveCreada= Nave_Usuario.objects.create(Usuario = miUsuario, 
                                                Nave = minave, 
                                                resistencia =minave.resistencia,
                                                ataque = minave.ataque,
                                                defensa = minave.defensa,
                                                escudos = minave.escudos,
                                                radar= minave.radar,
                                                comunicaciones= minave.comunicaciones)
        naveCreada.save()

        return redirect('index')
    else:
        form = UserForm()
    return render(request, 'registro.html', {'form': form})

def ranking(request):
    miUsuario = request.user.usuario
    listaJugadores = Usuario.objects.all()
    return render(request, "ranking.html", {"listaJugadores": listaJugadores, "usuario": miUsuario})

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


    return render(request, "nave.html",{"miNave":miNave, "misTripulantes": listaMisTripulantes, "resistencia": resistencia, "usuario":miUsuario})

def reclutar(request):
    mensajeError = ""
    miUsuario = request.user.usuario
    listaTripulacion = Tripulacion.objects.all()
    listatripulantes = Tripulacion_Usuario.objects.filter(Usuario=miUsuario)

    # Obtener una lista de IDs de Tripulacion en listatripulantes
    tripulantes_ids = listatripulantes.values_list('Tripulacion_id', flat=True)

    # Excluir los tripulantes que ya están en listatripulantes
    listaTripulacion = listaTripulacion.exclude(id__in=tripulantes_ids).order_by("?")

#AQUI
    if (request.method == "GET" and request.GET.get("id")):
        idTripulante = request.GET.get("id")
        miTripulante = Tripulacion.objects.get(id = idTripulante)
        #miUsuario = request.user.usuario
        if (miUsuario.oro >= miTripulante.precio and int(miUsuario.acciones > 10)):
            miUsuario.oro -= miTripulante.precio
            miTripulacion = Tripulacion_Usuario.objects.create(
                Tripulacion = miTripulante,
                Usuario = miUsuario
            )
            miUsuario.save()
            miTripulacion.save()
            EjecutaAccion(miUsuario,10)
        
        else:
            mensajeError = "No hay suficiente oro o acciones"

    
#HASTA AQUI
    return render(request, "reclutar.html", {"tripulantes": listaTripulacion, "usuario": miUsuario, "mensajeError":mensajeError})


# def reclutarTripulante(request):
#     idTripulante = request.GET["id"]
#     mensajeError = ""
#     miTripulante = Tripulacion.objects.get(id = idTripulante)
#     miUsuario = request.user.usuario
#     if (miUsuario.oro >= miTripulante.precio):
#         miUsuario.oro -= miTripulante.precio
#         miTripulacion = Tripulacion_Usuario.objects.create(
#             Tripulacion = miTripulante,
#             Usuario = miUsuario
#         )
#         miUsuario.save()
#         miTripulacion.save()
#         EjecutaAccion(miUsuario,10)
#     else:
#         mensajeError = "No hay suficiente oro"
        
#     return render(request, "reclutar.html", {"tripulantes": listaTripulacion, "usuario": miUsuario, "mensajeError":mensajeError})
#     #return redirect('inicio')

def batalla(request):

    if request.method == "POST":
        miUsuario = request.user.usuario
        idOponente = int(request.POST.get('atacar'))
        oponenteUser = User.objects.get(id=idOponente)
        oponenteUsuario = oponenteUser.usuario
        relatoBatalla = EjecutarBatalla(miUsuario, oponenteUsuario)
        EjecutaAccion(miUsuario, 20)

    return render(request, "batalla.html",{"relatoBatalla": relatoBatalla, "usuario": miUsuario})

def explorar(request):
    miUsuario = request.user.usuario
    relatoExploracion=""
    mensajeError = ""
    if request.method == "POST":
        acciones = int(request.POST['acciones'])
        if int(miUsuario.acciones) >= acciones:
            relatoExploracion = EjecutarExplorar(miUsuario, acciones)
        else:
            mensajeError= "No hay suficientes acciones."

    return render(request, "explorar.html", {"mensaje":relatoExploracion,"usuario": miUsuario,"mensajeError":mensajeError})

def taller(request):
    miUsuario = request.user.usuario
    miNaveUsuario = Nave_Usuario.objects.get(Usuario= miUsuario)
    miNave = Nave.objects.get(id = miNaveUsuario.Nave.id)
    mensajeError = ""

    if request.method == "POST":
        acciones = int(request.POST['acciones'])
        if int(miUsuario.acciones) >= acciones:
            mensajeError = EjecutarTaller (acciones, request.POST, miUsuario, miNaveUsuario, miNave)
        else:
            mensajeError= "No hay suficientes acciones."

    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    for item in listaTripulantesdeUsuario:
        miNave.ataque += item.Tripulacion.ataque
        miNave.defensa += item.Tripulacion.defensa
        miNave.radar += item.Tripulacion.radar

    return render(request, "taller.html",{"miNave":miNave, "miNaveUsuario":miNaveUsuario, "usuario": miUsuario,"mensajeError":mensajeError})