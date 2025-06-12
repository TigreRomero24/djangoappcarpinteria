"""
URL configuration for carpinteria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from aplicaciones.empresa.views import *
from aplicaciones.trabajadores.views import *
from aplicaciones.productos.views import *
from aplicaciones.proveedores.views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('empresa/', empresadefecto.as_view()),
    path('nueva_empresa/', empresanueva.as_view(),),
    path('trabajadores/', trabajadordefecto.as_view()),
    path('nuevo_trabajador/', creartrabajadores.as_view()),
    path('productos/', productos_defecto.as_view()),
    path('nuevo_producto/', producto_nuevo.as_view()),
    path('proveedores/', proveedores_defecto.as_view()),
    path('nuevo_proveedor/', proveedor_nuevo.as_view()),

]
