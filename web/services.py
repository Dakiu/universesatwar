from .models import Usuario, Tripulacion_Usuario, Nave_Usuario, Nave, RegistroBatalla
import random

def EjecutaAccion(usuario, accion):
    miUsuario = Usuario.objects.get(id =usuario.id)
    miUsuario.acciones -= accion
    miUsuario.save()

def EjecutarBatalla(miUsuario, oponenteUsuario):

    miNaveUsuario = Nave_Usuario.objects.get(Usuario= miUsuario)
    miNave = Nave.objects.get(id = miNaveUsuario.id)

    oponenteNaveUsuario = Nave_Usuario.objects.get(Usuario= oponenteUsuario)
    oponenteNave = Nave.objects.get(id = oponenteNaveUsuario.id)

    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    #listaMisTripulantes = list()
    #Sumar las estadísticas de los tripulantes de mi nave.
    for item in listaTripulantesdeUsuario:
        #listaMisTripulantes.append(item.Tripulacion)
        miNave.ataque += item.Tripulacion.ataque
        miNave.defensa += item.Tripulacion.defensa
    #Sumar las estadísticas de los tripulantes del enemigo
    listaTripulantesdeOponente = Tripulacion_Usuario.objects.filter(Usuario = oponenteUsuario)
    #listaMisTripulantes = list()
    #Sumar las estadísticas de los tripulantes.
    for item in listaTripulantesdeOponente:
        #listaMisTripulantes.append(item.Tripulacion)
        oponenteNave.ataque += item.Tripulacion.ataque
        oponenteNave.defensa += item.Tripulacion.defensa

    relatoBatalla=""

    relatoBatalla += miNave.nombre +" inicia el ataque <br>"
    relatoBatalla += "Dispara a "+oponenteNave.nombre +" <br>"
    miDaño = miNave.ataque - oponenteNave.defensa
    if (miDaño> 0):
        relatoBatalla += "causa "+ str(miDaño) +" de daño. <br><br>"
    else:
        relatoBatalla +="No causa daño."

    relatoBatalla += oponenteNave.nombre +" responde el ataque <br>"
    relatoBatalla += "Dispara a "+ miNave.nombre +" <br>"
    dañoRival = oponenteNave.ataque - miNave.defensa
    if (dañoRival> 0):
        relatoBatalla += "causa "+ str(dañoRival) +" de daño. <br>"
    else:
        relatoBatalla +="No causa daño."

    miNaveUsuario.resistencia -= dañoRival
    miNaveUsuario.save()

    oponenteNaveUsuario.resistencia -= miDaño
    oponenteNaveUsuario.save()

    batalla = RegistroBatalla.objects.create(
        atacante = miUsuario,
        defensor = oponenteUsuario,
        relatoBatalla = relatoBatalla
    )
    batalla.save()

    return relatoBatalla

def EjecutarExplorar(miUsuario, acciones):

    miNaveUsuario = Nave_Usuario.objects.get(Usuario= miUsuario)
    miNave = Nave.objects.get(id = miNaveUsuario.id)
    miNave.radar

    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    for item in listaTripulantesdeUsuario:
        miNave.radar += item.Tripulacion.radar

    relatoExploracion=""
    for i in range(acciones):
        probabilidad = random.randint(1, 100)

        miUsuario.acciones -=1
        miUsuario.save()
    
        # Verifica si el número generado está dentro del rango de radar
        if probabilidad <= miNave.radar:
            busqueda = random.randint(1, 4)  # Genera un número entre 1 y 4
            if busqueda == 1:
                relatoExploracion+=" Encontraste 3 recursos. <br>"
                miUsuario.recursos +=3
            elif busqueda == 2:
                relatoExploracion+=" Encontraste 1 aliado. <br>"
            elif busqueda == 3:
                relatoExploracion+=" Encontraste 10 oro. <br>"
                miUsuario.oro +=10
            else:
                relatoExploracion+=" Encontraste 5 recursos. <br>"
                miUsuario.recursos +=5

        else:
            relatoExploracion+="No encontraste nada. <br>"
    
    return relatoExploracion+" RADAR: "+ str(miNave.radar)



def EjecutarTaller(acciones, post, miUsuario, miNaveUsuario, miNave):
    mensajeError = ""
    if 'accion' in post:
        accion = post['accion']
        if accion == "repararResistencia":
            mensajeError = reparar(miUsuario, miNaveUsuario, 'resistencia', acciones, miNave)
        elif accion == "repararAtaque":
            mensajeError = reparar(miUsuario, miNaveUsuario, 'ataque', acciones, miNave)
        elif accion == "repararDefensa":
            mensajeError = reparar(miUsuario, miNaveUsuario, 'defensa', acciones, miNave)
        elif accion == "repararEscudos":
            mensajeError = reparar(miUsuario, miNaveUsuario, 'escudos', acciones, miNave)
        elif accion == "repararRadar":
            mensajeError = reparar(miUsuario, miNaveUsuario, 'radar', acciones, miNave)

        elif accion == "mejorarResistencia":
            mensajeError = mejorar(miUsuario, miNave, 'resistencia', acciones)
        elif accion == "mejorarAtaque":
            mensajeError =mejorar(miUsuario, miNave, 'ataque', acciones)
        elif accion == "mejorarDefensa":
            mensajeError = mejorar(miUsuario, miNave, 'defensa', acciones)
        elif accion == "mejorarEscudos":
            mensajeError = mejorar(miUsuario, miNave, 'escudos', acciones)
        elif accion == "mejorarRadar":
            mensajeError = mejorar(miUsuario, miNave, 'radar', acciones)
    return mensajeError
        
def reparar(miUsuario, miNaveUsuario, atributo, acciones, miNave):
    totalRecursosaUsar = acciones * 3
    if miUsuario.recursos >= totalRecursosaUsar:
        miUsuario.recursos -= totalRecursosaUsar
        miUsuario.save()
        if getattr(miNaveUsuario, atributo) + acciones > getattr(miNave, atributo):
            setattr(miNaveUsuario, atributo, getattr(miNave, atributo))
        else:
            setattr(miNaveUsuario, atributo, getattr(miNaveUsuario, atributo) + acciones)
        miNaveUsuario.save()
        return ""
    else:
        return "No hay suficientes recursos"

def mejorar(miUsuario, miNave, atributo, acciones):
    totalRecursosaUsar = acciones * 5
    totalOroaUsar = acciones * 10
    if miUsuario.recursos >= int(totalRecursosaUsar) and miUsuario.oro >= int(totalOroaUsar):
        miUsuario.recursos -= totalRecursosaUsar 
        miUsuario.oro -= totalOroaUsar 
        miUsuario.save()
        setattr(miNave, atributo, getattr(miNave, atributo) + acciones)
        miNave.save()
        return ""
    else:
        return "No hay suficientes recursos u oro"


def calcularPoder(miUsuario):
    poder = 1
    miNaveUsuario = Nave_Usuario.objects.get(Usuario= miUsuario) *5
    miNave = Nave.objects.get(id = miNaveUsuario.Nave.id) *5
    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    listaMisTripulantes = list()
    for item in listaTripulantesdeUsuario:
        poder *=2
        listaMisTripulantes.append(item.Tripulacion)
        miNave.ataque += item.Tripulacion.ataque
        miNave.defensa += item.Tripulacion.defensa
    
    return poder
