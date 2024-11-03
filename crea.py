import os
import django

# Configura Django para usar el entorno del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "universesatwar.settings")
django.setup()

from web.models import Nave, Tripulacion

def crear_naves():
    naves_data = [
        {"nombre": "Interceptor", "ataque": 10, "defensa": 10, "escudos": 8, "radar": 10, "comunicaciones": 10, "capacidadTripulantes": 8, "resistencia":20},
        {"nombre": "Explorador", "ataque": 5, "defensa": 10, "escudos": 20, "radar": 20, "comunicaciones": 10, "capacidadTripulantes": 8, "resistencia":10},
        {"nombre": "Fragata", "ataque": 20, "defensa": 15, "escudos": 10, "radar": 60, "comunicaciones": 10, "capacidadTripulantes": 10, "resistencia":30},
        {"nombre": "Carguero", "ataque": 20, "defensa": 60, "escudos": 10, "radar": 30, "comunicaciones": 10, "capacidadTripulantes": 20, "resistencia":50},        
        {"nombre": "Destructor", "ataque": 30, "defensa": 70, "escudos": 60, "radar": 40, "comunicaciones": 10, "capacidadTripulantes": 30, "resistencia":50},
        {"nombre": "Crucero", "ataque": 50, "defensa": 80, "escudos": 70, "radar": 60, "comunicaciones": 10, "capacidadTripulantes": 40, "resistencia":60},
    ]

    # Crear cada nave en la base de datos
    for nave_data in naves_data:
        nave = Nave(**nave_data)
        nave.save()
        print(f"Nave '{nave.nombre}' creada con éxito.")
        

def crear_tripulantes():
    tripulacion_data = [
        {"nombre": "Bohdan Troufal", "imagen": "", "ataque": 1, "defensa": 1, "precio": 10},
        {"nombre": "Medard Pavlík", "imagen": "", "ataque": 2, "defensa": 4, "precio": 20},
        {"nombre": "Kaiden Barrett", "imagen": "", "ataque": 3, "defensa": 3, "precio": 30},
        {"nombre": "Sebastian Booth", "imagen": "", "ataque": 4, "defensa": 2, "precio": 30},
        {"nombre": "Kate Mills", "imagen": "", "ataque": 2, "defensa": 3, "precio": 20},
        {"nombre": "Maitea Fetuccini", "imagen": "", "ataque": 3, "defensa": 2, "precio": 20},
        {"nombre": "Edenia Von Brocken", "imagen": "", "ataque": 1, "defensa": 4, "precio": 50},
        {"nombre": "Claudie Saxon", "imagen": "", "ataque": 4, "defensa": 1, "precio": 50},
    ]

    # Crear cada nave en la base de datos
    for tripulante in tripulacion_data:
        tripulantes = Tripulacion(**tripulante)
        tripulantes.save()
        print(f"Nave '{tripulantes.nombre}' creada con éxito.")

if __name__ == "__main__":
    crear_naves()
    crear_tripulantes()