from django.shortcuts import render,redirect
from django.db import connection
import cx_Oracle

# Create your views here.


def home(request):
    data={
        'productos': lista_productos()
    }
    return render(request, 'app/home.html',data)

def ofertas(request):
    return render(request, 'app/ofertas.html')

def detalle(request,id):
    data={
        'producto': get_producto(id)
    }
    return render(request, 'app/detalle.html',data)

def hora(request):
    data = {}
    if request.method == 'POST':
        Rut= request.POST.get('rut')
        Nombre= request.POST.get('nombre')
        Apellido= request.POST.get('apellido')
        Patente= request.POST.get('patente')
        Telefono= request.POST.get('telefono')
        Fecha= request.POST.get('fecha')
        Descripcion= request.POST.get('descripcion')
        respuesta = agendar_hora(Rut,Nombre,Apellido,Patente,Telefono,Fecha,Descripcion)
        print(respuesta)
        if respuesta== 1:
            data['mensaje'] = Fecha
            data['validacion'] = 1
        else:
            data['mensaje'] = 'Error: Verifique los campos'
            data['validacion'] = 2
    return render(request, 'app/hora.html',data)

def auto(request):
    return render(request, 'app/autos.html')

def agendar_hora(Rut,Nombre,Apellido,Patente,Telefono,Fecha,Descripcion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    respuesta = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_SLCTD_HORA_WEB",[Rut,Nombre,Apellido,Patente,Telefono,Fecha,Descripcion,respuesta]) 
    return respuesta.getvalue()
 
def lista_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_GET_PRODUCTOS_P",[out_cur]) 

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista

def get_producto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_GET_PRODUCTO",[id,out_cur]) 

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista
