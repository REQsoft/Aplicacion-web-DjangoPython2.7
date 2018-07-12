# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from adminapp.views import index, bienvenido
from adminapp.views import conexion_new, conexion_list, conexion_edit, conexion_delete
from adminapp.views import servicio_new, servicio_list, servicio_edit
from adminapp.views import directorio_new, directorio_list, directorio_edit, directorio_delete
from adminapp.views import localizacion_new, localizacion_list, localizacion_edit, localizacion_delete
from adminapp.views import articulo_list, articulo_delete, parametrizacion_list, FotoPDetailView
from adminapp import views
from rest_framework. urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    #Urls principal.
    url(r'^$', login_required(index), name='index'),
    url(r'^$', login_required(bienvenido), name='bienvenido'),
    #Urls para gestionar conexiones.
    url(r'^nconexion$', login_required(conexion_new), name='conexion_crear'),
    url(r'^lconexion$',login_required(conexion_list), name='conexion_listar'), 
    url(r'^edconexion/(?P<id_conexion>\d+)/$', login_required(conexion_edit), name='conexion_editar'),
    url(r'^elconexion/(?P<id_conexion>\d+)/$', login_required(conexion_delete), name='conexion_eliminar'), 
    #Urls para gestionar servicios.
    url(r'^nservicio$', login_required(servicio_new), name='servicio_crear'),
    url(r'^lservicio$', login_required(servicio_list), name='servicio_listar'),
    url(r'^edservicio/(?P<id_servicio>\d+)/$', login_required(servicio_edit), name='servicio_editar'),
    #Urls para gestionar el directorio telefónico.
    url(r'^ndirectorio$', login_required(directorio_new), name='directorio_crear'),
    url(r'^ldirectorio$', login_required(directorio_list), name='directorio_listar'),
    url(r'^eddirectorio/(?P<id_directorio>\d+)/$', login_required(directorio_edit), name='directorio_editar'),
    url(r'^eldirectorio/(?P<id_directorio>\d+)/$', login_required(directorio_delete), name='directorio_eliminar'), 
    #Urls para gestionar georreferenciación.
    url(r'^nlocalizacion$', login_required(localizacion_new), name='localizacion_crear'),
    url(r'^llocalizacion$', login_required(localizacion_list), name='localizacion_listar'),
    url(r'^edlocalizacion/(?P<id_localizacion>\d+)/$', login_required(localizacion_edit), name='localizacion_editar'),
    url(r'^ellocalizacion/(?P<id_localizacion>\d+)/$', login_required(localizacion_delete), name='localizacion_eliminar'),
    #Urls para gestionar artículos perdidos.
    url(r'^narticulo$', login_required(views.ArticuloCreate.as_view()), name='articulo_crear'),
    url(r'^larticulo$', login_required(articulo_list), name='articulo_listar'),
    url(r'^edarticulo/(?P<pk>\d+)/update/$', login_required(views.ArticuloUpdate.as_view()), name='articulo_editar'),
    url(r'^elarticulo/(?P<id_descripcion>\d+)/$', login_required(articulo_delete), name='articulo_eliminar'),    
    #Urls para poder listar los diferentes servicios con la ayuda de Django Rest Framework y poder mostrarlos en formato Json.
    url(r'^articulo/$', views.ArticuloList.as_view(),name='articuloList'),
    url(r'^directorio/$', views.DirectorioList.as_view(),name='directorioList'),
    url(r'^localizacion/$', views.LocalizacionList.as_view(),name='localizacionList'),
    url(r'^servicios/$', views.ServiciosList.as_view(),name='serviciosList'),
    url(r'^usuarios/$', views.UsuariosList.as_view(),name='usuariosList'),
    url(r'^servicio/(?P<id_servicio>\d+)/$',views. ServicioList.as_view(),name='servicio'),
    url(r'^lparametrizacion$', login_required(parametrizacion_list), name='parametrizacion_listar'),
    url(r'^edparametrizacion/(?P<pk>\d+)/update/$', login_required(views.ParametrizacionUpdate.as_view()), name='parametrizacion_editar'),
    url(r'^fotoP/(?P<pk>\d+)/detail/$',views.FotoPDetailView.as_view(), name='foto-detail'),
    url(r'^parametrizacion/$', views.ParametrizacionList.as_view(),name='parametrizacionList'),
]

#Url utilizada para acceder a la carpeta en la cual tenemos guardadas las imágenes.
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
    
urlpatterns = format_suffix_patterns(urlpatterns)