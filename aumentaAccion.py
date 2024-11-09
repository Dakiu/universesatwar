import os
import django

# Configura Django para usar el entorno del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "universesatwar.settings")
django.setup()

from web.models import Usuario

def aumenta_accion():
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        usuario.acciones = 100
        usuario.save()

if __name__ == "__main__":
    aumenta_accion()