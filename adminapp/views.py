# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from adminapp.forms import ConexionForm, ServicioForm, DirectorioForm, LocalizacionForm
from adminapp.models import Conexion, Sql, Directorio, Localizacion, Articulo, Parametrizacion
from adminapp.classes import Conectar
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse
from adminapp.serializers import ArticuloSerializer, DirectorioSerializer, LocalizacionSerializer, ParametrizacionSerializer, ServicioSerializer
from rest_framework import generics, viewsets,status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView 
import json
from rest_framework.response import Response 
from . import serializers
from collections import defaultdict
import collections


# Crea la vista principal(index).
def index(request):
    return render(request, 'vistas/principal.html')

# Crea la vista bienvenida.
def bienvenido(request):
    return render(request, 'vistas/bienvenido.html')

#Vistas Conexion
# Crea la vista formulario nueva conexion.
def conexion_new(request):
    if request.method == 'POST':
        form = ConexionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:conexion_listar')
    else: 
        form = ConexionForm()
        return render (request, 'vistas/conexion/conexion_new.html', {'form':form})
    
# Crea la vista lista conexion.
def conexion_list(request):
    conexion = Conexion.objects.all().order_by('id')
    contexto = {'conexion':conexion}
    return render(request, 'vistas/conexion/conexion_list.html', contexto)

# Crea la vista editar conexion.
def conexion_edit(request, id_conexion):
    conexion = Conexion.objects.get(id=id_conexion)
    if request.method == 'GET':
        form = ConexionForm(instance = conexion)
    else:
        form = ConexionForm(request.POST, instance = conexion)
        if form.is_valid():
            form.save()
        return redirect('principal:conexion_listar')
    return render (request, 'vistas/conexion/conexion_new.html', {'form':form})

# Crea la vista eliminar conexion.
def conexion_delete(request, id_conexion):
    conexion = Conexion.objects.get(id=id_conexion)
    if request.method == 'POST':
        conexion.delete()
        return redirect('principal:conexion_listar')
    return render (request, 'vistas/conexion/conexion_delete.html', {'conexion':conexion})  

