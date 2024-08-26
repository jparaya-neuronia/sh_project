# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from decimal import Decimal
import json
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.db.models import Sum
from apps.home.models import * 
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def REGION_LISTALL(request):
    try:
        object_list = REGION.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/REGION/reg_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def REGION_ADDONE(request):
    try:
        if request.method =='POST':
            form = formREGION(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Región guardada correctamente')
                return redirect('/reg_listall/')
        form = formREGION()
        ctx = {
            'form': form
        }
        return render(request, 'home/REGION/reg_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def REGION_UPDATE(request, pk):
    try:
        region = REGION.objects.get(id=pk)
        if request.method == 'POST':
            form = formREGION(request.POST, instance=region)
            if form.is_valid():
                form.save()
                messages.success(request, 'Región actualizada correctamente')
                return redirect('/reg_listall/')
        form = formREGION(instance=region)
        ctx = {
            'form': form
        }
        return render(request, 'home/REGION/reg_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROVINCIA_LISTALL(request):
    try:
        object_list = PROVINCIA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/PROVINCIA/prov_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROVINCIA_ADDONE(request):
    try:
        if request.method =='POST':
            form = formPROVINCIA(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Provincia guardada correctamente')
                return redirect('/prov_listall/')
        form = formPROVINCIA()
        ctx = {
            'form': form
        }
        return render(request, 'home/PROVINCIA/prov_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROVINCIA_UPDATE(request, pk):
    try:
        provincia = PROVINCIA.objects.get(id=pk)
        if request.method == 'POST':
            form = formPROVINCIA(request.POST, instance=provincia)
            if form.is_valid():
                form.save()
                messages.success(request, 'Provincia actualizada correctamente')
                return redirect('/prov_listall/')
        form = formPROVINCIA(instance=provincia)
        ctx = {
            'form': form
        }
        return render(request, 'home/PROVINCIA/prov_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COMUNA_LISTALL(request):
    try:
        object_list = COMUNA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/COMUNA/com_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COMUNA_ADDONE(request):
    try:
        if request.method =='POST':
            form = formCOMUNA(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comuna guardada correctamente')
                return redirect('/com_listall/')
        form = formCOMUNA()
        ctx = {
            'form': form
        }
        return render(request, 'home/COMUNA/com_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COMUNA_UPDATE(request, pk):
    try:
        comuna = COMUNA.objects.get(id=pk)
        if request.method == 'POST':
            form = formCOMUNA(request.POST, instance=comuna)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comuna actualizada correctamente')
                return redirect('/com_listall/')
        form = formCOMUNA(instance=comuna)
        ctx = {
            'form': form
        }
        return render(request, 'home/COMUNA/com_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PARAMETRO_LISTALL(request):
    try:
        object_list = PARAMETRO.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/PARAMETRO/param_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PARAMETRO_ADDONE(request):
    try:
        if request.method =='POST':
            form = formPARAMETRO(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Parámetro guardado correctamente')
                return redirect('/param_listall/')
        form = formPARAMETRO()
        ctx = {
            'form': form
        }
        return render(request, 'home/PARAMETRO/param_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PARAMETRO_UPDATE(request, pk):
    try:
        parametro = PARAMETRO.objects.get(id=pk)
        if request.method == 'POST':
            form = formPARAMETRO(request.POST, instance=parametro)
            if form.is_valid():
                form.save()
                messages.success(request, 'Parámetro actualizado correctamente')
                return redirect('/param_listall/')
        form = formPARAMETRO(instance=parametro)
        ctx = {
            'form': form
        }
        return render(request, 'home/PARAMETRO/param_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ROL_LISTALL(request):
    try:
        object_list = ROL.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/ROL/rol_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ROL_ADDONE(request):
    try:
        if request.method =='POST':
            form = formROL(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Rol guardado correctamente')
                return redirect('/rol_listall/')
        form = formROL()
        ctx = {
            'form': form
        }
        return render(request, 'home/ROL/rol_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ROL_UPDATE(request, pk):
    try:
        rol = ROL.objects.get(id=pk)
        if request.method == 'POST':
            form = formROL(request.POST, instance=rol)
            if form.is_valid():
                form.save()
                messages.success(request, 'Rol actualizado correctamente')
                return redirect('/rol_listall/')
        form = formROL(instance=rol)
        ctx = {
            'form': form
        }
        return render(request, 'home/ROL/rol_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CATEGORIA_PROYECTO_LISTALL(request):
    try:
        object_list = CATEGORIA_PROYECTO.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/CATEGORIA_PROYECTO/catproy_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CATEGORIA_PROYECTO_ADDONE(request):
    try:
        if request.method =='POST':
            form = formCATEGORIA_PROYECTO(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Categoría de proyecto guardada correctamente')
                return redirect('/catproy_listall/')
        form = formCATEGORIA_PROYECTO()
        ctx = {
            'form': form
        }
        return render(request, 'home/CATEGORIA_PROYECTO/catproy_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CATEGORIA_PROYECTO_UPDATE(request, pk):
    try:
        categoria_proyecto = CATEGORIA_PROYECTO.objects.get(id=pk)
        if request.method == 'POST':
            form = formCATEGORIA_PROYECTO(request.POST, instance=categoria_proyecto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Categoría de proyecto actualizada correctamente')
                return redirect('/catproy_listall/')
        form = formCATEGORIA_PROYECTO(instance=categoria_proyecto)
        ctx = {
            'form': form
        }
        return render(request, 'home/CATEGORIA_PROYECTO/catproy_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CATEGORIA_CLIENTE_LISTALL(request):
    try:
        object_list = CATEGORIA_CLIENTE.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/CATEGORIA_CLIENTE/catcli_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CATEGORIA_CLIENTE_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formCATEGORIA_CLIENTE(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Categoría de cliente guardada correctamente')
                return redirect('/catcli_listall/')
        form = formCATEGORIA_CLIENTE()
        ctx = {
            'form': form
        }
        return render(request, 'home/CATEGORIA_CLIENTE/catcli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CATEGORIA_CLIENTE_UPDATE(request, pk):
    try:
        categoria_cliente = CATEGORIA_CLIENTE.objects.get(id=pk)
        if request.method == 'POST':
            form = formCATEGORIA_CLIENTE(request.POST, instance=categoria_cliente)
            if form.is_valid():
                form.save()
                messages.success(request, 'Categoría de cliente actualizada correctamente')
                return redirect('/catcli_listall/')
        form = formCATEGORIA_CLIENTE(instance=categoria_cliente)
        ctx = {
            'form': form
        }
        return render(request, 'home/CATEGORIA_CLIENTE/catcli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TIPO_PROYECTO_LISTALL(request):
    try:
        object_list = TIPO_PROYECTO.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/TIPO_PROYECTO/tipoproy_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TIPO_PROYECTO_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formTIPO_PROYECTO(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tipo de proyecto guardado correctamente')
                return redirect('/tipoproy_listall/')
        form = formTIPO_PROYECTO()
        ctx = {
            'form': form
        }
        return render(request, 'home/TIPO_PROYECTO/tipoproy_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TIPO_PROYECTO_UPDATE(request, pk):
    try:
        tipo_proyecto = TIPO_PROYECTO.objects.get(id=pk)
        if request.method == 'POST':
            form = formTIPO_PROYECTO(request.POST, instance=tipo_proyecto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tipo de proyecto actualizado correctamente')
                return redirect('/tipoproy_listall/')
        form = formTIPO_PROYECTO(instance=tipo_proyecto)
        ctx = {
            'form': form
        }
        return render(request, 'home/TIPO_PROYECTO/tipoproy_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PERMISO_LISTALL(request):
    try:
        object_list = PERMISO.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/PERMISO/permiso_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PERMISO_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formPERMISO(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Permiso guardado correctamente')
                return redirect('/permiso_listall/')
        form = formPERMISO()
        ctx = {
            'form': form
        }
        return render(request, 'home/PERMISO/permiso_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PERMISO_UPDATE(request, pk):
    try:
        permiso = PERMISO.objects.get(id=pk)
        if request.method == 'POST':
            form = formPERMISO(request.POST, instance=permiso)
            if form.is_valid():
                form.save()
                messages.success(request, 'Permiso actualizado correctamente')
                return redirect('/permiso_listall/')
        form = formPERMISO(instance=permiso)
        ctx = {
            'form': form
        }
        return render(request, 'home/PERMISO/permiso_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PERMISO_ROL_LISTALL(request):
    try:
        object_list = PERMISO_ROL.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/PERMISO_ROL/permisorol_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PERMISO_ROL_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formPERMISO_ROL(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Permiso de rol guardado correctamente')
                return redirect('/permisorol_listall/')
        form = formPERMISO_ROL()
        ctx = {
            'form': form
        }
        return render(request, 'home/PERMISO_ROL/permisorol_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PERMISO_ROL_UPDATE(request, pk):
    try:
        permiso_rol = PERMISO_ROL.objects.get(id=pk)
        if request.method == 'POST':
            form = formPERMISO_ROL(request.POST, instance=permiso_rol)
            if form.is_valid():
                form.save()
                messages.success(request, 'Permiso de rol actualizado correctamente')
                return redirect('/permisorol_listall/')
        form = formPERMISO_ROL(instance=permiso_rol)
        ctx = {
            'form': form
        }
        return render(request, 'home/PERMISO_ROL/permisorol_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def USUARIO_ROL_LISTALL(request):
    try:
        object_list = USUARIO_ROL.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/USUARIO_ROL/usuariorol_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def USUARIO_ROL_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formUSUARIO_ROL(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuario rol guardado correctamente')
                return redirect('/usuariorol_listall/')
        form = formUSUARIO_ROL()
        ctx = {
            'form': form
        }
        return render(request, 'home/USUARIO_ROL/usuariorol_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def USUARIO_ROL_UPDATE(request, pk):
    try:
        usuario_rol = USUARIO_ROL.objects.get(id=pk)
        if request.method == 'POST':
            form = formUSUARIO_ROL(request.POST, instance=usuario_rol)
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuario rol actualizado correctamente')
                return redirect('/usuariorol_listall/')
        form = formUSUARIO_ROL(instance=usuario_rol)
        ctx = {
            'form': form
        }
        return render(request, 'home/USUARIO_ROL/usuariorol_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CLIENTE_LISTALL(request):
    try:
        object_list = CLIENTE.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/CLIENTE/cliente_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CLIENTE_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formCLIENTE(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cliente guardado correctamente')
                return redirect('/cliente_listall/')
        form = formCLIENTE()
        ctx = {
            'form': form
        }
        return render(request, 'home/CLIENTE/cliente_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CLIENTE_UPDATE(request, pk):
    try:
        cliente = CLIENTE.objects.get(id=pk)
        if request.method == 'POST':
            form = formCLIENTE(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cliente actualizado correctamente')
                return redirect('/cliente_listall/')
        form = formCLIENTE(instance=cliente)
        ctx = {
            'form': form
        }
        return render(request, 'home/CLIENTE/cliente_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CONTACTO_CLIENTE_LISTALL(request):
    try:
        object_list = CONTACTO_CLIENTE.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/CONTACTO_CLIENTE/contactocli_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CONTACTO_CLIENTE_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formCONTACTO_CLIENTE(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contacto de cliente guardado correctamente')
                return redirect('/contactocli_listall/')
        form = formCONTACTO_CLIENTE()
        ctx = {
            'form': form
        }
        return render(request, 'home/CONTACTO_CLIENTE/contactocli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CONTACTO_CLIENTE_UPDATE(request, pk):
    try:
        contacto_cliente = CONTACTO_CLIENTE.objects.get(id=pk)
        if request.method == 'POST':
            form = formCONTACTO_CLIENTE(request.POST, instance=contacto_cliente)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contacto de cliente actualizado correctamente')
                return redirect('/contactocli_listall/')
        form = formCONTACTO_CLIENTE(instance=contacto_cliente)
        ctx = {
            'form': form
        }
        return render(request, 'home/CONTACTO_CLIENTE/contactocli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def DIRECCION_CLIENTE_LISTALL(request):
    try:
        object_list = DIRECCION_CLIENTE.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/DIRECCION_CLIENTE/direccioncli_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def DIRECCION_CLIENTE_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formDIRECCION_CLIENTE(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Dirección de cliente guardada correctamente')
                return redirect('/direccioncli_listall/')
        form = formDIRECCION_CLIENTE()
        ctx = {
            'form': form
        }
        return render(request, 'home/DIRECCION_CLIENTE/direccioncli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def DIRECCION_CLIENTE_UPDATE(request, pk):
    try:
        direccion_cliente = DIRECCION_CLIENTE.objects.get(id=pk)
        if request.method == 'POST':
            form = formDIRECCION_CLIENTE(request.POST, instance=direccion_cliente)
            if form.is_valid():
                form.save()
                messages.success(request, 'Dirección de cliente actualizada correctamente')
                return redirect('/direccioncli_listall/')
        form = formDIRECCION_CLIENTE(instance=direccion_cliente)
        ctx = {
            'form': form
        }
        return render(request, 'home/DIRECCION_CLIENTE/direccioncli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PRODUCTO_LISTALL(request):
    try:
        object_list = PRODUCTO.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/PRODUCTO/producto_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PRODUCTO_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formPRODUCTO(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto guardado correctamente')
                return redirect('/producto_listall/')
        form = formPRODUCTO()
        ctx = {
            'form': form
        }
        return render(request, 'home/PRODUCTO/producto_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PRODUCTO_UPDATE(request, pk):
    try:
        producto = PRODUCTO.objects.get(id=pk)
        if request.method == 'POST':
            form = formPRODUCTO(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto actualizado correctamente')
                return redirect('/producto_listall/')
        form = formPRODUCTO(instance=producto)
        ctx = {
            'form': form
        }
        return render(request, 'home/PRODUCTO/producto_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def EMPLEADO_LISTALL(request):
    try:
        object_list = EMPLEADO.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/EMPLEADO/empleado_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def EMPLEADO_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formEMPLEADO(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empleado guardado correctamente')
                return redirect('/empleado_listall/')
        form = formEMPLEADO()
        ctx = {
            'form': form
        }
        return render(request, 'home/EMPLEADO/empleado_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def EMPLEADO_UPDATE(request, pk):
    try:
        empleado = EMPLEADO.objects.get(id=pk)
        if request.method == 'POST':
            form = formEMPLEADO(request.POST, instance=empleado)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empleado actualizado correctamente')
                return redirect('/empleado_listall/')
        form = formEMPLEADO(instance=empleado)
        ctx = {
            'form': form
        }
        return render(request, 'home/EMPLEADO/empleado_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CONTRATISTA_LISTALL(request):
    try:
        object_list = CONTRATISTA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/CONTRATISTA/contratista_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CONTRATISTA_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formCONTRATISTA(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contratista guardado correctamente')
                return redirect('/contratista_listall/')
        form = formCONTRATISTA()
        ctx = {
            'form': form
        }
        return render(request, 'home/CONTRATISTA/contratista_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def CONTRATISTA_UPDATE(request, pk):
    try:
        contratista = CONTRATISTA.objects.get(id=pk)
        if request.method == 'POST':
            form = formCONTRATISTA(request.POST, instance=contratista)
            if form.is_valid():
                form.save()
                messages.success(request, 'Contratista actualizado correctamente')
                return redirect('/contratista_listall/')
        form = formCONTRATISTA(instance=contratista)
        ctx = {
            'form': form
        }
        return render(request, 'home/CONTRATISTA/contratista_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def EMPLEADO_EXTERNO_LISTALL(request):
    try:
        object_list = EMPLEADO_CONTRATISTA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/EMPLEADO_CONTRATISTA/empleado_externo_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def EMPLEADO_EXTERNO_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formEMPLEADO_CONTRATISTA(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empleado externo guardado correctamente')
                return redirect('/empleado_externo_listall/')
        form = formEMPLEADO_CONTRATISTA()
        ctx = {
            'form': form
        }
        return render(request, 'home/EMPLEADO_CONTRATISTA/empleado_externo_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def EMPLEADO_EXTERNO_UPDATE(request, pk):
    try:
        empleado_externo = EMPLEADO_CONTRATISTA.objects.get(id=pk)
        if request.method == 'POST':
            form = formEMPLEADO_CONTRATISTA(request.POST, instance=empleado_externo)
            if form.is_valid():
                empleado = form.save(commit=False)
                empleado.EC_CUSUARIO_MODIFICADOR = request.user
                empleado.save()
                messages.success(request, 'Empleado externo actualizado correctamente')
                return redirect('/empleado_externo_listall/')
        else:
            # Asegúrate de que las fechas se carguen correctamente en el formulario
            initial_data = {
                'EC_FFECHA_CONTRATACION': empleado_externo.EC_FFECHA_CONTRATACION.strftime('%Y-%m-%d') if empleado_externo.EC_FFECHA_CONTRATACION else None,
                'EC_CFECHA_NACIMIENTO': empleado_externo.EC_CFECHA_NACIMIENTO.strftime('%Y-%m-%d') if empleado_externo.EC_CFECHA_NACIMIENTO else None,
            }
            form = formEMPLEADO_CONTRATISTA(instance=empleado_externo, initial=initial_data)
        
        ctx = {
            'form': form,
            'empleado_externo': empleado_externo
        }
        return render(request, 'home/EMPLEADO_CONTRATISTA/empleado_externo_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ETAPA_LISTALL(request):
    try:
        object_list = ETAPA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/ETAPA/etapa_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ETAPA_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formETAPA(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Etapa guardada correctamente')
                return redirect('/etapa_listall/')
        form = formETAPA()
        ctx = {
            'form': form
        }
        return render(request, 'home/ETAPA/etapa_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ETAPA_UPDATE(request, pk):
    try:
        etapa = ETAPA.objects.get(id=pk)
        if request.method == 'POST':
            form = formETAPA(request.POST, instance=etapa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Etapa actualizada correctamente')
                return redirect('/etapa_listall/')
        form = formETAPA(instance=etapa)
        ctx = {
            'form': form
        }
        return render(request, 'home/ETAPA/etapa_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROYECTO_CLIENTE_LISTALL(request):
    try:
        object_list = PROYECTO_CLIENTE.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/PROYECTO_CLIENTE/proycli_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROYECTO_CLIENTE_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formPROYECTO_CLIENTE(request.POST)
            if form.is_valid():
                proyecto = form.save(commit=False)
                proyecto.PC_CUSUARIO_CREADOR = request.user
                proyecto.save()
                messages.success(request, 'Proyecto de cliente guardado correctamente')
                return redirect('/proycli_listall/')
        form = formPROYECTO_CLIENTE()
        ctx = {
            'form': form
        }
        return render(request, 'home/PROYECTO_CLIENTE/proycli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROYECTO_CLIENTE_UPDATE(request, pk, page):
    try:
        proyecto = PROYECTO_CLIENTE.objects.get(id=pk)
        if request.method == 'POST':
            form = formPROYECTO_CLIENTE(request.POST, instance=proyecto)
            if form.is_valid():
                proyecto = form.save(commit=False)
                proyecto.PC_CUSUARIO_MODIFICADOR = request.user
                proyecto.save()
                messages.success(request, 'Proyecto de cliente actualizado correctamente')
                if page == 1:
                    return redirect('/proycli_listone/'+str(proyecto.id)+'/')
                else:
                    return redirect('/proycli_listall/')
        else:
            # Convertir las fechas a formato de cadena para el formulario
            proyecto.PC_FFECHA_INICIO = proyecto.PC_FFECHA_INICIO.strftime('%Y-%m-%d') if proyecto.PC_FFECHA_INICIO else None
            proyecto.PC_FFECHA_FIN_ESTIMADA = proyecto.PC_FFECHA_FIN_ESTIMADA.strftime('%Y-%m-%d') if proyecto.PC_FFECHA_FIN_ESTIMADA else None
            proyecto.PC_FFECHA_FIN_REAL = proyecto.PC_FFECHA_FIN_REAL.strftime('%Y-%m-%d') if proyecto.PC_FFECHA_FIN_REAL else None
            form = formPROYECTO_CLIENTE(instance=proyecto)
        ctx = {
            'form': form
        }
        return render(request, 'home/PROYECTO_CLIENTE/proycli_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def PROYECTO_CLIENTE_LISTONE(request, pk):
    try:
        proyecto = PROYECTO_CLIENTE.objects.get(id=pk)
        tareas_general = TAREA_GENERAL.objects.filter(TG_PROYECTO_CLIENTE=proyecto)
        tareas_ingenieria = TAREA_INGENIERIA.objects.filter(TI_PROYECTO_CLIENTE=proyecto)
        tareas_financiera = TAREA_FINANCIERA.objects.filter(TF_PROYECTO_CLIENTE=proyecto)
        
        dependencias_general = TAREA_GENERAL_DEPENDENCIA.objects.filter(TD_TAREA_SUCESORA__in=tareas_general)
        dependencias_ingenieria = TAREA_INGENIERIA_DEPENDENCIA.objects.filter(TD_TAREA_SUCESORA__in=tareas_ingenieria)
        dependencias_financiera = TAREA_FINANCIERA_DEPENDENCIA.objects.filter(TD_TAREA_SUCESORA__in=tareas_financiera)        
        
        asignacion_empleado_general = ASIGNACION_EMPLEADO_TAREA_GENERAL.objects.filter(AE_TAREA__in=tareas_general)
        asignacion_empleado_ingenieria = ASIGNACION_EMPLEADO_TAREA_INGENIERIA.objects.filter(AE_TAREA__in=tareas_ingenieria)
        asignacion_empleado_financiera = ASIGNACION_EMPLEADO_TAREA_FINANCIERA.objects.filter(AE_TAREA__in=tareas_financiera)
        
        asignacion_empleado_recurso_general = ASIGNACION_RECURSO_TAREA_GENERAL.objects.filter(ART_TAREA__in=tareas_general)
        asignacion_empleado_recurso_ingenieria = ASIGNACION_RECURSO_TAREA_INGENIERIA.objects.filter(ART_TAREA__in=tareas_ingenieria)
        asignacion_empleado_recurso_financiera = ASIGNACION_RECURSO_TAREA_FINANCIERA.objects.filter(ART_TAREA__in=tareas_financiera)
        
        asignacion_contratista_general = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL.objects.filter(AEC_TAREA__in=tareas_general)
        asignacion_contratista_ingenieria = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA.objects.filter(AEC_TAREA__in=tareas_ingenieria)
        asignacion_contratista_financiera = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA.objects.filter(AEC_TAREA__in=tareas_financiera)
        
        costo_real_proyecto = 0
        horas_reales_proyecto = 0

        for tarea in tareas_general:
            tarea.TG_NPROGRESO = int(round(float(tarea.TG_NPROGRESO)))
            if tarea.TG_NPROGRESO == 100 and tarea.TG_NDURACION_REAL is not None and tarea.TG_NDURACION_REAL > 0:                
                    horas_reales_proyecto += tarea.TG_NDURACION_REAL    

                    if not (asignacion_empleado_general.filter(AE_TAREA=tarea).exists() or
                            asignacion_empleado_recurso_general.filter(ART_TAREA=tarea).exists() or
                            asignacion_contratista_general.filter(AEC_TAREA=tarea).exists()):
                        costo_real_proyecto +=  tarea.TG_NPRESUPUESTO

                    for asignacion in asignacion_empleado_general:
                        if asignacion.AE_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.AE_COSTO_TOTAL
                    for asignacion in asignacion_empleado_recurso_general:
                        if asignacion.ART_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.ART_COSTO_TOTAL
                    for asignacion in asignacion_contratista_general:
                        if asignacion.AEC_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.AEC_COSTO_TOTAL
        for tarea in tareas_ingenieria:
            tarea.TI_NPROGRESO = int(round(float(tarea.TI_NPROGRESO)))
            if tarea.TI_NPROGRESO == 100 and tarea.TI_NDURACION_REAL is not None and tarea.TI_NDURACION_REAL > 0:
                    
                    horas_reales_proyecto += tarea.TI_NDURACION_REAL
                    
                    if not (asignacion_empleado_ingenieria.filter(AE_TAREA=tarea).exists() or
                            asignacion_empleado_recurso_ingenieria.filter(ART_TAREA=tarea).exists() or
                            asignacion_contratista_ingenieria.filter(AEC_TAREA=tarea).exists()):
                        costo_real_proyecto +=  tarea.TI_NPRESUPUESTO

                    for asignacion in asignacion_empleado_ingenieria:
                        if asignacion.AE_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.AE_COSTO_TOTAL
                    for asignacion in asignacion_empleado_recurso_ingenieria:
                        if asignacion.ART_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.ART_COSTO_TOTAL
                    for asignacion in asignacion_contratista_ingenieria:
                        if asignacion.AEC_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.AEC_COSTO_TOTAL
        for tarea in tareas_financiera:
            tarea.TF_NPROGRESO = int(round(float(tarea.TF_NPROGRESO)))
            if tarea.TF_NPROGRESO == 100 and tarea.TF_NDURACION_REAL is not None and tarea.TF_NDURACION_REAL > 0:
                    
                    horas_reales_proyecto += tarea.TF_NDURACION_REAL
                    # Si la tarea no tiene asignaciones, se suma este valor
                    if not (asignacion_empleado_financiera.filter(AE_TAREA=tarea).exists() or
                            asignacion_empleado_recurso_financiera.filter(ART_TAREA=tarea).exists() or
                            asignacion_contratista_financiera.filter(AEC_TAREA=tarea).exists()):
                        costo_real_proyecto +=  tarea.TF_NMONTO                    

                    for asignacion in asignacion_empleado_financiera:
                        if asignacion.AE_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.AE_COSTO_TOTAL
                    for asignacion in asignacion_empleado_recurso_financiera:
                        if asignacion.ART_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.ART_COSTO_TOTAL
                    for asignacion in asignacion_contratista_financiera:
                        if asignacion.AEC_TAREA == tarea:                            
                            costo_real_proyecto +=  asignacion.AEC_COSTO_TOTAL
        if horas_reales_proyecto != proyecto.PC_NHORAS_REALES:
            print('horas_reales_proyecto', horas_reales_proyecto)
            print('proyecto.PC_NHORAS_REALES', proyecto.PC_NHORAS_REALES)
            proyecto.PC_NHORAS_REALES = horas_reales_proyecto
            proyecto.save()
        if costo_real_proyecto != proyecto.PC_NCOSTO_REAL:
            print('costo_real_proyecto', costo_real_proyecto)
            print('proyecto.PC_NCOSTO_REAL', proyecto.PC_NCOSTO_REAL)
            proyecto.PC_NCOSTO_REAL = costo_real_proyecto
            proyecto.save()
        max_costo = max(proyecto.PC_NCOSTO_REAL, proyecto.PC_NCOSTO_ESTIMADO)
        ctx = {
            'proyecto': proyecto,
            'tareas_general': tareas_general,
            'tareas_ingenieria': tareas_ingenieria,
            'tareas_financiera': tareas_financiera,
            'dependencias_general': dependencias_general,
            'dependencias_ingenieria': dependencias_ingenieria,
            'dependencias_financiera': dependencias_financiera,
            'costo_real_proyecto': costo_real_proyecto,
            'horas_reales_proyecto': horas_reales_proyecto,
            'max_costo': max_costo
        }
        return render(request, 'home/PROYECTO_CLIENTE/proycli_listone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')
#--------------------------------------
#----------------TAREAS----------------
#--------------------------------------

# ----------TAREA GENERAL--------------

def TAREA_GENERAL_LISTALL(request):
    try:
        tareas_generales = TAREA_GENERAL.objects.all()
        ctx = {
            'tareas_generales': tareas_generales
        }
        return render(request, 'home/TAREA/GENERAL/tarea_general_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TAREA_GENERAL_ADDONE(request, page):
    try:
        form = formTAREA_GENERAL()
        form_asignacion_empleado = formASIGNACION_EMPLEADO_TAREA_GENERAL()
        form_asignacion_contratista = formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL()
        form_asignacion_recurso = formASIGNACION_RECURSO_TAREA_GENERAL()

        if request.method == 'POST':
            form = formTAREA_GENERAL(request.POST)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.TG_CUSUARIO_CREADOR = request.user                                                
                tarea.save()

                # Manejar asignaciones múltiples
                empleados_ids = request.POST.getlist('empleados')
                contratistas_ids = request.POST.getlist('contratistas')                
                recursos_json = request.POST.get('recursos_json')

                # Asignar empleados
                for empleado_id in empleados_ids:
                    id_emp = EMPLEADO.objects.get(id=empleado_id)
                    asignacion = ASIGNACION_EMPLEADO_TAREA_GENERAL(
                        AE_TAREA=tarea,
                        AE_EMPLEADO=id_emp,
                        AE_CESTADO = 'ASIGNADO',
                        AE_CUSUARIO_CREADOR = request.user,
                        AE_FFECHA_ASIGNACION=tarea.TG_FFECHA_INICIO,  
                        AE_FFECHA_FINALIZACION=tarea.TG_FFECHA_FIN_ESTIMADA                      
                    )
                    asignacion.save()

                # Asignar contratistas
                for contratista_id in contratistas_ids:
                    id_emp = EMPLEADO_CONTRATISTA.objects.get(id=contratista_id)
                    asignacion = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL(
                        AEC_TAREA=tarea,
                        AEC_EMPLEADO=id_emp,
                        AEC_CESTADO = 'ASIGNADO',
                        AEC_FFECHA_ASIGNACION=tarea.TG_FFECHA_INICIO,
                        AEC_FFECHA_FINALIZACION=tarea.TG_FFECHA_FIN_ESTIMADA,
                        AEC_CUSUARIO_CREADOR=request.user
                    )
                    asignacion.save()

                # Procesar recursos                
                if recursos_json:
                    recursos = json.loads(recursos_json)
                    for recurso in recursos:
                        id_rec = PRODUCTO.objects.get(id=recurso['id'])
                        asignacion = ASIGNACION_RECURSO_TAREA_GENERAL(
                            ART_TAREA=tarea,
                            ART_PRODUCTO=id_rec,
                            ART_FFECHA_ASIGNACION=tarea.TG_FFECHA_INICIO,
                            ART_CUSUARIO_CREADOR=request.user,
                            ART_CANTIDAD=int(float(recurso['cantidad'])),
                            ART_COSTO_UNITARIO=int(float(recurso['costo'])),
                            ART_COSTO_TOTAL = int(float(recurso['costo'])) * int(float(recurso['cantidad']))
                        )
                        asignacion.save()

                messages.success(request, 'Tarea general guardada correctamente con las asignaciones seleccionadas')
                if page == 1:
                    return redirect('/proycli_listone/'+str(tarea.TG_PROYECTO_CLIENTE.id)+'/')
                else:
                    return redirect('/tarea_general_listall/')
            else:
                messages.error(request, 'Por favor, corrija los errores en el formulario.')
        
        ctx = {
            'form': form,
            'form_asignacion_empleado': form_asignacion_empleado,
            'form_asignacion_contratista': form_asignacion_contratista,
            'form_asignacion_recurso': form_asignacion_recurso
        }
        return render(request, 'home/TAREA/GENERAL/tarea_general_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_GENERAL_UPDATE(request, pk, page):
    try:
        tarea = TAREA_GENERAL.objects.get(id=pk)
        if request.method == 'POST':
            form = formTAREA_GENERAL(request.POST, instance=tarea)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.TG_CUSUARIO_MODIFICADOR = request.user
                tarea.save()
                messages.success(request, 'Tarea general actualizada correctamente')
                if page == 1:
                    return redirect('/proycli_listone/'+str(tarea.TG_PROYECTO_CLIENTE.id)+'/')
                else:
                    return redirect('/tarea_general_listall/')
        else:
            # Asegúrate de que las fechas se carguen correctamente en el formulario
            initial_data = {
                'TG_FFECHA_INICIO': tarea.TG_FFECHA_INICIO.strftime('%Y-%m-%d') if tarea.TG_FFECHA_INICIO else None,
                'TG_FFECHA_FIN_ESTIMADA': tarea.TG_FFECHA_FIN_ESTIMADA.strftime('%Y-%m-%d') if tarea.TG_FFECHA_FIN_ESTIMADA else None,
                'TG_FFECHA_FIN_REAL': tarea.TG_FFECHA_FIN_REAL.strftime('%Y-%m-%d') if tarea.TG_FFECHA_FIN_REAL else None
            }
            form = formTAREA_GENERAL(instance=tarea, initial=initial_data)
        
        ctx = {
            'form': form,
            'tarea': tarea
        }
        return render(request, 'home/TAREA/GENERAL/tarea_general_update.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TAREA_GENERAL_UPDATE_ASIGNACIONES(request, pk, page):
    try:
        tarea = TAREA_GENERAL.objects.get(id=pk)
        form_asignacion_empleado = formASIGNACION_EMPLEADO_TAREA_GENERAL()
        form_asignacion_contratista = formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL()
        form_asignacion_recurso = formASIGNACION_RECURSO_TAREA_GENERAL()

        # Cargar asignaciones existentes
        empleados_asignados = ASIGNACION_EMPLEADO_TAREA_GENERAL.objects.filter(AE_TAREA=tarea)
        contratistas_asignados = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL.objects.filter(AEC_TAREA=tarea)
        recursos_asignados = ASIGNACION_RECURSO_TAREA_GENERAL.objects.filter(ART_TAREA=tarea)

        if request.method == 'POST':
            # Manejar asignaciones múltiples
            empleados_ids = request.POST.getlist('empleados')
            contratistas_ids = request.POST.getlist('contratistas')                
            recursos_json = request.POST.get('recursos_json')

            # Eliminar asignaciones existentes
            ASIGNACION_EMPLEADO_TAREA_GENERAL.objects.filter(AE_TAREA=tarea).delete()
            ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL.objects.filter(AEC_TAREA=tarea).delete()
            ASIGNACION_RECURSO_TAREA_GENERAL.objects.filter(ART_TAREA=tarea).delete()

            # Asignar empleados
            for empleado_id in empleados_ids:
                id_emp = EMPLEADO.objects.get(id=empleado_id)
                asignacion = ASIGNACION_EMPLEADO_TAREA_GENERAL(
                    AE_TAREA=tarea,
                    AE_EMPLEADO=id_emp,
                    AE_CESTADO = 'ASIGNADO',
                    AE_CUSUARIO_CREADOR = request.user,
                    AE_FFECHA_ASIGNACION=tarea.TG_FFECHA_INICIO,  
                    AE_FFECHA_FINALIZACION=tarea.TG_FFECHA_FIN_ESTIMADA                      
                )
                asignacion.save()

            # Asignar contratistas
            for contratista_id in contratistas_ids:
                id_emp = EMPLEADO_CONTRATISTA.objects.get(id=contratista_id)
                asignacion = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL(
                    AEC_TAREA=tarea,
                    AEC_EMPLEADO=id_emp,
                    AEC_CESTADO = 'ASIGNADO',
                    AEC_FFECHA_ASIGNACION=tarea.TG_FFECHA_INICIO,
                    AEC_FFECHA_FINALIZACION=tarea.TG_FFECHA_FIN_ESTIMADA,
                    AEC_CUSUARIO_CREADOR=request.user
                )
                asignacion.save()

            # Procesar recursos                
            if recursos_json:
                recursos = json.loads(recursos_json)
                for recurso in recursos:
                    id_rec = PRODUCTO.objects.get(id=recurso['id'])
                    asignacion = ASIGNACION_RECURSO_TAREA_GENERAL(
                        ART_TAREA=tarea,
                        ART_PRODUCTO=id_rec,
                        ART_FFECHA_ASIGNACION=tarea.TG_FFECHA_INICIO,
                        ART_CUSUARIO_CREADOR=request.user,
                        ART_CANTIDAD=int(float(recurso['cantidad'])),   
                        ART_COSTO_UNITARIO=int(float(recurso['costo'])),
                        ART_COSTO_TOTAL = int(float(recurso['costo'])) * int(float(recurso['cantidad']))
                    )
                    asignacion.save()

            messages.success(request, 'Asignaciones de la tarea general actualizadas correctamente')
            if page == 1:
                return redirect('/proycli_listone/'+str(tarea.TG_PROYECTO_CLIENTE.id)+'/')
            else:
                return redirect('/tarea_general_listall/')
        
        # Preparar datos para mostrar en el template
        empleados_asignados_ids = list(empleados_asignados.values_list('AE_EMPLEADO__id', flat=True))
        contratistas_asignados_ids = list(contratistas_asignados.values_list('AEC_EMPLEADO__id', flat=True))
        recursos_asignados_data = [
            {
                'id': str(recurso.ART_PRODUCTO.id),
                'nombre': recurso.ART_PRODUCTO.PR_CNOMBRE,
                'cantidad': str(recurso.ART_CANTIDAD),
                'costo': str(recurso.ART_COSTO_UNITARIO)
            } for recurso in recursos_asignados
        ]
        
        ctx = {
            'form_asignacion_empleado': form_asignacion_empleado,
            'form_asignacion_contratista': form_asignacion_contratista,
            'form_asignacion_recurso': form_asignacion_recurso,
            'tarea': tarea,
            'empleados_asignados_ids': empleados_asignados_ids,
            'contratistas_asignados_ids': contratistas_asignados_ids,
            'recursos_asignados_data': json.dumps(recursos_asignados_data),
            'page': page
        }
        return render(request, 'home/TAREA/GENERAL/tarea_general_update_asignaciones.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_GENERAL_LISTONE(request, pk, page):
    try:
        tarea = TAREA_GENERAL.objects.get(id=pk)
        empleados_asignados = ASIGNACION_EMPLEADO_TAREA_GENERAL.objects.filter(AE_TAREA=tarea)
        contratistas_asignados = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL.objects.filter(AEC_TAREA=tarea)
        recursos_asignados = ASIGNACION_RECURSO_TAREA_GENERAL.objects.filter(ART_TAREA=tarea)
        tarea.TG_NPROGRESO = int(round(float(tarea.TG_NPROGRESO)))
        ctx = {
            'tarea': tarea,
            'page': page,
            'empleados_asignados': empleados_asignados,
            'contratistas_asignados': contratistas_asignados,
            'recursos_asignados': recursos_asignados
        }
        return render(request, 'home/TAREA/GENERAL/tarea_general_listone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_GENERAL_DEPENDENCIA_ADDONE(request, pk):
    try:
        tarea = TAREA_GENERAL.objects.get(id=pk)
        proyecto_actual = tarea.TG_PROYECTO_CLIENTE
        dependencia_existente = TAREA_GENERAL_DEPENDENCIA.objects.filter(TD_TAREA_PREDECESORA=tarea)
        if request.method == 'POST':
            form = formTAREA_GENERAL_DEPENDENCIA(request.POST)
            if form.is_valid():
                dependencia = form.save(commit=False)
                dependencia.TD_TAREA_PREDECESORA = tarea
                dependencia.save()
                messages.success(request, 'Dependencia agregada correctamente')
                return redirect('proycli_listone', pk=proyecto_actual.id)
        else:
            form = formTAREA_GENERAL_DEPENDENCIA()
        
        # Filtrar las tareas generales del proyecto actual
        tareas_sucesoras = TAREA_GENERAL.objects.filter(TG_PROYECTO_CLIENTE=proyecto_actual).exclude(id=tarea.id)
        form.fields['TD_TAREA_SUCESORA'].queryset = tareas_sucesoras
        
        ctx = {
            'form': form,
            'tarea': tarea,
            'dependencia_existente': dependencia_existente  
        }
        return render(request, 'home/TAREA/GENERAL/tarea_general_dependencia_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

# ----------TAREA INGENIERIA--------------

def TAREA_INGENIERIA_LISTALL(request):
    try:
        tareas_ingenieria = TAREA_INGENIERIA.objects.all()
        ctx = {
            'tareas_ingenieria': tareas_ingenieria
        }
        return render(request, 'home/TAREA/INGENIERIA/tarea_ingenieria_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TAREA_INGENIERIA_ADDONE(request, page):
    try:
        form = formTAREA_INGENIERIA()
        form_asignacion_empleado = formASIGNACION_EMPLEADO_TAREA_INGENIERIA()
        form_asignacion_contratista = formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA()
        form_asignacion_recurso = formASIGNACION_RECURSO_TAREA_INGENIERIA()

        if request.method == 'POST':
            form = formTAREA_INGENIERIA(request.POST)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.TI_CUSUARIO_CREADOR = request.user                                                
                tarea.save()

                # Manejar asignaciones múltiples
                empleados_ids = request.POST.getlist('empleados')
                contratistas_ids = request.POST.getlist('contratistas')                
                recursos_json = request.POST.get('recursos_json')

                # Asignar empleados
                for empleado_id in empleados_ids:
                    id_emp = EMPLEADO.objects.get(id=empleado_id)
                    asignacion = ASIGNACION_EMPLEADO_TAREA_INGENIERIA(
                        AE_TAREA=tarea,
                        AE_EMPLEADO=id_emp,
                        AE_CESTADO = 'ASIGNADO',
                        AE_CUSUARIO_CREADOR = request.user,
                        AE_FFECHA_ASIGNACION=tarea.TI_FFECHA_INICIO,  
                        AE_FFECHA_FINALIZACION=tarea.TI_FFECHA_FIN_ESTIMADA                      
                    )
                    asignacion.save()

                # Asignar contratistas
                for contratista_id in contratistas_ids:
                    id_emp = EMPLEADO_CONTRATISTA.objects.get(id=contratista_id)
                    asignacion = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA(
                        AEC_TAREA=tarea,
                        AEC_EMPLEADO=id_emp,
                        AEC_CESTADO = 'ASIGNADO',
                        AEC_FFECHA_ASIGNACION=tarea.TI_FFECHA_INICIO,
                        AEC_FFECHA_FINALIZACION=tarea.TI_FFECHA_FIN_ESTIMADA,
                        AEC_CUSUARIO_CREADOR=request.user
                    )
                    asignacion.save()

                # Procesar recursos                
                if recursos_json:
                    recursos = json.loads(recursos_json)
                    for recurso in recursos:
                        id_rec = PRODUCTO.objects.get(id=recurso['id'])
                        asignacion = ASIGNACION_RECURSO_TAREA_INGENIERIA(
                            ART_TAREA=tarea,
                            ART_PRODUCTO=id_rec,
                            ART_FFECHA_ASIGNACION=tarea.TI_FFECHA_INICIO,
                            ART_CUSUARIO_CREADOR=request.user,
                            ART_CANTIDAD=int(recurso['cantidad']),
                            ART_COSTO_UNITARIO=int(recurso['costo']),
                            ART_COSTO_TOTAL = int(recurso['costo']) * int(recurso['cantidad'])
                        )
                        asignacion.save()

                messages.success(request, 'Tarea de ingeniería guardada correctamente con las asignaciones seleccionadas')
                if page == 1:
                    return redirect('/proycli_listone/'+str(tarea.TI_PROYECTO_CLIENTE.id)+'/')
                else:
                    return redirect('/tarea_ingenieria_listall/')
            else:
                messages.error(request, 'Por favor, corrija los errores en el formulario.')
        
        ctx = {
            'form': form,
            'form_asignacion_empleado': form_asignacion_empleado,
            'form_asignacion_contratista': form_asignacion_contratista,
            'form_asignacion_recurso': form_asignacion_recurso,
            'page': page
        }
        return render(request, 'home/TAREA/INGENIERIA/tarea_ingenieria_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_INGENIERIA_UPDATE(request, pk, page):
    try:
        tarea = TAREA_INGENIERIA.objects.get(id=pk)
        if request.method == 'POST':
            form = formTAREA_INGENIERIA(request.POST, instance=tarea)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.TI_CUSUARIO_MODIFICADOR = request.user
                tarea.save()
                messages.success(request, 'Tarea de ingeniería actualizada correctamente')
                if page == 1:
                    return redirect('/proycli_listone/'+str(tarea.TI_PROYECTO_CLIENTE.id)+'/')
                else:
                    return redirect('/tarea_ingenieria_listall/')
        else:
            initial_data = {
                'TI_FFECHA_INICIO': tarea.TI_FFECHA_INICIO.strftime('%Y-%m-%d') if tarea.TI_FFECHA_INICIO else None,
                'TI_FFECHA_FIN_ESTIMADA': tarea.TI_FFECHA_FIN_ESTIMADA.strftime('%Y-%m-%d') if tarea.TI_FFECHA_FIN_ESTIMADA else None,
            }
            form = formTAREA_INGENIERIA(instance=tarea, initial=initial_data)
        
        ctx = {
            'form': form,
            'tarea': tarea
        }
        return render(request, 'home/TAREA/INGENIERIA/tarea_ingenieria_update.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TAREA_INGENIERIA_UPDATE_ASIGNACIONES(request, pk, page):
    try:
        tarea = TAREA_INGENIERIA.objects.get(id=pk)
        form_asignacion_empleado = formASIGNACION_EMPLEADO_TAREA_INGENIERIA()
        form_asignacion_contratista = formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA()
        form_asignacion_recurso = formASIGNACION_RECURSO_TAREA_INGENIERIA()

        # Cargar asignaciones existentes
        empleados_asignados = ASIGNACION_EMPLEADO_TAREA_INGENIERIA.objects.filter(AE_TAREA=tarea)
        contratistas_asignados = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA.objects.filter(AEC_TAREA=tarea)
        recursos_asignados = ASIGNACION_RECURSO_TAREA_INGENIERIA.objects.filter(ART_TAREA=tarea)

        if request.method == 'POST':
            # Manejar asignaciones múltiples
            empleados_ids = request.POST.getlist('empleados')
            contratistas_ids = request.POST.getlist('contratistas')                
            recursos_json = request.POST.get('recursos_json')

            # Eliminar asignaciones existentes
            ASIGNACION_EMPLEADO_TAREA_INGENIERIA.objects.filter(AE_TAREA=tarea).delete()
            ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA.objects.filter(AEC_TAREA=tarea).delete()
            ASIGNACION_RECURSO_TAREA_INGENIERIA.objects.filter(ART_TAREA=tarea).delete()

            # Asignar empleados
            for empleado_id in empleados_ids:
                id_emp = EMPLEADO.objects.get(id=empleado_id)
                asignacion = ASIGNACION_EMPLEADO_TAREA_INGENIERIA(
                    AE_TAREA=tarea,
                    AE_EMPLEADO=id_emp,
                    AE_CESTADO = 'ASIGNADO',
                    AE_CUSUARIO_CREADOR = request.user,
                    AE_FFECHA_ASIGNACION=tarea.TI_FFECHA_INICIO,  
                    AE_FFECHA_FINALIZACION=tarea.TI_FFECHA_FIN_ESTIMADA                      
                )
                asignacion.save()

            # Asignar contratistas
            for contratista_id in contratistas_ids:
                id_emp = EMPLEADO_CONTRATISTA.objects.get(id=contratista_id)
                asignacion = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA(
                    AEC_TAREA=tarea,
                    AEC_EMPLEADO=id_emp,
                    AEC_CESTADO = 'ASIGNADO',
                    AEC_FFECHA_ASIGNACION=tarea.TI_FFECHA_INICIO,
                    AEC_FFECHA_FINALIZACION=tarea.TI_FFECHA_FIN_ESTIMADA,
                    AEC_CUSUARIO_CREADOR=request.user
                )
                asignacion.save()

            # Procesar recursos                
            if recursos_json:
                recursos = json.loads(recursos_json)
                for recurso in recursos:
                    id_rec = PRODUCTO.objects.get(id=recurso['id'])
                    asignacion = ASIGNACION_RECURSO_TAREA_INGENIERIA(
                        ART_TAREA=tarea,
                        ART_PRODUCTO=id_rec,
                        ART_FFECHA_ASIGNACION=tarea.TI_FFECHA_INICIO,
                        ART_CUSUARIO_CREADOR=request.user,
                        ART_CANTIDAD=int(float(recurso['cantidad'])),
                        ART_COSTO_UNITARIO=int(float(recurso['costo'])),
                        ART_COSTO_TOTAL = int(float(recurso['costo'])) * int(float(recurso['cantidad']))
                    )
                    asignacion.save()

            messages.success(request, 'Asignaciones de la tarea de ingeniería actualizadas correctamente')
            if page == 1:
                return redirect('/proycli_listone/'+str(tarea.TI_PROYECTO_CLIENTE.id)+'/')
            else:
                return redirect('/tarea_ingenieria_listall/')
        
        # Preparar datos para mostrar en el template
        empleados_asignados_ids = list(empleados_asignados.values_list('AE_EMPLEADO__id', flat=True))
        contratistas_asignados_ids = list(contratistas_asignados.values_list('AEC_EMPLEADO__id', flat=True))
        recursos_asignados_data = [
            {
                'id': str(recurso.ART_PRODUCTO.id),
                'nombre': recurso.ART_PRODUCTO.PR_CNOMBRE,
                'cantidad': str(recurso.ART_CANTIDAD),
                'costo': str(recurso.ART_COSTO_UNITARIO)
            } for recurso in recursos_asignados
        ]
        
        ctx = {
            'form_asignacion_empleado': form_asignacion_empleado,
            'form_asignacion_contratista': form_asignacion_contratista,
            'form_asignacion_recurso': form_asignacion_recurso,
            'tarea': tarea,
            'empleados_asignados_ids': empleados_asignados_ids,
            'contratistas_asignados_ids': contratistas_asignados_ids,
            'recursos_asignados_data': json.dumps(recursos_asignados_data),
            'page': page
        }
        return render(request, 'home/TAREA/INGENIERIA/tarea_ingenieria_update_asignaciones.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_INGENIERIA_LISTONE(request, pk, page):
    try:
        tarea = TAREA_INGENIERIA.objects.get(id=pk)
        empleados_asignados = ASIGNACION_EMPLEADO_TAREA_INGENIERIA.objects.filter(AE_TAREA=tarea)
        contratistas_asignados = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA.objects.filter(AEC_TAREA=tarea)
        recursos_asignados = ASIGNACION_RECURSO_TAREA_INGENIERIA.objects.filter(ART_TAREA=tarea)
        tarea.TI_NPROGRESO = int(round(float(tarea.TI_NPROGRESO)))
        ctx = {
            'tarea': tarea,
            'page': page,
            'empleados_asignados': empleados_asignados,
            'contratistas_asignados': contratistas_asignados,
            'recursos_asignados': recursos_asignados
        }
        return render(request, 'home/TAREA/INGENIERIA/tarea_ingenieria_listone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_INGENIERIA_DEPENDENCIA_ADDONE(request, pk):
    try:
        tarea = TAREA_INGENIERIA.objects.get(id=pk)
        proyecto_actual = tarea.TI_PROYECTO_CLIENTE
        dependencia_existente = TAREA_INGENIERIA_DEPENDENCIA.objects.filter(TD_TAREA_PREDECESORA=tarea)
        if request.method == 'POST':
            form = formTAREA_INGENIERIA_DEPENDENCIA(request.POST)
            if form.is_valid():
                dependencia = form.save(commit=False)
                dependencia.TD_TAREA_PREDECESORA = tarea
                dependencia.save()
                messages.success(request, 'Dependencia agregada correctamente')
                return redirect('proycli_listone', pk=proyecto_actual.id)
        else:
            form = formTAREA_INGENIERIA_DEPENDENCIA()
        
        # Filtrar las tareas de ingeniería del proyecto actual
        tareas_sucesoras = TAREA_INGENIERIA.objects.filter(TI_PROYECTO_CLIENTE=proyecto_actual).exclude(id=tarea.id)
        form.fields['TD_TAREA_SUCESORA'].queryset = tareas_sucesoras
        
        ctx = {
            'form': form,
            'tarea': tarea,
            'dependencia_existente': dependencia_existente
        }
        return render(request, 'home/TAREA/INGENIERIA/tarea_ingenieria_dependencia_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

# ----------TAREA FINANCIERA--------------

def TAREA_FINANCIERA_LISTALL(request):
    try:
        tareas_financiera = TAREA_FINANCIERA.objects.all()
        ctx = {
            'tareas_financiera': tareas_financiera
        }
        return render(request, 'home/TAREA/FINANCIERA/tarea_financiera_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def TAREA_FINANCIERA_ADDONE(request, page):
    try:
        form = formTAREA_FINANCIERA()
        form_asignacion_empleado = formASIGNACION_EMPLEADO_TAREA_FINANCIERA()
        form_asignacion_contratista = formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA()
        form_asignacion_recurso = formASIGNACION_RECURSO_TAREA_FINANCIERA()        
        if request.method == 'POST':
            form = formTAREA_FINANCIERA(request.POST)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.TF_CUSUARIO_CREADOR = request.user
                
                # Aplicar lógica de fechas automáticamente
                fecha_inicio = form.cleaned_data.get('TF_FFECHA_INICIO')
                fecha_fin_estimada = form.cleaned_data.get('TF_FFECHA_FIN_ESTIMADA')
                
                if fecha_inicio and not fecha_fin_estimada:
                    tarea.TF_FFECHA_FIN_ESTIMADA = fecha_inicio
                elif fecha_fin_estimada and not fecha_inicio:
                    tarea.TF_FFECHA_INICIO = fecha_fin_estimada
                
                tarea.save()

                # Manejar asignaciones múltiples
                empleados_ids = request.POST.getlist('empleados')
                contratistas_ids = request.POST.getlist('contratistas')                
                recursos_json = request.POST.get('recursos_json')

                # Asignar empleados
                for empleado_id in empleados_ids:
                    id_emp = EMPLEADO.objects.get(id=empleado_id)
                    asignacion = ASIGNACION_EMPLEADO_TAREA_FINANCIERA(
                        AE_TAREA=tarea,
                        AE_EMPLEADO=id_emp,
                        AE_CESTADO = 'ASIGNADO',
                        AE_CUSUARIO_CREADOR = request.user,
                        AE_FFECHA_ASIGNACION=fecha_inicio,  
                        AE_FFECHA_FINALIZACION=fecha_fin_estimada                      
                    )
                    asignacion.save()

                # Asignar contratistas
                for contratista_id in contratistas_ids:
                    id_emp = EMPLEADO_CONTRATISTA.objects.get(id=contratista_id)
                    asignacion = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA(
                        AEC_TAREA=tarea,
                        AEC_EMPLEADO=id_emp,
                        AEC_CESTADO = 'ASIGNADO',
                        AEC_FFECHA_ASIGNACION=fecha_inicio,
                        AEC_FFECHA_FINALIZACION=fecha_fin_estimada,
                        AEC_CUSUARIO_CREADOR=request.user
                    )
                    asignacion.save()

                # Procesar recursos                
                if recursos_json:
                    recursos = json.loads(recursos_json)
                    for recurso in recursos:
                        id_rec = PRODUCTO.objects.get(id=recurso['id'])
                        asignacion = ASIGNACION_RECURSO_TAREA_FINANCIERA(
                            ART_TAREA=tarea,
                            ART_PRODUCTO=id_rec,
                            ART_FFECHA_ASIGNACION=fecha_inicio,
                            ART_CUSUARIO_CREADOR=request.user,
                            ART_CANTIDAD=int(recurso['cantidad']),
                            ART_COSTO_UNITARIO=int(recurso['costo']),
                            ART_COSTO_TOTAL = int(recurso['costo']) * int(recurso['cantidad'])
                        )
                        asignacion.save()
                
                messages.success(request, 'Tarea financiera guardada correctamente con las asignaciones seleccionadas')
                if page == 1:
                    return redirect('/proycli_listone/'+str(tarea.TF_PROYECTO_CLIENTE.id)+'/')
                else:
                    return redirect('/tarea_financiera_listall/')
            else:
                messages.error(request, 'Por favor, corrija los errores en el formulario.')
        
        ctx = {
            'form': form,
            'form_asignacion_empleado': form_asignacion_empleado,
            'form_asignacion_contratista': form_asignacion_contratista,
            'form_asignacion_recurso': form_asignacion_recurso,            
            'page': page
        }
        return render(request, 'home/TAREA/FINANCIERA/tarea_financiera_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_FINANCIERA_UPDATE(request, pk, page):
    try:
        tarea = TAREA_FINANCIERA.objects.get(id=pk)
        if request.method == 'POST':
            form = formTAREA_FINANCIERA(request.POST, instance=tarea)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.TF_CUSUARIO_MODIFICADOR = request.user
                
                # Aplicar lógica de fechas automáticamente
                fecha_inicio = form.cleaned_data.get('TF_FFECHA_INICIO')
                fecha_fin_estimada = form.cleaned_data.get('TF_FFECHA_FIN_ESTIMADA')
                
                if fecha_inicio and not fecha_fin_estimada:
                    tarea.TF_FFECHA_FIN_ESTIMADA = fecha_inicio
                elif fecha_fin_estimada and not fecha_inicio:
                    tarea.TF_FFECHA_INICIO = fecha_fin_estimada
                
                tarea.save()

                messages.success(request, 'Tarea financiera actualizada correctamente')
                if page == 1:
                    return redirect('/proycli_listone/'+str(tarea.TF_PROYECTO_CLIENTE.id)+'/')
                else:
                    return redirect('/tarea_financiera_listall/')
            else:
                messages.error(request, 'Por favor, corrija los errores en el formulario.')
        else:
            # Asegúrate de que las fechas se carguen correctamente en el formulario
            initial_data = {
                'TF_FFECHA_INICIO': tarea.TF_FFECHA_INICIO.strftime('%Y-%m-%d') if tarea.TF_FFECHA_INICIO else None,
                'TF_FFECHA_FIN_ESTIMADA': tarea.TF_FFECHA_FIN_ESTIMADA.strftime('%Y-%m-%d') if tarea.TF_FFECHA_FIN_ESTIMADA else None,
                'TF_FFECHA_FIN_REAL': tarea.TF_FFECHA_FIN_REAL.strftime('%Y-%m-%d') if tarea.TF_FFECHA_FIN_REAL else None
            }
            form = formTAREA_FINANCIERA(instance=tarea, initial=initial_data)
        
        ctx = {
            'form': form,
            'tarea': tarea,
            'page': page
        }
        return render(request, 'home/TAREA/FINANCIERA/tarea_financiera_update.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_FINANCIERA_UPDATE_ASIGNACIONES(request, pk, page):
    try:
        tarea = TAREA_FINANCIERA.objects.get(id=pk)
        form_asignacion_empleado = formASIGNACION_EMPLEADO_TAREA_FINANCIERA()
        form_asignacion_contratista = formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA()
        form_asignacion_recurso = formASIGNACION_RECURSO_TAREA_FINANCIERA()

        # Cargar asignaciones existentes
        empleados_asignados = ASIGNACION_EMPLEADO_TAREA_FINANCIERA.objects.filter(AE_TAREA=tarea)
        contratistas_asignados = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA.objects.filter(AEC_TAREA=tarea)
        recursos_asignados = ASIGNACION_RECURSO_TAREA_FINANCIERA.objects.filter(ART_TAREA=tarea)

        if request.method == 'POST':
            # Manejar asignaciones múltiples
            empleados_ids = request.POST.getlist('empleados')
            contratistas_ids = request.POST.getlist('contratistas')                
            recursos_json = request.POST.get('recursos_json')

            # Eliminar asignaciones existentes
            ASIGNACION_EMPLEADO_TAREA_FINANCIERA.objects.filter(AE_TAREA=tarea).delete()
            ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA.objects.filter(AEC_TAREA=tarea).delete()
            ASIGNACION_RECURSO_TAREA_FINANCIERA.objects.filter(ART_TAREA=tarea).delete()

            # Asignar empleados
            for empleado_id in empleados_ids:
                id_emp = EMPLEADO.objects.get(id=empleado_id)
                asignacion = ASIGNACION_EMPLEADO_TAREA_FINANCIERA(
                    AE_TAREA=tarea,
                    AE_EMPLEADO=id_emp,
                    AE_CESTADO = 'ASIGNADO',
                    AE_CUSUARIO_CREADOR = request.user,
                    AE_FFECHA_ASIGNACION=tarea.TF_FFECHA_INICIO,  
                    AE_FFECHA_FINALIZACION=tarea.TF_FFECHA_FIN_ESTIMADA                      
                )
                asignacion.save()

            # Asignar contratistas
            for contratista_id in contratistas_ids:
                id_emp = EMPLEADO_CONTRATISTA.objects.get(id=contratista_id)
                asignacion = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA(
                    AEC_TAREA=tarea,
                    AEC_EMPLEADO=id_emp,
                    AEC_CESTADO = 'ASIGNADO',
                    AEC_FFECHA_ASIGNACION=tarea.TF_FFECHA_INICIO,
                    AEC_FFECHA_FINALIZACION=tarea.TF_FFECHA_FIN_ESTIMADA,
                    AEC_CUSUARIO_CREADOR=request.user
                )
                asignacion.save()

            # Procesar recursos                
            if recursos_json:
                recursos = json.loads(recursos_json)
                for recurso in recursos:
                    id_rec = PRODUCTO.objects.get(id=recurso['id'])
                    asignacion = ASIGNACION_RECURSO_TAREA_FINANCIERA(
                        ART_TAREA=tarea,
                        ART_PRODUCTO=id_rec,
                        ART_FFECHA_ASIGNACION=tarea.TF_FFECHA_INICIO,
                        ART_CUSUARIO_CREADOR=request.user,
                        ART_CANTIDAD=int(float(recurso['cantidad'])),  # Convert to float first, then to int
                        ART_COSTO_UNITARIO=int(float(recurso['costo'])),  # Same here
                        ART_COSTO_TOTAL = int(float(recurso['costo'])) * int(float(recurso['cantidad']))
                    )
                    asignacion.save()

            messages.success(request, 'Asignaciones de la tarea financiera actualizadas correctamente')
            if page == 1:
                return redirect('/proycli_listone/'+str(tarea.TF_PROYECTO_CLIENTE.id)+'/')
            else:
                return redirect('/tarea_financiera_listall/')
        
        # Preparar datos para mostrar en el template
        empleados_asignados_ids = list(empleados_asignados.values_list('AE_EMPLEADO__id', flat=True))
        contratistas_asignados_ids = list(contratistas_asignados.values_list('AEC_EMPLEADO__id', flat=True))
        recursos_asignados_data = [
            {
                'id': str(recurso.ART_PRODUCTO.id),
                'nombre': recurso.ART_PRODUCTO.PR_CNOMBRE,
                'cantidad': str(recurso.ART_CANTIDAD),
                'costo': str(recurso.ART_COSTO_UNITARIO)
            } for recurso in recursos_asignados
        ]
        
        ctx = {
            'form_asignacion_empleado': form_asignacion_empleado,
            'form_asignacion_contratista': form_asignacion_contratista,
            'form_asignacion_recurso': form_asignacion_recurso,
            'tarea': tarea,
            'empleados_asignados_ids': empleados_asignados_ids,
            'contratistas_asignados_ids': contratistas_asignados_ids,
            'recursos_asignados_data': json.dumps(recursos_asignados_data),
            'page': page
        }
        return render(request, 'home/TAREA/FINANCIERA/tarea_financiera_update_asignaciones.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_FINANCIERA_LISTONE(request, pk, page):
    try:
        tarea = TAREA_FINANCIERA.objects.get(id=pk)
        empleados_asignados = ASIGNACION_EMPLEADO_TAREA_FINANCIERA.objects.filter(AE_TAREA=tarea)
        contratistas_asignados = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA.objects.filter(AEC_TAREA=tarea)
        recursos_asignados = ASIGNACION_RECURSO_TAREA_FINANCIERA.objects.filter(ART_TAREA=tarea)
        tarea.TF_NPROGRESO = int(round(float(tarea.TF_NPROGRESO)))
        ctx = {
            'tarea': tarea,
            'empleados_asignados': empleados_asignados,
            'contratistas_asignados': contratistas_asignados,
            'recursos_asignados': recursos_asignados,
            'page': page
        }
        return render(request, 'home/TAREA/FINANCIERA/tarea_financiera_listone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

def TAREA_FINANCIERA_DEPENDENCIA_ADDONE(request, pk):
    try:
        tarea = TAREA_FINANCIERA.objects.get(id=pk)
        proyecto_actual = tarea.TF_PROYECTO_CLIENTE
        dependencia_existente = TAREA_FINANCIERA_DEPENDENCIA.objects.filter(TD_TAREA_PREDECESORA=tarea)
        if request.method == 'POST':
            form = formTAREA_FINANCIERA_DEPENDENCIA(request.POST)
            if form.is_valid():
                dependencia = form.save(commit=False)
                dependencia.TD_TAREA_PREDECESORA = tarea
                dependencia.save()
                messages.success(request, 'Dependencia agregada correctamente')
                return redirect('proycli_listone', pk=proyecto_actual.id)
        else:
            form = formTAREA_FINANCIERA_DEPENDENCIA()
        
        # Filtrar las tareas financieras del proyecto actual
        tareas_sucesoras = TAREA_FINANCIERA.objects.filter(TF_PROYECTO_CLIENTE=proyecto_actual).exclude(id=tarea.id)
        form.fields['TD_TAREA_SUCESORA'].queryset = tareas_sucesoras
        
        ctx = {
            'form': form,
            'tarea': tarea,
            'dependencia_existente': dependencia_existente  
        }
        return render(request, 'home/TAREA/FINANCIERA/tarea_financiera_dependencia_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error: {str(e)}')
        return redirect('/')

# ----------TAREA UPDATE DATA--------------
def tarea_update_data(request, tipo_tarea, pk):
    if tipo_tarea == 'general':
        Tarea = TAREA_GENERAL
        AsignacionEmpleado = ASIGNACION_EMPLEADO_TAREA_GENERAL
        AsignacionContratista = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL
        AsignacionRecurso = ASIGNACION_RECURSO_TAREA_GENERAL
    elif tipo_tarea == 'ingenieria':
        Tarea = TAREA_INGENIERIA
        AsignacionEmpleado = ASIGNACION_EMPLEADO_TAREA_INGENIERIA
        AsignacionContratista = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA
        AsignacionRecurso = ASIGNACION_RECURSO_TAREA_INGENIERIA
    elif tipo_tarea == 'financiera':
        Tarea = TAREA_FINANCIERA
        AsignacionEmpleado = ASIGNACION_EMPLEADO_TAREA_FINANCIERA
        AsignacionContratista = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA
        AsignacionRecurso = ASIGNACION_RECURSO_TAREA_FINANCIERA
    else:
        return HttpResponseBadRequest("Tipo de tarea no válido")

    tarea = get_object_or_404(Tarea, id=pk)
    empleados_asignados = AsignacionEmpleado.objects.filter(AE_TAREA=tarea)
    contratistas_asignados = AsignacionContratista.objects.filter(AEC_TAREA=tarea)
    recursos_asignados = AsignacionRecurso.objects.filter(ART_TAREA=tarea)

    if request.method == 'POST':
        try:
            # Actualizar datos de la tarea
            if tipo_tarea == 'general':
                proyecto_actual = tarea.TG_PROYECTO_CLIENTE
                if request.POST.get('porcentajeAvance'):
                    tarea.TG_NPROGRESO = float(request.POST.get('porcentajeAvance'))
                if request.POST.get('horasTarea'):
                    tarea.TG_NDURACION_REAL = float(request.POST.get('horasTarea'))
            elif tipo_tarea == 'ingenieria':
                proyecto_actual = tarea.TI_PROYECTO_CLIENTE
                if request.POST.get('porcentajeAvance'):
                    tarea.TI_NPROGRESO = float(request.POST.get('porcentajeAvance'))
                if request.POST.get('horasTarea'):
                    tarea.TI_NDURACION_REAL = float(request.POST.get('horasTarea'))
            elif tipo_tarea == 'financiera':
                proyecto_actual = tarea.TF_PROYECTO_CLIENTE
                if request.POST.get('porcentajeAvance'):
                    tarea.TF_NPROGRESO = float(request.POST.get('porcentajeAvance'))
                if request.POST.get('horasTarea'):
                    tarea.TF_NDURACION_REAL = float(request.POST.get('horasTarea'))
            tarea.save()

            # Actualizar asignaciones
            for empleado in empleados_asignados:
                if request.POST.get(f'costo_empleado_{empleado.id}'):
                    empleado.AE_COSTO_REAL = float(request.POST.get(f'costo_empleado_{empleado.id}'))
                if request.POST.get(f'horas_empleado_{empleado.id}'):
                    empleado.AE_HORAS_REALES = float(request.POST.get(f'horas_empleado_{empleado.id}')  )
                if request.POST.get(f'total_empleado_{empleado.id}'):
                    empleado.AE_COSTO_TOTAL = float(request.POST.get(f'total_empleado_{empleado.id}'))
                empleado.save()

            for contratista in contratistas_asignados:
                if request.POST.get(f'costo_contratista_{contratista.id}'):
                    contratista.AEC_COSTO_REAL = float(request.POST.get(f'costo_contratista_{contratista.id}'))
                if request.POST.get(f'horas_contratista_{contratista.id}'):
                    contratista.AEC_HORAS_REALES = float(request.POST.get(f'horas_contratista_{contratista.id}'))
                if request.POST.get(f'total_contratista_{contratista.id}'):
                    contratista.AEC_COSTO_TOTAL = float(request.POST.get(f'total_contratista_{contratista.id}'))
                contratista.save()

            for recurso in recursos_asignados:
                if request.POST.get(f'cantidad_recurso_{recurso.id}'):
                    recurso.ART_CANTIDAD = float(request.POST.get(f'cantidad_recurso_{recurso.id}'))
                if request.POST.get(f'costo_recurso_{recurso.id}'):
                    recurso.ART_COSTO_UNITARIO = float(request.POST.get(f'costo_recurso_{recurso.id}'))
                if request.POST.get(f'horas_recurso_{recurso.id}'):
                    recurso.ART_HORAS_REALES = float(request.POST.get(f'horas_recurso_{recurso.id}'))
                if request.POST.get(f'total_recurso_{recurso.id}'):   
                    total_recurso = request.POST.get(f'total_recurso_{recurso.id}')
                    total_recurso = total_recurso.replace(',', '.')
                    recurso.ART_COSTO_REAL = float(total_recurso)
                recurso.save()

            return JsonResponse({
                'success': True,
                'message': 'Datos de la tarea actualizados correctamente.',
                'redirect_url': reverse('proycli_listone', kwargs={'pk': proyecto_actual.id})
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error al actualizar los datos: {str(e)}'
            }, status=400)

    ctx = {
        'tarea': tarea,
        'empleados_asignados': empleados_asignados,
        'contratistas_asignados': contratistas_asignados,
        'recursos_asignados': recursos_asignados,
        'tipo_tarea': tipo_tarea
    }
    return render(request, 'home/TAREA/tarea_update_data.html', ctx)
# ----------TAREA UPDATE DATA--------------

#--------------------------------------
#----------------TAREAS----------------
#--------------------------------------

def ACTA_REUNION_LISTALL(request):
    try:
        object_list = ACTA_REUNION.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/ACTA_REUNION/actareunion_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ACTA_REUNION_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formACTA_REUNION(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Acta de reunión guardada correctamente')
                return redirect('/actareunion_listall/')
        form = formACTA_REUNION()
        ctx = {
            'form': form
        }
        return render(request, 'home/ACTA_REUNION/actareunion_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ACTA_REUNION_UPDATE(request, pk):
    try:
        acta_reunion = ACTA_REUNION.objects.get(id=pk)
        if request.method == 'POST':
            form = formACTA_REUNION(request.POST, instance=acta_reunion)
            if form.is_valid():
                form.save()
                messages.success(request, 'Acta de reunión actualizada correctamente')
                return redirect('/actareunion_listall/')
        form = formACTA_REUNION(instance=acta_reunion)
        ctx = {
            'form': form
        }
        return render(request, 'home/ACTA_REUNION/actareunion_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COTIZACION_LISTALL(request):
    try:
        object_list = COTIZACION.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/COTIZACION/cotizacion_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COTIZACION_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formCOTIZACION(request.POST)
            if form.is_valid():
                cotizacion = form.save(commit=False)
                cotizacion.CO_CUSUARIO_CREADOR = request.user
                cotizacion.save()
                messages.success(request, 'Cotización guardada correctamente')
                return redirect('/cotizacion_listall/')
        form = formCOTIZACION()
        ctx = {
            'form': form
        }
        return render(request, 'home/COTIZACION/cotizacion_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COTIZACION_ADD_LINE(request):
    try:
        if request.method == 'POST':

            cotizacion_id = request.POST.get('cotizacion_id')
            producto_id = request.POST.get('producto')
            cantidad = request.POST.get('cantidad')
            precio_unitario = request.POST.get('precioUnitario')
            descuento = request.POST.get('descuento')

            # Ensure cantidad and precio_unitario are at least 1
            cantidad = max(1, int(cantidad or 0))
            precio_unitario = max(Decimal('1'), Decimal(precio_unitario or '0'))

            # Recalculate subtotal
            subtotal = Decimal(cantidad) * precio_unitario

            # Ensure descuento is non-negative and not greater than subtotal
            descuento = max(Decimal('0'), min(Decimal(descuento or '0'), subtotal))

            cotizacion = COTIZACION.objects.get(id=cotizacion_id)
            producto = PRODUCTO.objects.get(id=producto_id)

            subtotal = Decimal(cantidad) * Decimal(precio_unitario)
            total = subtotal - Decimal(descuento)

            # Verificar si la combinación de cotización y producto ya existe
            existing_detail = COTIZACION_DETALLE.objects.filter(CD_COTIZACION=cotizacion, CD_PRODUCTO=producto).first()
            if existing_detail:
                existing_detail.delete()

            # Recalculate total
            total = subtotal - descuento

            detalle = COTIZACION_DETALLE(
                CD_COTIZACION=cotizacion,
                CD_PRODUCTO=producto,
                CD_NCANTIDAD=cantidad,
                CD_NPRECIO_UNITARIO=precio_unitario,
                CD_NSUBTOTAL=subtotal,
                CD_NDESCUENTO=descuento,
                CD_NTOTAL=total,
                CD_CUSUARIO_CREADOR=request.user
            )
            detalle.save()

            # Recalculate COTIZACION.CO_NTOTAL
            total_cotizacion = COTIZACION_DETALLE.objects.filter(CD_COTIZACION=cotizacion).aggregate(Sum('CD_NTOTAL'))['CD_NTOTAL__sum'] or 0
            cotizacion.CO_NTOTAL = total_cotizacion
            cotizacion.save()

            messages.success(request, 'Línea de cotización agregada correctamente')
            return redirect(f'/cotizacion_listone/{cotizacion_id}')
        
        return redirect('/cotizacion_listall/')
    except Exception as e:
        errMsg=print(f"Error al agregar línea de cotización: {str(e)}")
        messages.error(request, errMsg)
        return JsonResponse({'error': str(errMsg)}, status=400)

def COTIZACION_UPDATE(request, pk):
    try:
        cotizacion = COTIZACION.objects.get(id=pk)
        if request.method == 'POST':
            form = formCOTIZACION(request.POST, instance=cotizacion)
            if form.is_valid():
                cotizacion = form.save(commit=False)
                cotizacion.CO_CUSUARIO_MODIFICADOR = request.user
                cotizacion.save()
                messages.success(request, 'Cotización actualizada correctamente')
                return redirect('/cotizacion_listall/')
        form = formCOTIZACION(instance=cotizacion)
        ctx = {
            'form': form
        }
        return render(request, 'home/COTIZACION/cotizacion_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def COTIZACION_LISTONE(request, pk):
    try:
        cotizacion = COTIZACION.objects.get(id=pk)
        product_list = list(PRODUCTO.objects.filter(PR_BACTIVO=True).values_list('id', 'PR_CNOMBRE'))
        
        ctx = {
            'cotizacion': cotizacion,
            'product_list': product_list,
        }
        return render(request, 'home/COTIZACION/cotizacion_listone.html', ctx)
    except Exception as e:
        print("ERROR:", e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/cotizacion_listall/')
    
def COTIZACION_GET_DATA(request, pk):
    try:
        cotizacion = COTIZACION.objects.get(id=pk)
        data = {
            'cotizacion': {
                'id': cotizacion.id,
                'CO_CCLIENTE': {
                    'id': cotizacion.CO_CLIENTE.id,
                    'nombre': str(cotizacion.CO_CLIENTE)
                },
                'CO_CNUMERO': cotizacion.CO_CNUMERO,
                'CO_FFECHA': cotizacion.CO_FFECHA.strftime('%Y-%m-%d'),
                'CO_CVALIDO_HASTA': cotizacion.CO_CVALIDO_HASTA.strftime('%Y-%m-%d'),
                'CO_CESTADO': cotizacion.CO_CESTADO,
                'CO_NTOTAL': str(cotizacion.CO_NTOTAL),
                'CO_COBSERVACIONES': cotizacion.CO_COBSERVACIONES,
                'CO_CCOMENTARIO': cotizacion.CO_CCOMENTARIO
            }
        }
        return JsonResponse(data)
    except COTIZACION.DoesNotExist:
        return JsonResponse({'error': 'Cotización no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)



def COTIZACION_LISTONE_FORMAT(request, pk):
    try:
        cotizacion = COTIZACION.objects.get(id=pk)
        product_list = list(PRODUCTO.objects.filter(PR_BACTIVO=True).values_list('id', 'PR_CNOMBRE'))
        
        ctx = {
            'cotizacion': cotizacion,
            'product_list': product_list,
        }
        return render(request, 'home/COTIZACION/cotizacion_listone_format.html', ctx)
    except Exception as e:
        print("ERROR:", e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/cotizacion_listall/')

def COTIZACION_GET_LINE(request, pk):
    try:
        print("id linea:", pk)
        detalle = COTIZACION_DETALLE.objects.get(id=pk)
        
        data = {
            'id': detalle.id,
            'producto': detalle.CD_PRODUCTO.id,
            'cantidad': detalle.CD_NCANTIDAD,
            'precioUnitario': detalle.CD_NPRECIO_UNITARIO,
            'descuento': detalle.CD_NDESCUENTO
        }
        return JsonResponse(data)
    except COTIZACION_DETALLE.DoesNotExist:
        return JsonResponse({'error': 'Línea de cotización no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)

def COTIZACION_DELETE_LINE(request, pk):
    try:
        detalle = COTIZACION_DETALLE.objects.get(id=pk)
        cotizacion_id = detalle.CD_COTIZACION.id
        detalle.delete()
        # Recalculate COTIZACION.CO_NTOTAL
        cotizacion = detalle.CD_COTIZACION
        total_cotizacion = COTIZACION_DETALLE.objects.filter(CD_COTIZACION=cotizacion).aggregate(Sum('CD_NTOTAL'))['CD_NTOTAL__sum'] or 0
        cotizacion.CO_NTOTAL = total_cotizacion
        cotizacion.save()
        return JsonResponse({'success': 'Línea de cotización eliminada correctamente', 'cotizacion_id': cotizacion_id})
    except COTIZACION_DETALLE.DoesNotExist:
        return JsonResponse({'error': 'Línea de cotización no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)

def CHECK_CO_NUMERO(request):
    if request.method == 'POST':
        co_numero = request.POST.get('co_numero')
        exists = COTIZACION.objects.filter(CO_CNUMERO=co_numero).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def ORDEN_VENTA_LISTALL(request):
    try:
        object_list = ORDEN_VENTA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ORDEN_VENTA_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formORDEN_VENTA(request.POST)
            if form.is_valid():
                print("form is valid")
                orden_venta = form.save(commit=False)
                orden_venta.OV_CUSUARIO_CREADOR = request.user
                orden_venta.save()
                print("orden_venta saved")
                # If there's a related cotización, copy its details
                if orden_venta.OV_COTIZACION:
                    print("orden_venta.OV_COTIZACION:", orden_venta.OV_COTIZACION)
                    try:
                        cotizacion_detalles = COTIZACION_DETALLE.objects.filter(CD_COTIZACION=orden_venta.OV_COTIZACION)
                        for cotizacion_detalle in cotizacion_detalles:
                            ORDEN_VENTA_DETALLE.objects.create(
                                OVD_ORDEN_VENTA=orden_venta,
                                OVD_PRODUCTO=cotizacion_detalle.CD_PRODUCTO,
                                OVD_NCANTIDAD=cotizacion_detalle.CD_NCANTIDAD,
                                OVD_NPRECIO_UNITARIO=cotizacion_detalle.CD_NPRECIO_UNITARIO,
                                OVD_NSUBTOTAL=cotizacion_detalle.CD_NSUBTOTAL,
                                OVD_NDESCUENTO=cotizacion_detalle.CD_NDESCUENTO,
                                OVD_NTOTAL=cotizacion_detalle.CD_NTOTAL,
                                OVD_CUSUARIO_CREADOR=request.user
                            )
                    except Exception as e:
                        print(f"Error al copiar detalles de cotización: {str(e)}")

                messages.success(request, 'Orden de venta guardada correctamente')
                return redirect('/orden_venta_listall/')
            else:
                print("Form is not valid. Errors:", form.errors)
                return HttpResponse(form.errors.as_text())
        form = formORDEN_VENTA()
        ctx = {
            'form': form
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')
    
def ORDEN_VENTA_ADD_LINE(request):
    try:
        if request.method == 'POST':

            orden_venta_id = request.POST.get('orden_venta_id')
            producto_id = request.POST.get('producto')
            cantidad = request.POST.get('cantidad')
            precio_unitario = request.POST.get('precioUnitario')
            descuento = request.POST.get('descuento')

            # Ensure cantidad and precio_unitario are at least 1
            cantidad = max(1, int(cantidad or 0))
            precio_unitario = max(Decimal('1'), Decimal(precio_unitario or '0'))

            # Recalculate subtotal
            subtotal = Decimal(cantidad) * precio_unitario

            # Ensure descuento is non-negative and not greater than subtotal
            descuento = max(Decimal('0'), min(Decimal(descuento or '0'), subtotal))

            orden_venta = ORDEN_VENTA.objects.get(id=orden_venta_id)
            producto = PRODUCTO.objects.get(id=producto_id)

            subtotal = Decimal(cantidad) * Decimal(precio_unitario)
            total = subtotal - Decimal(descuento)

            # Verificar si la combinación de orden de venta y producto ya existe
            existing_detail = ORDEN_VENTA_DETALLE.objects.filter(OVD_ORDEN_VENTA=orden_venta, OVD_PRODUCTO=producto).first()
            if existing_detail:
                existing_detail.delete()

            # Recalculate total
            total = subtotal - descuento

            detalle = ORDEN_VENTA_DETALLE(
                OVD_ORDEN_VENTA=orden_venta,
                OVD_PRODUCTO=producto,
                OVD_NCANTIDAD=cantidad,
                OVD_NPRECIO_UNITARIO=precio_unitario,
                OVD_NSUBTOTAL=subtotal,
                OVD_NDESCUENTO=descuento,
                OVD_NTOTAL=total,
                OVD_CUSUARIO_CREADOR=request.user
            )
            detalle.save()

            # Recalculate ORDEN_VENTA.OV_NTOTAL
            total_orden_venta = ORDEN_VENTA_DETALLE.objects.filter(OVD_ORDEN_VENTA=orden_venta).aggregate(Sum('OVD_NTOTAL'))['OVD_NTOTAL__sum'] or 0
            orden_venta.OV_NTOTAL = total_orden_venta
            orden_venta.save()

            messages.success(request, 'Línea de orden de venta agregada correctamente')
            return redirect(f'/orden_venta_listone/{orden_venta_id}')
        
        return redirect('/orden_venta_listall/')
    except Exception as e:
        errMsg=print(f"Error al agregar línea de orden de venta: {str(e)}")
        messages.error(request, errMsg)
        return JsonResponse({'error': str(errMsg)}, status=400)

def ORDEN_VENTA_UPDATE(request, pk):
    try:
        orden_venta = ORDEN_VENTA.objects.get(id=pk)
        if request.method == 'POST':
            form = formORDEN_VENTA(request.POST, instance=orden_venta)
            if form.is_valid():
                orden_venta = form.save(commit=False)
                orden_venta.OV_CUSUARIO_MODIFICADOR = request.user
                orden_venta.save()
                messages.success(request, 'Orden de venta actualizada correctamente')
                return redirect('/orden_venta_listall/')
        form = formORDEN_VENTA(instance=orden_venta)
        ctx = {
            'form': form
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ORDEN_VENTA_LISTONE(request, pk):
    try:
        orden_venta = ORDEN_VENTA.objects.get(id=pk)
        product_list = list(PRODUCTO.objects.filter(PR_BACTIVO=True).values_list('id', 'PR_CNOMBRE'))
        
        ctx = {
            'orden_venta': orden_venta,
            'product_list': product_list,
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_listone.html', ctx)
    except Exception as e:
        print("ERROR:", e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/orden_venta_listall/')

def ORDEN_VENTA_LISTONE_FORMAT(request, pk):
    try:
        orden_venta = ORDEN_VENTA.objects.get(id=pk)
        product_list = list(PRODUCTO.objects.filter(PR_BACTIVO=True).values_list('id', 'PR_CNOMBRE'))
        
        ctx = {
            'orden_venta': orden_venta,
            'product_list': product_list,
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_listone_format.html', ctx)
    except Exception as e:
        print("ERROR:", e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/orden_venta_listall/')

def ORDEN_VENTA_GET_LINE(request, pk):
    try:
        print("id linea:", pk)
        detalle = ORDEN_VENTA_DETALLE.objects.get(id=pk)
        
        data = {
            'id': detalle.id,
            'producto': detalle.OVD_PRODUCTO.id,
            'cantidad': detalle.OVD_NCANTIDAD,
            'precioUnitario': detalle.OVD_NPRECIO_UNITARIO,
            'descuento': detalle.OVD_NDESCUENTO
        }
        return JsonResponse(data)
    except ORDEN_VENTA_DETALLE.DoesNotExist:
        return JsonResponse({'error': 'Línea de orden de venta no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)

def ORDEN_VENTA_DELETE_LINE(request, pk):
    try:
        detalle = ORDEN_VENTA_DETALLE.objects.get(id=pk)
        orden_venta_id = detalle.OVD_ORDEN_VENTA.id
        detalle.delete()
        # Recalculate ORDEN_VENTA.OV_NTOTAL
        orden_venta = detalle.OVD_ORDEN_VENTA
        total_orden_venta = ORDEN_VENTA_DETALLE.objects.filter(OVD_ORDEN_VENTA=orden_venta).aggregate(Sum('OVD_NTOTAL'))['OVD_NTOTAL__sum'] or 0
        orden_venta.OV_NTOTAL = total_orden_venta
        orden_venta.save()
        return JsonResponse({'success': 'Línea de orden de venta eliminada correctamente', 'orden_venta_id': orden_venta_id})
    except ORDEN_VENTA_DETALLE.DoesNotExist:
        return JsonResponse({'error': 'Línea de orden de venta no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)

def CHECK_OV_NUMERO(request):
    if request.method == 'POST':
        ov_numero = request.POST.get('ov_numero')
        exists = ORDEN_VENTA.objects.filter(OV_CNUMERO=ov_numero).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def ORDEN_VENTA_LISTALL(request):
    try:
        object_list = ORDEN_VENTA.objects.all()
        ctx = {
            'object_list': object_list
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_listall.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ORDEN_VENTA_ADDONE(request):
    try:
        if request.method == 'POST':
            form = formORDEN_VENTA(request.POST)
            if form.is_valid():
                print("form is valid")
                orden_venta = form.save(commit=False)
                orden_venta.OV_CUSUARIO_CREADOR = request.user
                orden_venta.save()
                print("orden_venta saved")
                # If there's a related cotización, copy its details
                if orden_venta.OV_COTIZACION:
                    print("orden_venta.OV_COTIZACION:", orden_venta.OV_COTIZACION)
                    try:
                        cotizacion_detalles = COTIZACION_DETALLE.objects.filter(CD_COTIZACION=orden_venta.OV_COTIZACION)
                        for cotizacion_detalle in cotizacion_detalles:
                            ORDEN_VENTA_DETALLE.objects.create(
                                OVD_ORDEN_VENTA=orden_venta,
                                OVD_PRODUCTO=cotizacion_detalle.CD_PRODUCTO,
                                OVD_NCANTIDAD=cotizacion_detalle.CD_NCANTIDAD,
                                OVD_NPRECIO_UNITARIO=cotizacion_detalle.CD_NPRECIO_UNITARIO,
                                OVD_NSUBTOTAL=cotizacion_detalle.CD_NSUBTOTAL,
                                OVD_NDESCUENTO=cotizacion_detalle.CD_NDESCUENTO,
                                OVD_NTOTAL=cotizacion_detalle.CD_NTOTAL,
                                OVD_CUSUARIO_CREADOR=request.user
                            )
                    except Exception as e:
                        print(f"Error al copiar detalles de cotización: {str(e)}")

                messages.success(request, 'Orden de venta guardada correctamente')
                return redirect('/orden_venta_listall/')
            else:
                print("Form is not valid. Errors:", form.errors)
                return HttpResponse(form.errors.as_text())
        form = formORDEN_VENTA()
        ctx = {
            'form': form
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')
    
def ORDEN_VENTA_ADD_LINE(request):
    try:
        if request.method == 'POST':

            orden_venta_id = request.POST.get('orden_venta_id')
            producto_id = request.POST.get('producto')
            cantidad = request.POST.get('cantidad')
            precio_unitario = request.POST.get('precioUnitario')
            descuento = request.POST.get('descuento')

            # Ensure cantidad and precio_unitario are at least 1
            cantidad = max(1, int(cantidad or 0))
            precio_unitario = max(Decimal('1'), Decimal(precio_unitario or '0'))

            # Recalculate subtotal
            subtotal = Decimal(cantidad) * precio_unitario

            # Ensure descuento is non-negative and not greater than subtotal
            descuento = max(Decimal('0'), min(Decimal(descuento or '0'), subtotal))

            orden_venta = ORDEN_VENTA.objects.get(id=orden_venta_id)
            producto = PRODUCTO.objects.get(id=producto_id)

            subtotal = Decimal(cantidad) * Decimal(precio_unitario)
            total = subtotal - Decimal(descuento)

            # Verificar si la combinación de orden de venta y producto ya existe
            existing_detail = ORDEN_VENTA_DETALLE.objects.filter(OVD_ORDEN_VENTA=orden_venta, OVD_PRODUCTO=producto).first()
            if existing_detail:
                existing_detail.delete()

            # Recalculate total
            total = subtotal - descuento

            detalle = ORDEN_VENTA_DETALLE(
                OVD_ORDEN_VENTA=orden_venta,
                OVD_PRODUCTO=producto,
                OVD_NCANTIDAD=cantidad,
                OVD_NPRECIO_UNITARIO=precio_unitario,
                OVD_NSUBTOTAL=subtotal,
                OVD_NDESCUENTO=descuento,
                OVD_NTOTAL=total,
                OVD_CUSUARIO_CREADOR=request.user
            )
            detalle.save()

            # Recalculate ORDEN_VENTA.OV_NTOTAL
            total_orden_venta = ORDEN_VENTA_DETALLE.objects.filter(OVD_ORDEN_VENTA=orden_venta).aggregate(Sum('OVD_NTOTAL'))['OVD_NTOTAL__sum'] or 0
            orden_venta.OV_NTOTAL = total_orden_venta
            orden_venta.save()

            messages.success(request, 'Línea de orden de venta agregada correctamente')
            return redirect(f'/orden_venta_listone/{orden_venta_id}')
        
        return redirect('/orden_venta_listall/')
    except Exception as e:
        errMsg=print(f"Error al agregar línea de orden de venta: {str(e)}")
        messages.error(request, errMsg)
        return JsonResponse({'error': str(errMsg)}, status=400)

def ORDEN_VENTA_UPDATE(request, pk):
    try:
        orden_venta = ORDEN_VENTA.objects.get(id=pk)
        if request.method == 'POST':
            form = formORDEN_VENTA(request.POST, instance=orden_venta)
            if form.is_valid():
                orden_venta = form.save(commit=False)
                orden_venta.OV_CUSUARIO_MODIFICADOR = request.user
                orden_venta.save()
                messages.success(request, 'Orden de venta actualizada correctamente')
                return redirect('/orden_venta_listall/')
        form = formORDEN_VENTA(instance=orden_venta)
        ctx = {
            'form': form
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_addone.html', ctx)
    except Exception as e:
        print(e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/')

def ORDEN_VENTA_LISTONE(request, pk):
    try:
        orden_venta = ORDEN_VENTA.objects.get(id=pk)
        product_list = list(PRODUCTO.objects.filter(PR_BACTIVO=True).values_list('id', 'PR_CNOMBRE'))
        
        ctx = {
            'orden_venta': orden_venta,
            'product_list': product_list,
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_listone.html', ctx)
    except Exception as e:
        print("ERROR:", e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/orden_venta_listall/')

def ORDEN_VENTA_LISTONE_FORMAT(request, pk):
    try:
        orden_venta = ORDEN_VENTA.objects.get(id=pk)
        product_list = list(PRODUCTO.objects.filter(PR_BACTIVO=True).values_list('id', 'PR_CNOMBRE'))
        
        ctx = {
            'orden_venta': orden_venta,
            'product_list': product_list,
        }
        return render(request, 'home/ORDEN_VENTA/orden_venta_listone_format.html', ctx)
    except Exception as e:
        print("ERROR:", e)
        messages.error(request, f'Error, {str(e)}')
        return redirect('/orden_venta_listall/')

def ORDEN_VENTA_GET_LINE(request, pk):
    try:
        print("id linea:", pk)
        detalle = ORDEN_VENTA_DETALLE.objects.get(id=pk)
        
        data = {
            'id': detalle.id,
            'producto': detalle.OVD_PRODUCTO.id,
            'cantidad': detalle.OVD_NCANTIDAD,
            'precioUnitario': detalle.OVD_NPRECIO_UNITARIO,
            'descuento': detalle.OVD_NDESCUENTO
        }
        return JsonResponse(data)
    except ORDEN_VENTA_DETALLE.DoesNotExist:
        return JsonResponse({'error': 'Línea de orden de venta no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)

def ORDEN_VENTA_DELETE_LINE(request, pk):
    try:
        detalle = ORDEN_VENTA_DETALLE.objects.get(id=pk)
        orden_venta_id = detalle.OVD_ORDEN_VENTA.id
        detalle.delete()
        # Recalculate ORDEN_VENTA.OV_NTOTAL
        orden_venta = detalle.OVD_ORDEN_VENTA
        total_orden_venta = ORDEN_VENTA_DETALLE.objects.filter(OVD_ORDEN_VENTA=orden_venta).aggregate(Sum('OVD_NTOTAL'))['OVD_NTOTAL__sum'] or 0
        orden_venta.OV_NTOTAL = total_orden_venta
        orden_venta.save()
        return JsonResponse({'success': 'Línea de orden de venta eliminada correctamente', 'orden_venta_id': orden_venta_id})
    except ORDEN_VENTA_DETALLE.DoesNotExist:
        return JsonResponse({'error': 'Línea de orden de venta no encontrada'}, status=404)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)

def CHECK_OV_NUMERO(request):
    if request.method == 'POST':
        ov_numero = request.POST.get('ov_numero')
        exists = ORDEN_VENTA.objects.filter(OV_CNUMERO=ov_numero).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# def BOLETA_GARANTIA_LISTALL(request):
#     try:
#         object_list = BOLETA_GARANTIA.objects.all()
#         ctx = {
#             'object_list': object_list
#         }
#         return render(request, 'home/BOLETA_GARANTIA/boletagarantia_listall.html', ctx)
#     except Exception as e:
#         print(e)
#         messages.error(request, f'Error, {str(e)}')
#         return redirect('/')

# def BOLETA_GARANTIA_ADDONE(request):
#     try:
#         if request.method =='POST':
#             form = formBOLETA_GARANTIA(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Boleta de garantía guardada correctamente')
#                 return redirect('/boletagarantia_listall/')
#         form = formBOLETA_GARANTIA()
#         ctx = {
#             'form': form
#         }
#         return render(request, 'home/BOLETA_GARANTIA/boletagarantia_addone.html', ctx)
#     except Exception as e:
#         print(e)
#         messages.error(request, f'Error, {str(e)}')
#         return redirect('/')

# def BOLETA_GARANTIA_UPDATE(request, pk):
#     try:
#         boleta_garantia = BOLETA_GARANTIA.objects.get(id=pk)
#         if request.method == 'POST':
#             form = formBOLETA_GARANTIA(request.POST, instance=boleta_garantia)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Boleta de garantía actualizada correctamente')
#                 return redirect('/boletagarantia_listall/')
#         form = formBOLETA_GARANTIA(instance=boleta_garantia)
#         ctx = {
#             'form': form
#         }
#         return render(request, 'home/BOLETA_GARANTIA/boletagarantia_addone.html', ctx)
#     except Exception as e:
#         print(e)
#         messages.error(request, f'Error, {str(e)}')
#         return redirect('/')
