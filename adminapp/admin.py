# -*- coding: utf-8 -*-
from django.contrib import admin
from adminapp.models import Conexion, Sql, Directorio, Localizacion, Articulo, Parametrizacion
# Registrar el modelo de la base de datos para el administrador.
# Modelo en la base de datos para la conexión.
admin.site.register(Conexion)
# Modelo en la base de datos para la sentencia SQL.
admin.site.register(Sql)
# Modelo en la base de datos para el directorio telefónico.
admin.site.register(Directorio)
# Modelo en la base de datos para la localización.
admin.site.register(Localizacion)
# Modelo en la base de datos para artículos perdidos.
admin.site.register(Articulo)
# Modelo en la base de datos para la parametrización del sistema.
admin.site.register(Parametrizacion)