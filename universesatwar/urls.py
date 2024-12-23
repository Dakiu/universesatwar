"""
URL configuration for universesatwar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('orden-lista', views.index, name ="ordenlista"),
    path('ordenes', views.index, name ="ordenes"),
    path('login',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='/', http_method_names=['get', 'post']),name='logout'),
    path('registro', views.registro, name='registro'),
    path('ranking', views.ranking, name='ranking'),
    path('nave', views.nave, name='nave'),
    path('reclutar', views.reclutar, name='reclutar'),
    # path('reclutarTripulante/', views.reclutarTripulante, name='reclutarTripulante'),
    path('inicio', views.inicio, name='inicio'),
    path('batalla', views.batalla, name='batalla'),
    path('explorar', views.explorar, name='batalla'),
    path('taller', views.taller, name='taller'),
]
