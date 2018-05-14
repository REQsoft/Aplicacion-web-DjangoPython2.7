"""administracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from adminapp import views
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^principal/', include('adminapp.urls', namespace="principal")),
    url(r'^listarbd/$',views.listarbd,name='listarbd'),
    url(r'^conexion/$',views.conexion,name='conexion_list'),

    url(r'^$',login, {'template_name':'vistas/index.html'},name='login'),
    url(r'^accounts/login/',login, {'template_name':'vistas/index.html'},name='login'),
    url(r'^logout/',logout_then_login,name='logout'),
]