#Vistas Servicios
# Crea la vista formulario nuevo servicio.
def servicio_new(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:servicio_listar')
    else: 
        form = ServicioForm()
        return render (request, 'vistas/servicios/servicio_new.html', {'form':form})
    
# Crea la vista lista servicio.
def servicio_list(request):
    servicio = Sql.objects.all().order_by('id')
    contexto = {'servicio':servicio}
    return render(request, 'vistas/servicios/servicio_list.html', contexto)

# Crea la vista editar servicio.
def servicio_edit(request, id_servicio):
    servicio = Sql.objects.get(id=id_servicio)
    if request.method == 'GET':
        form = ServicioForm(instance = servicio)
    else:
        form = ServicioForm(request.POST, instance = servicio)
        if form.is_valid():
            form.save()
        return redirect('principal:servicio_listar')
    return render (request, 'vistas/servicios/servicio_new.html', {'form':form})

# Crea la vista crear conexion.  
def conexion(request):
	conexion_list=Conexion.objects.all()
	context = {'object_list':conexion_list}
	return render(request,'conexion_new.html', context)

# Crear la vista para listar las base de datos con los parametros ingresados en el ssitema.
def listarbd(request):
    global bds
    motor=request.GET['motor']    
    obj=Conectar.Conectar()
    if motor=='postgres':  
            bds=obj.conectarPostgres(request.GET['usuario'],request.GET['contrasenia'],request.GET['servidor'],request.GET['puerto'])
    elif motor=='mysql':
            bds=obj.conectarMysql(request.GET['usuario'],request.GET['contrasenia'],request.GET['servidor'],request.GET['puerto'])
    context = {'object_list':bds}
    return render(request,'vistas/conexion/listarbd.html', context)

#Vistas Directorio
# Crea la vista formulario nuevo directorio.
def directorio_new(request):
    if request.method == 'POST':
        form = DirectorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:directorio_listar')
    else: 
        form = DirectorioForm()
        return render (request, 'vistas/directorio/directorio_new.html', {'form':form})
    
# Crea la vista lista directorios.
def directorio_list(request):
    directorio = Directorio.objects.all().order_by('id')
    contexto = {'directorio':directorio}
    return render(request, 'vistas/directorio/directorio_list.html', contexto)

# Crea la vista editar directorio.
def directorio_edit(request, id_directorio):
    directorio = Directorio.objects.get(id=id_directorio)
    if request.method == 'GET':
        form = DirectorioForm(instance = directorio)
    else:
        form = DirectorioForm(request.POST, instance = directorio)
        if form.is_valid():
            form.save()
        return redirect('principal:directorio_listar')
    return render (request, 'vistas/directorio/directorio_new.html', {'form':form})

# Crea la vista eliminar directorio.
def directorio_delete(request, id_directorio):
    directorio = Directorio.objects.get(id=id_directorio)
    if request.method == 'POST':
        directorio.delete()
        return redirect('principal:directorio_listar')
    return render (request, 'vistas/directorio/directorio_delete.html', {'directorio':directorio})

#Vistas Georreferenciación
# Crea la vista formulario nuevo georreferenciación.
def localizacion_new(request):
    if request.method == 'POST':
        form = LocalizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:localizacion_listar')
    else: 
        form = LocalizacionForm()
        return render (request, 'vistas/localizacion/localizacion_new.html', {'form':form})
    
# Crea la vista lista georreferenciación.
def localizacion_list(request):
    localizacion = Localizacion.objects.all().order_by('id')
    contexto = {'localizacion':localizacion}
    return render(request, 'vistas/localizacion/localizacion_list.html', contexto)

# Crea la vista editar georreferenciación.
def localizacion_edit(request, id_localizacion):
    localizacion = Localizacion.objects.get(id=id_localizacion)
    if request.method == 'GET':
        form = LocalizacionForm(instance = localizacion)
    else:
        form = LocalizacionForm(request.POST, instance = localizacion)
        if form.is_valid():
            form.save()
        return redirect('principal:localizacion_listar')
    return render (request, 'vistas/localizacion/localizacion_new.html', {'form':form})

# Crea la vista eliminar georreferenciación.
def localizacion_delete(request, id_localizacion):
    localizacion = Localizacion.objects.get(id=id_localizacion)
    if request.method == 'POST':
        localizacion.delete()
        return redirect('principal:localizacion_listar')
    return render (request, 'vistas/localizacion/localizacion_delete.html', {'localizacion':localizacion})

#Vistas Articulos Extraviados
# Crea la vista formulario nuevo articulos extraviados.
class ArticuloCreate(CreateView):
    model = Articulo
    fields = '__all__'
    def get_success_url(self):
        return reverse('principal:articulo_listar')
    
# Crea la vista lista articulos extraviados.
def articulo_list(request):
    articulo = Articulo.objects.all().order_by('id')
    contexto = {'articulo':articulo}
    return render(request, 'vistas/articulo/articulo_list.html', contexto)

# Crea la vista editar articulos extraviados.
class ArticuloUpdate(UpdateView):
    model = Articulo
    fields = '__all__'
    def get_success_url(self):
        return reverse('principal:articulo_listar')

# Crea la vista eliminar articulos extraviados.
def articulo_delete(request, id_descripcion):
    articulo = Articulo.objects.get(id=id_descripcion)
    if request.method == 'POST':
        articulo.delete()
        return redirect('principal:articulo_listar')
    return render (request, 'vistas/articulo/articulo_delete.html', {'articulo':articulo})

# Crea la vista que permite visualizar el serializar de los servicios.
class ServiciosList(ListAPIView):
    queryset = Sql.objects.all()
    serializer_class = ServicioSerializer
# Crea la vista que permite visualizar el serializar de los artículos.
class ArticuloList(ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
# Crea la vista que permite visualizar el serializar de deirectorio telefónico.
class DirectorioList(ListAPIView):
    queryset = Directorio.objects.all()
    serializer_class = DirectorioSerializer
    
# Crea la vista que permite visualizar el serializar de locaclización.    
class LocalizacionList(ListAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer
    
# Crea la vista que permite visualizar el serializar de parametrización.    
def parametrizacion_list(request):
    parametrizacion = Parametrizacion.objects.all().order_by('id')
    contexto = {'parametrizacion':parametrizacion}
    return render(request, 'vistas/parametrizacion/parametrizacion_list.html', contexto)

# Crea la vista que permite editar la parametrización.  
class ParametrizacionUpdate(UpdateView):
    model = Parametrizacion
    fields = '__all__'
    def get_success_url(self):
        return reverse('principal:parametrizacion_listar')
    
# Crea la vista que permite visualizar la foto en parametrización.  
class FotoPDetailView(DetailView):
    model = Parametrizacion
    
# Crea la vista que permite visualizar la parametrización.  
class ParametrizacionList(ListAPIView):
    queryset = Parametrizacion.objects.all()
    serializer_class = ParametrizacionSerializer
    
# Crea la vista para cada servicio.      
class ServicioList(APIView):
    def post(self):
        pass
    
    def get(self, request, id_servicio):
        obj=Conectar.Conectar() 
        servicio = Sql.objects.get(id=id_servicio)
        conexion = Conexion.objects.get(nombre = servicio.conexion)
        if(id_servicio=='1'):
            return ofertaAcademica(self, obj, servicio, conexion)
        elif(id_servicio=='2'):
            return listaEstudiantes(self, obj, servicio, conexion)
        elif(id_servicio=='3'):
            return hojaVida(self, obj, servicio, conexion)
        elif(id_servicio=='4'):
            return consultaNotas(self, obj, servicio, conexion)
        elif(id_servicio=='5'):
            return consultaMaterias(self, obj, servicio, conexion)
        else:
            return Response("Error en el servicio")
        
# Crea la vista de estudiantes.  
def listaEstudiantes(self, obj, servicio, conexion):       
        
        list = obj.ejecutarServicios(conexion.usuario,conexion.contrasena, conexion.ip,str(conexion.puerto),conexion.bd,servicio.sql, conexion.motor)    
        
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
        list8=[]
        print(list)
        for i in list:
            list1.append(i[0])
            list2.append(i[1])
            list3.append(i[2])
            list4.append(i[3])
            list5.append(i[4])
            list6.append(i[5])

        j=0
        materias = []
        while j<len(list1):
            materias.append({'codigo':list1[j],'nombres':list2[j],'apellidos':list3[j],'semestre':list4[j], 'materia':list5[j], 'programa':list6[j]})
            j+=1
        
        serializer = json.dumps(materias)
        return Response(json.loads(serializer))   
    
def get_dic_from_two_lists(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }

# Crea la vista de oferta academica.  
def ofertaAcademica(self, obj, servicio,conexion):       
            
        list = obj.ejecutarServicios(conexion.usuario,conexion.contrasena, conexion.ip,str(conexion.puerto),conexion.bd,servicio.sql, conexion.motor)    

        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
        list8=[]
        list9=[]
        list10=[]
        for i in list:
            list1.append(i[0])
            list2.append(i[1])
            list3.append(i[2])
            list4.append(i[3])
            list5.append(i[4])
            list6.append(i[5])  
            list7.append(i[6])  
            list8.append(i[7])  
            list9.append(i[8])  
            list10.append(i[9])  
        j=0
        oferta = []
        while j<len(list1):
            oferta.append({'codigo':list1[j],'formacion':list2[j],'titulo':list3[j],                   'lugar':list4[j],'metodologia':list5[j],'creditos':list6[j],'periodicidad':list7[j],
                          'duracion':list8[j],'jornada':list9[j],'valor':list10[j]})
            j+=1

        serializer = json.dumps(oferta)
        return Response(json.loads(serializer))
    
# Crea la vista de hoja de vida.  
def hojaVida(self, obj, servicio, conexion):       
            
        list = obj.ejecutarServicios(conexion.usuario,conexion.contrasena, conexion.ip,str(conexion.puerto),conexion.bd,servicio.sql, conexion.motor)    

        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
        list8=[]
        for i in list:
            list1.append(i[0])
            list2.append(i[1])
            list3.append(i[2])
            list4.append(i[3])
            list5.append(i[4])
            list6.append(i[5])  
            list7.append(i[6])  
            list8.append(i[7])   
        j=0
        hoja = []
        while j<len(list1):
            hoja.append({'identificacion':list1[j],'nombres':list2[j],'apellidos':list3[j],                   'direccion':list4[j],'telofono':list5[j],'estado_civil':list6[j],'email':list7[j],
                          'tipo_sangre':list8[j]})
            j+=1

        serializer = json.dumps(hoja)
        return Response(json.loads(serializer))
    
# Crea la vistaque permite consultar notas a los estudiantes.      
def consultaNotas(self, obj, servicio, conexion):       
            
        list = obj.ejecutarServicios(conexion.usuario,conexion.contrasena, conexion.ip,str(conexion.puerto),conexion.bd,servicio.sql, conexion.motor)    
        
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
        list8=[]
        print(list)
        for i in list:
            list1.append(i[0])
            list2.append(i[1])
            list3.append(i[2])
            list4.append(i[3])
            list5.append(i[4])

        j=0
        materias = []
        while j<len(list1):
            materias.append({'codigo_estudiante':list1[j],'codigo_materia':list2[j],'materia':list3[j], 'nota':list4[j], 'faltas':list5[j]})
            j+=1
        
        serializer = json.dumps(materias)
        return Response(json.loads(serializer))
    
    
# Crea la vista que permite consultar materias.  
def consultaMaterias(self, obj, servicio, conexion):       
            
        list = obj.ejecutarServicios(conexion.usuario,conexion.contrasena, conexion.ip,str(conexion.puerto),conexion.bd,servicio.sql, conexion.motor)    

        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]

        for i in list:
            list1.append(i[0])
            list2.append(i[1])
            list3.append(i[2])
            list4.append(i[3])
            list5.append(i[4])
            list6.append(i[5])

        j=0
        materias = []
        while j<len(list1):
            materias.append({'codigo':list1[j],'nombres':list2[j],'tipo':list3[j],'categoria':list4[j],                   'creditos':list5[j], 'programa':list6[j]})
            j+=1

        serializer = json.dumps(materias)
        return Response(json.loads(serializer))

# Crea la vista de usuarios.  
class UsuariosList(APIView):    
    def post(self):
        pass
    def get(self, request):
        obj=Conectar.Conectar() 
        conexion = Conexion.objects.get(nombre = 'Usuarios')
        sql="select * from usuario;"
        list = obj.ejecutarServicios(conexion.usuario,conexion.contrasena, conexion.ip,str(conexion.puerto),conexion.bd,sql, conexion.motor)    

        list1=[]
        list2=[]
        list3=[]

        for i in list:
            list1.append(i[1])
            list2.append(i[2])
            list3.append(i[3])

        j=0
        usuarios = []
        while j<len(list1):
            usuarios.append({'codigo':list1[j],'usuario':list2[j],'rol':list3[j]})
            j+=1

        serializer = json.dumps(usuarios)
        return Response(json.loads(serializer))