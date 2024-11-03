from .models import Usuario, Tripulacion_Usuario, Nave_Usuario, Nave
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

    return relatoBatalla

def EjecutarExplorar(miUsuario, acciones):

    miNaveUsuario = Nave_Usuario.objects.get(Usuario= miUsuario)
    miNave = Nave.objects.get(id = miNaveUsuario.id)
    miNave.radar

    listaTripulantesdeUsuario = Tripulacion_Usuario.objects.filter(Usuario = miUsuario)
    for item in listaTripulantesdeUsuario:
        miNave.radar += item.Tripulacion.radar


    relatoExploracion=""
    for i in range(int(acciones)):
        probabilidad = random.randint(1, 100)
    
        # Verifica si el número generado está dentro del rango de radar
        if probabilidad <= miNave.radar:
            busqueda = random.randint(1, 4)  # Genera un número entre 1 y 4
            if busqueda == 1:
                relatoExploracion+=" Encontraste 3 recursos. <br>"
            elif busqueda == 2:
                relatoExploracion+=" Encontraste 1 aliado. <br>"
            elif busqueda == 3:
                relatoExploracion+=" Encontraste 10 oro. <br>"
            else:
                relatoExploracion+=" Encontraste 5 recursos. <br>"

        else:
            relatoExploracion+="No encontraste nada. <br>"
    
    return relatoExploracion+" RADAR: "+ str(miNave.radar)

    
