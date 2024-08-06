import datetime
from django import forms
from django.contrib.auth.models import *
from apps.home.models import *
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.forms import ModelMultipleChoiceField
from collections import OrderedDict

def validate_file_size(value):
    filesize = value.file.size
    if filesize > 5242880:  # 5MB limit
        raise ValidationError("El tamaño máximo de archivo que se puede subir es de 5MB")
    else:
        return value
    
class formREGION(forms.ModelForm):
    class Meta:
        model = REGION
        fields = ['RG_CNOMBRE', 'RG_CCODIGO']  # Adjust fields to match model attributes
        labels = {
            'RG_CNOMBRE': 'Nombre',
            'RG_CCODIGO': 'Código'
        }
        widgets = {
            'RG_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'RG_CCODIGO': forms.TextInput(attrs={'class': 'form-control'})
        }

class formPROVINCIA(forms.ModelForm):
    class Meta:
        model = PROVINCIA
        fields = ['PV_CNOMBRE', 'PV_CCODIGO', 'RG_NID']  # Adjust fields to match model attributes
        labels = {
            'PV_CNOMBRE': 'Nombre',
            'PV_CCODIGO': 'Código',
            'REGION': 'Región'
        }
        widgets = {
            'PV_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'PV_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'RG_NID': forms.Select(attrs={'class': 'form-control js-example-placeholder-multiple', 'id': 'id_region'}),
            
        }

class formCOMUNA(forms.ModelForm):
    class Meta:
        model = COMUNA
        fields = ['COM_CNOMBRE', 'COM_CCODIGO', 'PV_NID']  # Adjust fields to match model attributes
        labels = {
            'COM_CNOMBRE': 'Nombre',
            'COM_CCODIGO': 'Código',
            'PV_NID': 'Provincia'
        }
        widgets = {
            'COM_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'COM_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'PV_NID': forms.Select(attrs={'class': 'form-control js-example-placeholder-multiple', 'id': 'id_provincia'}),
        }

class formSYSTEM_LOG(forms.ModelForm):
    class Meta:
        model = SYSTEM_LOG
        fields = ['USER_CREATOR_ID', 'LG_ACTION', 'LG_DESCRIPTION']
        labels = {
            'USER_CREATOR_ID': 'Usuario Creador',
            'LG_ACTION': 'Acción',
            'LG_DESCRIPTION': 'Descripción'
        }
        widgets = {
            'USER_CREATOR_ID': forms.Select(attrs={'class': 'form-control'}),
            'LG_ACTION': forms.TextInput(attrs={'class': 'form-control'}),
            'LG_DESCRIPTION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        super(formSYSTEM_LOG, self).__init__(*args, **kwargs)
        self.fields['LG_TIMESTAMP'].widget = forms.HiddenInput()

class formPARAMETRO(forms.ModelForm):
    class Meta:
        model = PARAMETRO
        fields = ['PM_CGRUPO', 'PM_CCODIGO', 'PM_CDESCRIPCION', 'PM_CVALOR']
        labels = {
            'PM_CGRUPO': 'Grupo',
            'PM_CCODIGO': 'Código',
            'PM_CDESCRIPCION': 'Descripción',
            'PM_CVALOR': 'Valor'
        }
        widgets = {
            'PM_CGRUPO': forms.TextInput(attrs={'class': 'form-control'}),
            'PM_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'PM_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'PM_CVALOR': forms.TextInput(attrs={'class': 'form-control'})
        }

class formALERTA(forms.ModelForm):
    class Meta:
        model = ALERTA
        fields = ['AL_USUARIO_ORIGEN', 'AL_USUARIO_DESTINO', 'AL_CCLASE', 'AL_CASUNTO', 'AL_CCUERPO']
        labels = {
            'AL_USUARIO_ORIGEN': 'Usuario Origen',
            'AL_USUARIO_DESTINO': 'Usuario Destino',
            'AL_CCLASE': 'Clase',
            'AL_CASUNTO': 'Asunto',
            'AL_CCUERPO': 'Cuerpo'
        }
        widgets = {
            'AL_USUARIO_ORIGEN': forms.Select(attrs={'class': 'form-control'}),
            'AL_USUARIO_DESTINO': forms.Select(attrs={'class': 'form-control'}),
            'AL_CCLASE': forms.TextInput(attrs={'class': 'form-control'}),
            'AL_CASUNTO': forms.TextInput(attrs={'class': 'form-control'}),
            'AL_CCUERPO': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }

    def __init__(self, *args, **kwargs):
        super(formALERTA, self).__init__(*args, **kwargs)
        self.fields['AL_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['AL_FFECHA_ENVIO'].widget = forms.HiddenInput()
        self.fields['AL_FFECHA_LECTURA'].widget = forms.HiddenInput()
        self.fields['AL_BLEIDA'].widget = forms.HiddenInput()

class formROL(forms.ModelForm):
    class Meta:
        model = ROL
        fields = ['RO_CNOMBRE', 'RO_CDESCRIPCION', 'RO_BACTIVO']
        labels = {
            'RO_CNOMBRE': 'Nombre del rol',
            'RO_CDESCRIPCION': 'Descripción del rol',
            'RO_BACTIVO': 'Activo'
        }
        widgets = {
            'RO_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'RO_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'RO_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formROL, self).__init__(*args, **kwargs)
        self.fields['RO_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['RO_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formCATEGORIA_PROYECTO(forms.ModelForm):
    class Meta:
        model = CATEGORIA_PROYECTO
        fields = ['CA_CNOMBRE', 'CA_CDESCRIPCION', 'CA_BACTIVA']
        labels = {
            'CA_CNOMBRE': 'Nombre de la categoría',
            'CA_CDESCRIPCION': 'Descripción de la categoría',
            'CA_BACTIVA': 'Activa'
        }
        widgets = {
            'CA_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'CA_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'CA_BACTIVA': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formCATEGORIA_PROYECTO, self).__init__(*args, **kwargs)
        self.fields['CA_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formCATEGORIA_CLIENTE(forms.ModelForm):
    class Meta:
        model = CATEGORIA_CLIENTE
        fields = ['CA_CNOMBRE', 'CA_CDESCRIPCION', 'CA_BACTIVA']
        labels = {
            'CA_CNOMBRE': 'Nombre de la categoría',
            'CA_CDESCRIPCION': 'Descripción de la categoría',
            'CA_BACTIVA': 'Activa'
        }
        widgets = {
            'CA_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'CA_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'CA_BACTIVA': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formCATEGORIA_CLIENTE, self).__init__(*args, **kwargs)
        self.fields['CA_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formTIPO_PROYECTO(forms.ModelForm):
    class Meta:
        model = TIPO_PROYECTO
        fields = ['TP_CNOMBRE', 'TP_CDESCRIPCION', 'TP_BACTIVO']
        labels = {
            'TP_CNOMBRE': 'Nombre del tipo de proyecto',
            'TP_CDESCRIPCION': 'Descripción del tipo de proyecto',
            'TP_BACTIVO': 'Activo'
        }
        widgets = {
            'TP_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'TP_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'TP_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formTIPO_PROYECTO, self).__init__(*args, **kwargs)
        self.fields['TP_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['TP_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formPERMISO(forms.ModelForm):
    class Meta:
        model = PERMISO
        fields = ['PE_CNOMBRE', 'PE_CDESCRIPCION', 'PE_BACTIVO']
        labels = {
            'PE_CNOMBRE': 'Nombre del permiso',
            'PE_CDESCRIPCION': 'Descripción del permiso',
            'PE_BACTIVO': 'Activo'
        }
        widgets = {
            'PE_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'PE_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'PE_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formPERMISO, self).__init__(*args, **kwargs)
        self.fields['PE_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['PE_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formPERMISO_ROL(forms.ModelForm):
    class Meta:
        model = PERMISO_ROL
        fields = ['PR_CPERMISO', 'PR_CROL', 'PR_BACTIVO']
        labels = {
            'PR_CPERMISO': 'Permiso',
            'PR_CROL': 'Rol',
            'PR_BACTIVO': 'Activo'
        }
        widgets = {
            'PR_CPERMISO': forms.Select(attrs={'class': 'form-control'}),
            'PR_CROL': forms.Select(attrs={'class': 'form-control'}),
            'PR_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formPERMISO_ROL, self).__init__(*args, **kwargs)
        self.fields['PR_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['PR_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formUSUARIO_ROL(forms.ModelForm):
    class Meta:
        model = USUARIO_ROL
        fields = ['UR_CUSUARIO', 'UR_CROL', 'UR_BACTIVO']
        labels = {
            'UR_CUSUARIO': 'Usuario',
            'UR_CROL': 'Rol',
            'UR_BACTIVO': 'Activo'
        }
        widgets = {
            'UR_CUSUARIO': forms.Select(attrs={'class': 'form-control'}),
            'UR_CROL': forms.Select(attrs={'class': 'form-control'}),
            'UR_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formUSUARIO_ROL, self).__init__(*args, **kwargs)
        self.fields['UR_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['UR_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

class formCLIENTE(forms.ModelForm):
    class Meta:
        model = CLIENTE
        fields = [
            'CL_CNOMBRE', 'CL_CRUT', 'CL_CDIRECCION', 'CL_CREGION', 'CL_CPROVINCIA', 
            'CL_CCOMUNA', 'CL_CTELEFONO', 'CL_CEMAIL', 'CL_CPERSONA_CONTACTO', 
            'CL_CSITIO_WEB', 'CL_CRUBRO', 'CL_BACTIVO', 'CL_BPROSPECTO', 'CL_CCATEGORIA',
            'CL_CUSUARIO_GESTOR'
        ]
        labels = {
            'CL_CNOMBRE': 'Nombre de la empresa',
            'CL_CRUT': 'RUT',
            'CL_CDIRECCION': 'Dirección',
            'CL_CREGION': 'Región',
            'CL_CPROVINCIA': 'Provincia',
            'CL_CCOMUNA': 'Comuna',
            'CL_CTELEFONO': 'Teléfono',
            'CL_CEMAIL': 'Correo electrónico',
            'CL_CPERSONA_CONTACTO': 'Persona de contacto',
            'CL_CSITIO_WEB': 'Sitio web',
            'CL_CRUBRO': 'Rubro',
            'CL_BACTIVO': 'Activo',
            'CL_BPROSPECTO': 'Prospecto',
            'CL_CCATEGORIA': 'Categoría del cliente',
            'CL_CUSUARIO_GESTOR': 'Usuario gestor'
        }
        widgets = {
            'CL_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'CL_CRUT': forms.TextInput(attrs={'class': 'form-control'}),
            'CL_CDIRECCION': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'CL_CREGION': forms.Select(attrs={'class': 'form-control'}),
            'CL_CPROVINCIA': forms.Select(attrs={'class': 'form-control'}),
            'CL_CCOMUNA': forms.Select(attrs={'class': 'form-control'}),
            'CL_CTELEFONO': forms.TextInput(attrs={'class': 'form-control'}),
            'CL_CEMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
            'CL_CPERSONA_CONTACTO': forms.TextInput(attrs={'class': 'form-control'}),
            'CL_CSITIO_WEB': forms.URLInput(attrs={'class': 'form-control'}),
            'CL_CRUBRO': forms.TextInput(attrs={'class': 'form-control'}),
            'CL_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'CL_BPROSPECTO': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'CL_CCATEGORIA': forms.Select(attrs={'class': 'form-control'}),
            'CL_CUSUARIO_GESTOR': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formCLIENTE, self).__init__(*args, **kwargs)
        self.fields['CL_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CL_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['CL_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['CL_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

        # Form for CONTACTO_CLIENTE model
        class formCONTACTO_CLIENTE(forms.ModelForm):
            class Meta:
                model = CONTACTO_CLIENTE
                fields = [
                    'CC_CLIENTE', 'CC_CNOMBRE', 'CC_CAPELLIDO', 'CC_CCARGO',
                    'CC_CTELEFONO', 'CC_CEMAIL', 'CC_BACTIVO'
                ]
                labels = {
                    'CC_CLIENTE': 'Cliente',
                    'CC_CNOMBRE': 'Nombre del contacto',
                    'CC_CAPELLIDO': 'Apellido del contacto',
                    'CC_CCARGO': 'Cargo',
                    'CC_CTELEFONO': 'Teléfono',
                    'CC_CEMAIL': 'Correo electrónico',
                    'CC_BACTIVO': 'Activo'
                }
                widgets = {
                    'CC_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
                    'CC_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
                    'CC_CAPELLIDO': forms.TextInput(attrs={'class': 'form-control'}),
                    'CC_CCARGO': forms.TextInput(attrs={'class': 'form-control'}),
                    'CC_CTELEFONO': forms.TextInput(attrs={'class': 'form-control'}),
                    'CC_CEMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
                    'CC_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
                }

            def __init__(self, *args, **kwargs):
                super(formCONTACTO_CLIENTE, self).__init__(*args, **kwargs)
                self.fields['CC_FFECHA_CREACION'].widget = forms.HiddenInput()
                self.fields['CC_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
                self.fields['CC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
                self.fields['CC_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for DIRECCION_CLIENTE model
class formDIRECCION_CLIENTE(forms.ModelForm):
    class Meta:
        model = DIRECCION_CLIENTE
        fields = [
            'DR_CLIENTE', 'DR_CDIRECCION', 'DR_CREGION', 'DR_CPROVINCIA',
            'DR_CCOMUNA', 'DR_CTIPO', 'DR_BACTIVA'
        ]
        labels = {
            'DR_CLIENTE': 'Cliente',
            'DR_CDIRECCION': 'Dirección',
            'DR_CREGION': 'Región',
            'DR_CPROVINCIA': 'Provincia',
            'DR_CCOMUNA': 'Comuna',
            'DR_CTIPO': 'Tipo de dirección',
            'DR_BACTIVA': 'Activa'
        }
        widgets = {
            'DR_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'DR_CDIRECCION': forms.Textarea(attrs={'class': 'form-control'}),
            'DR_CREGION': forms.Select(attrs={'class': 'form-control'}),
            'DR_CPROVINCIA': forms.Select(attrs={'class': 'form-control'}),
            'DR_CCOMUNA': forms.Select(attrs={'class': 'form-control'}),
            'DR_CTIPO': forms.TextInput(attrs={'class': 'form-control'}),
            'DR_BACTIVA': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formDIRECCION_CLIENTE, self).__init__(*args, **kwargs)
        self.fields['DR_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['DR_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['DR_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['DR_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for PRODUCTO model
class formPRODUCTO(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = [
            'PR_CNOMBRE', 'PR_CDESCRIPCION', 'PR_BACTIVO', 'PR_BSERVICIO'
        ]
        labels = {
            'PR_CNOMBRE': 'Nombre del producto',
            'PR_CDESCRIPCION': 'Descripción',
            'PR_BACTIVO': 'Activo',
            'PR_BSERVICIO': 'Tipo de producto'
        }
        widgets = {
            'PR_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'PR_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'PR_BACTIVO': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'PR_BSERVICIO': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super(formPRODUCTO, self).__init__(*args, **kwargs)
        self.fields['PR_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['PR_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['PR_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['PR_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for COTIZACION model
class formCOTIZACION(forms.ModelForm):
    class Meta:
        model = COTIZACION
        fields = [
            'CO_CLIENTE', 'CO_CNUMERO', 'CO_FFECHA', 'CO_CVALIDO_HASTA',
            'CO_CESTADO', 'CO_NTOTAL', 'CO_COBSERVACIONES', 'CO_CCOMENTARIO'
        ]
        labels = {
            'CO_CLIENTE': 'Cliente',
            'CO_CNUMERO': 'Número de cotización',
            'CO_FFECHA': 'Fecha de cotización',
            'CO_CVALIDO_HASTA': 'Válido hasta',
            'CO_CESTADO': 'Estado',
            'CO_NTOTAL': 'Total',
            'CO_COBSERVACIONES': 'Observaciones',
            'CO_CCOMENTARIO': 'Comentarios generales'
        }
        widgets = {
            'CO_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'CO_CNUMERO': forms.TextInput(attrs={'class': 'form-control'}),
            'CO_FFECHA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CO_CVALIDO_HASTA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CO_CESTADO': forms.Select(attrs={'class': 'form-control'}),
            'CO_NTOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'CO_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'CO_CCOMENTARIO': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formCOTIZACION, self).__init__(*args, **kwargs)
        self.fields['CO_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CO_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['CO_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['CO_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for COTIZACION_DETALLE model
class formCOTIZACION_DETALLE(forms.ModelForm):
    class Meta:
        model = COTIZACION_DETALLE
        fields = [
            'CD_COTIZACION', 'CD_PRODUCTO', 'CD_NCANTIDAD', 'CD_NPRECIO_UNITARIO',
            'CD_NSUBTOTAL', 'CD_NDESCUENTO', 'CD_NTOTAL'
        ]
        labels = {
            'CD_COTIZACION': 'Cotización',
            'CD_PRODUCTO': 'Producto',
            'CD_NCANTIDAD': 'Cantidad',
            'CD_NPRECIO_UNITARIO': 'Precio unitario',
            'CD_NSUBTOTAL': 'Subtotal',
            'CD_NDESCUENTO': 'Descuento',
            'CD_NTOTAL': 'Total'
        }
        widgets = {
            'CD_COTIZACION': forms.Select(attrs={'class': 'form-control'}),
            'CD_PRODUCTO': forms.Select(attrs={'class': 'form-control'}),
            'CD_NCANTIDAD': forms.NumberInput(attrs={'class': 'form-control'}),
            'CD_NPRECIO_UNITARIO': forms.NumberInput(attrs={'class': 'form-control'}),
            'CD_NSUBTOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'CD_NDESCUENTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'CD_NTOTAL': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formCOTIZACION_DETALLE, self).__init__(*args, **kwargs)
        self.fields['CD_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CD_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['CD_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['CD_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for ORDEN_VENTA model
class formORDEN_VENTA(forms.ModelForm):
    class Meta:
        model = ORDEN_VENTA
        fields = [
            'OV_CCLIENTE', 'OV_CNUMERO', 'OV_FFECHA', 'OV_FFECHA_ENTREGA',
            'OV_CESTADO', 'OV_NTOTAL', 'OV_COBSERVACIONES', 'OV_CCOMENTARIO',
            'OV_COTIZACION'
        ]
        labels = {
            'OV_CCLIENTE': 'Cliente',
            'OV_CNUMERO': 'Número de orden de venta',
            'OV_FFECHA': 'Fecha de orden',
            'OV_FFECHA_ENTREGA': 'Fecha de entrega',
            'OV_CESTADO': 'Estado',
            'OV_NTOTAL': 'Total',
            'OV_COBSERVACIONES': 'Observaciones',
            'OV_CCOMENTARIO': 'Comentarios generales',
            'OV_COTIZACION': 'Cotización'
        }
        widgets = {
            'OV_CCLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'OV_CNUMERO': forms.TextInput(attrs={'class': 'form-control'}),
            'OV_FFECHA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'OV_FFECHA_ENTREGA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'OV_CESTADO': forms.Select(attrs={'class': 'form-control'}),
            'OV_NTOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'OV_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'OV_CCOMENTARIO': forms.Textarea(attrs={'class': 'form-control'}),
            'OV_COTIZACION': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formORDEN_VENTA, self).__init__(*args, **kwargs)
        self.fields['OV_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['OV_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['OV_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['OV_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for ORDEN_VENTA_DETALLE model
class formORDEN_VENTA_DETALLE(forms.ModelForm):
    class Meta:
        model = ORDEN_VENTA_DETALLE
        fields = [
            'OVD_ORDEN_VENTA', 'OVD_PRODUCTO', 'OVD_NCANTIDAD',
            'OVD_NPRECIO_UNITARIO', 'OVD_NSUBTOTAL', 'OVD_NDESCUENTO', 'OVD_NTOTAL'
        ]
        labels = {
            'OVD_ORDEN_VENTA': 'Orden de Venta',
            'OVD_PRODUCTO': 'Producto',
            'OVD_NCANTIDAD': 'Cantidad',
            'OVD_NPRECIO_UNITARIO': 'Precio unitario',
            'OVD_NSUBTOTAL': 'Subtotal',
            'OVD_NDESCUENTO': 'Descuento',
            'OVD_NTOTAL': 'Total'
        }
        widgets = {
            'OVD_ORDEN_VENTA': forms.Select(attrs={'class': 'form-control'}),
            'OVD_PRODUCTO': forms.Select(attrs={'class': 'form-control'}),
            'OVD_NCANTIDAD': forms.NumberInput(attrs={'class': 'form-control'}),
            'OVD_NPRECIO_UNITARIO': forms.NumberInput(attrs={'class': 'form-control'}),
            'OVD_NSUBTOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'OVD_NDESCUENTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'OVD_NTOTAL': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formORDEN_VENTA_DETALLE, self).__init__(*args, **kwargs)
        self.fields['OVD_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['OVD_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['OVD_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['OVD_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for FACTURA model
class formFACTURA(forms.ModelForm):
    class Meta:
        model = FACTURA
        fields = [
            'FA_CORDEN_VENTA', 'FA_CNUMERO', 'FA_FFECHA', 'FA_FFECHA_VENCIMIENTO',
            'FA_CESTADO', 'FA_NTOTAL', 'FA_COBSERVACIONES', 'FA_CESTADO_PAGO',
            'FA_NMONTO_PAGADO', 'FA_FFECHA_ULTIMO_PAGO'
        ]
        labels = {
            'FA_CORDEN_VENTA': 'Orden de Venta',
            'FA_CNUMERO': 'Número de factura',
            'FA_FFECHA': 'Fecha de factura',
            'FA_FFECHA_VENCIMIENTO': 'Fecha de vencimiento',
            'FA_CESTADO': 'Estado',
            'FA_NTOTAL': 'Total',
            'FA_COBSERVACIONES': 'Observaciones',
            'FA_CESTADO_PAGO': 'Estado de pago',
            'FA_NMONTO_PAGADO': 'Monto pagado',
            'FA_FFECHA_ULTIMO_PAGO': 'Fecha del último pago'
        }
        widgets = {
            'FA_CORDEN_VENTA': forms.Select(attrs={'class': 'form-control'}),
            'FA_CNUMERO': forms.TextInput(attrs={'class': 'form-control'}),
            'FA_FFECHA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'FA_FFECHA_VENCIMIENTO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'FA_CESTADO': forms.Select(attrs={'class': 'form-control'}),
            'FA_NTOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'FA_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'FA_CESTADO_PAGO': forms.Select(attrs={'class': 'form-control'}),
            'FA_NMONTO_PAGADO': forms.NumberInput(attrs={'class': 'form-control'}),
            'FA_FFECHA_ULTIMO_PAGO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(formFACTURA, self).__init__(*args, **kwargs)
        self.fields['FA_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['FA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['FA_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['FA_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for FACTURA_DETALLE model
class formFACTURA_DETALLE(forms.ModelForm):
    class Meta:
        model = FACTURA_DETALLE
        fields = [
            'FAD_FACTURA', 'FAD_PRODUCTO', 'FAD_NCANTIDAD', 'FAD_NPRECIO_UNITARIO',
            'FAD_NSUBTOTAL', 'FAD_NDESCUENTO', 'FAD_NTOTAL'
        ]
        labels = {
            'FAD_FACTURA': 'Factura',
            'FAD_PRODUCTO': 'Producto',
            'FAD_NCANTIDAD': 'Cantidad',
            'FAD_NPRECIO_UNITARIO': 'Precio unitario',
            'FAD_NSUBTOTAL': 'Subtotal',
            'FAD_NDESCUENTO': 'Descuento',
            'FAD_NTOTAL': 'Total'
        }
        widgets = {
            'FAD_FACTURA': forms.Select(attrs={'class': 'form-control'}),
            'FAD_PRODUCTO': forms.Select(attrs={'class': 'form-control'}),
            'FAD_NCANTIDAD': forms.NumberInput(attrs={'class': 'form-control'}),
            'FAD_NPRECIO_UNITARIO': forms.NumberInput(attrs={'class': 'form-control'}),
            'FAD_NSUBTOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'FAD_NDESCUENTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'FAD_NTOTAL': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formFACTURA_DETALLE, self).__init__(*args, **kwargs)
        self.fields['FAD_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['FAD_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['FAD_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['FAD_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for EMPLEADO model
class formEMPLEADO(forms.ModelForm):
    class Meta:
        model = EMPLEADO
        fields = [
            'EM_CCODIGO', 'EM_CNOMBRE', 'EM_CAPELLIDO', 'EM_CRUT', 'EM_CFECHA_NACIMIENTO',
            'EM_CDIRECCION', 'EM_CTELEFONO', 'EM_CEMAIL', 'EM_FFECHA_CONTRATACION',
            'EM_CCARGO', 'EM_CDEPARTAMENTO', 'EM_CESTADO'
        ]
        widgets = {
            'EM_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CAPELLIDO': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CRUT': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CFECHA_NACIMIENTO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'EM_CDIRECCION': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CTELEFONO': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CEMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
            'EM_FFECHA_CONTRATACION': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'EM_CCARGO': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CDEPARTAMENTO': forms.TextInput(attrs={'class': 'form-control'}),
            'EM_CESTADO': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formEMPLEADO, self).__init__(*args, **kwargs)
        self.fields['EM_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['EM_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['EM_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['EM_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for EMPLEADO_ADJUNTO model
class formEMPLEADO_ADJUNTO(forms.ModelForm):
    class Meta:
        model = EMPLEADO_ADJUNTO
        fields = [
            'EA_EMPLEADO', 'EA_CNOMBRE', 'EA_CDESCRIPCION', 'EA_CARCHIVO', 'EA_CTIPO'
        ]
        widgets = {
            'EA_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'EA_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'EA_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'EA_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'EA_CTIPO': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formEMPLEADO_ADJUNTO, self).__init__(*args, **kwargs)
        self.fields['EA_FFECHA_SUBIDA'].widget = forms.HiddenInput()
        self.fields['EA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['EA_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['EA_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for CONTRATISTA model
class formCONTRATISTA(forms.ModelForm):
    class Meta:
        model = CONTRATISTA
        fields = [
            'CO_CCODIGO', 'CO_CNOMBRE', 'CO_CRUT', 'CO_CDIRECCION', 'CO_CTELEFONO',
            'CO_CEMAIL', 'CO_FFECHA_CONTRATACION', 'CO_CESTADO'
        ]
        widgets = {
            'CO_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'CO_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'CO_CRUT': forms.TextInput(attrs={'class': 'form-control'}),
            'CO_CDIRECCION': forms.TextInput(attrs={'class': 'form-control'}),
            'CO_CTELEFONO': forms.TextInput(attrs={'class': 'form-control'}),
            'CO_CEMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
            'CO_FFECHA_CONTRATACION': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CO_CESTADO': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formCONTRATISTA, self).__init__(*args, **kwargs)
        self.fields['CO_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CO_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['CO_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['CO_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for CONTRATISTA_ADJUNTO model
class formCONTRATISTA_ADJUNTO(forms.ModelForm):
    class Meta:
        model = CONTRATISTA_ADJUNTO
        fields = [
            'CA_CONTRATISTA', 'CA_CNOMBRE', 'CA_CDESCRIPCION', 'CA_CARCHIVO', 'CA_CTIPO'
        ]
        widgets = {
            'CA_CONTRATISTA': forms.Select(attrs={'class': 'form-control'}),
            'CA_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'CA_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'CA_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'CA_CTIPO': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formCONTRATISTA_ADJUNTO, self).__init__(*args, **kwargs)
        self.fields['CA_FFECHA_SUBIDA'].widget = forms.HiddenInput()
        self.fields['CA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['CA_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['CA_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for EMPLEADO_CONTRATISTA model
class formEMPLEADO_CONTRATISTA(forms.ModelForm):
    class Meta:
        model = EMPLEADO_CONTRATISTA
        fields = [
            'EC_CONTRATISTA', 'EC_CCODIGO', 'EC_CNOMBRE', 'EC_CAPELLIDO', 'EC_CRUT',
            'EC_CFECHA_NACIMIENTO', 'EC_CDIRECCION', 'EC_CTELEFONO', 'EC_CEMAIL',
            'EC_FFECHA_CONTRATACION', 'EC_CCARGO', 'EC_CESTADO'
        ]
        widgets = {
            'EC_CONTRATISTA': forms.Select(attrs={'class': 'form-control'}),
            'EC_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CAPELLIDO': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CRUT': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CFECHA_NACIMIENTO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'EC_CDIRECCION': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CTELEFONO': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CEMAIL': forms.EmailInput(attrs={'class': 'form-control'}),
            'EC_FFECHA_CONTRATACION': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'EC_CCARGO': forms.TextInput(attrs={'class': 'form-control'}),
            'EC_CESTADO': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formEMPLEADO_CONTRATISTA, self).__init__(*args, **kwargs)
        self.fields['EC_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['EC_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['EC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['EC_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for EMPLEADO_CONTRATISTA_ADJUNTO model
class formEMPLEADO_CONTRATISTA_ADJUNTO(forms.ModelForm):
    class Meta:
        model = EMPLEADO_CONTRATISTA_ADJUNTO
        fields = [
            'ECA_EMPLEADO', 'ECA_CNOMBRE', 'ECA_CDESCRIPCION', 'ECA_CARCHIVO', 'ECA_CTIPO'
        ]
        widgets = {
            'ECA_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'ECA_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'ECA_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'ECA_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'ECA_CTIPO': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(formEMPLEADO_CONTRATISTA_ADJUNTO, self).__init__(*args, **kwargs)
        self.fields['ECA_FFECHA_SUBIDA'].widget = forms.HiddenInput()
        self.fields['ECA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['ECA_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['ECA_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for CONTRATO_CLIENTE model
class formCONTRATO_CLIENTE(forms.ModelForm):
    class Meta:
        model = CONTRATO_CLIENTE
        fields = [
            'CC_CCODIGO', 'CC_CLIENTE', 'CC_FFECHA_INICIO', 'CC_FFECHA_FIN', 'CC_NESTADO',
            'CC_NVALOR_TOTAL', 'CC_CTERMS_CONDICIONES', 'CC_COBSERVACIONES'
        ]
        widgets = {
            'CC_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'CC_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'CC_FFECHA_INICIO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CC_FFECHA_FIN': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CC_NESTADO': forms.Select(attrs={'class': 'form-control'}),
            'CC_NVALOR_TOTAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'CC_CTERMS_CONDICIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'CC_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formCONTRATO_CLIENTE, self).__init__(*args, **kwargs)
        self.fields['CC_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['CC_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['CC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['CC_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for ANEXO model
class formANEXO(forms.ModelForm):
    class Meta:
        model = ANEXO
        fields = [
            'AN_CCODIGO', 'AN_CONTRATO', 'AN_CNOMBRE', 'AN_CDESCRIPCION', 'AN_CARCHIVO', 'AN_CTIPO'
        ]
        widgets = {
            'AN_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'AN_CONTRATO': forms.Select(attrs={'class': 'form-control'}),
            'AN_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'AN_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'AN_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'AN_CTIPO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formANEXO, self).__init__(*args, **kwargs)
        self.fields['AN_FFECHA_SUBIDA'].widget = forms.HiddenInput()
        self.fields['AN_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['AN_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['AN_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for PROYECTO_CLIENTE model
class formPROYECTO_CLIENTE(forms.ModelForm):
    class Meta:
        model = PROYECTO_CLIENTE
        fields = [
            'PC_CCODIGO', 'PC_CNOMBRE', 'PC_CDESCRIPCION', 'PC_CLIENTE', 'PC_CCATEGORIA',
            'PC_CTIPO', 'PC_FFECHA_INICIO', 'PC_FFECHA_FIN_ESTIMADA', 'PC_FFECHA_FIN_REAL',
            'PC_CESTADO', 'PC_NPRESUPUESTO', 'PC_COBSERVACIONES', 'PC_CONTACTO_CLIENTE',
            'PC_DIRECCION_CLIENTE', 'PC_NVALOR_HORA', 'PC_NHORAS_ESTIMADAS', 'PC_NCOSTO_ESTIMADO',
            'PC_NHORAS_REALES', 'PC_NCOSTO_REAL', 'PC_NMARGEN'
        ]
        widgets = {
            'PC_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'PC_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'PC_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'PC_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'PC_CCATEGORIA': forms.Select(attrs={'class': 'form-control'}),
            'PC_CTIPO': forms.Select(attrs={'class': 'form-control'}),
            'PC_FFECHA_INICIO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'PC_FFECHA_FIN_ESTIMADA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'PC_FFECHA_FIN_REAL': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'PC_CESTADO': forms.TextInput(attrs={'class': 'form-control'}),
            'PC_NPRESUPUESTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'PC_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'PC_CONTACTO_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'PC_DIRECCION_CLIENTE': forms.Select(attrs={'class': 'form-control'}),
            'PC_NVALOR_HORA': forms.NumberInput(attrs={'class': 'form-control'}),
            'PC_NHORAS_ESTIMADAS': forms.NumberInput(attrs={'class': 'form-control'}),
            'PC_NCOSTO_ESTIMADO': forms.NumberInput(attrs={'class': 'form-control'}),
            'PC_NHORAS_REALES': forms.NumberInput(attrs={'class': 'form-control'}),
            'PC_NCOSTO_REAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'PC_NMARGEN': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formPROYECTO_CLIENTE, self).__init__(*args, **kwargs)
        self.fields['PC_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['PC_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['PC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['PC_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for ETAPA model
class formETAPA(forms.ModelForm):
    class Meta:
        model = ETAPA
        fields = [
            'ET_CCODIGO', 'ET_CNOMBRE', 'ET_CDESCRIPCION', 'ET_PROYECTO', 'ET_FFECHA_INICIO',
            'ET_FFECHA_FIN_ESTIMADA', 'ET_FFECHA_FIN_REAL', 'ET_CESTADO', 'ET_NPRESUPUESTO',
            'ET_COBSERVACIONES'
        ]
        widgets = {
            'ET_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'ET_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'ET_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'ET_PROYECTO': forms.Select(attrs={'class': 'form-control'}),
            'ET_FFECHA_INICIO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ET_FFECHA_FIN_ESTIMADA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ET_FFECHA_FIN_REAL': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ET_CESTADO': forms.TextInput(attrs={'class': 'form-control'}),
            'ET_NPRESUPUESTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'ET_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formETAPA, self).__init__(*args, **kwargs)
        self.fields['ET_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['ET_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['ET_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['ET_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for TAREA_GENERAL model
class formTAREA_GENERAL(forms.ModelForm):
    class Meta:
        model = TAREA_GENERAL
        fields = [
            'TG_CCODIGO', 'TG_CNOMBRE', 'TG_CDESCRIPCION', 'TG_ETAPA', 'TG_FFECHA_INICIO',
            'TG_FFECHA_FIN_ESTIMADA', 'TG_FFECHA_FIN_REAL', 'TG_CESTADO', 'TG_NPRESUPUESTO',
            'TG_COBSERVACIONES', 'TG_BMILESTONE', 'TG_NPROGRESO', 'TG_NDURACION_PLANIFICADA',
            'TG_NDURACION_REAL', 'TG_BCRITICA'
        ]
        widgets = {
            'TG_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'TG_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'TG_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'TG_ETAPA': forms.Select(attrs={'class': 'form-control'}),
            'TG_FFECHA_INICIO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TG_FFECHA_FIN_ESTIMADA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TG_FFECHA_FIN_REAL': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TG_CESTADO': forms.TextInput(attrs={'class': 'form-control'}),
            'TG_NPRESUPUESTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'TG_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'TG_BMILESTONE': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'TG_NPROGRESO': forms.NumberInput(attrs={'class': 'form-control'}),
            'TG_NDURACION_PLANIFICADA': forms.NumberInput(attrs={'class': 'form-control'}),
            'TG_NDURACION_REAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'TG_BCRITICA': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(formTAREA_GENERAL, self).__init__(*args, **kwargs)
        self.fields['TG_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['TG_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['TG_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['TG_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for TAREA_INGENIERIA model
class formTAREA_INGENIERIA(forms.ModelForm):
    class Meta:
        model = TAREA_INGENIERIA
        fields = [
            'TI_CCODIGO', 'TI_CNOMBRE', 'TI_CDESCRIPCION', 'TI_ETAPA', 'TI_FFECHA_INICIO',
            'TI_FFECHA_FIN_ESTIMADA', 'TI_FFECHA_FIN_REAL', 'TI_CESTADO', 'TI_NPRESUPUESTO',
            'TI_COBSERVACIONES', 'TI_BMILESTONE', 'TI_NPROGRESO', 'TI_NDURACION_PLANIFICADA',
            'TI_NDURACION_REAL', 'TG_BCRITICA'
        ]
        widgets = {
            'TI_CCODIGO': forms.TextInput(attrs={'class': 'form-control'}),
            'TI_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'TI_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'TI_ETAPA': forms.Select(attrs={'class': 'form-control'}),
            'TI_FFECHA_INICIO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TI_FFECHA_FIN_ESTIMADA': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TI_FFECHA_FIN_REAL': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TI_CESTADO': forms.TextInput(attrs={'class': 'form-control'}),
            'TI_NPRESUPUESTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'TI_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
            'TI_BMILESTONE': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'TI_NPROGRESO': forms.NumberInput(attrs={'class': 'form-control'}),
            'TI_NDURACION_PLANIFICADA': forms.NumberInput(attrs={'class': 'form-control'}),
            'TI_NDURACION_REAL': forms.NumberInput(attrs={'class': 'form-control'}),
            'TG_BCRITICA': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(formTAREA_INGENIERIA, self).__init__(*args, **kwargs)
        self.fields['TI_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['TI_FFECHA_MODIFICACION'].widget = forms.HiddenInput()

        self.fields['TI_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['TI_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for ADJUNTO_TAREA_GENERAL model
class formADJUNTO_TAREA_GENERAL(forms.ModelForm):
    class Meta:
        model = ADJUNTO_TAREA_GENERAL
        fields = ['AT_TAREA', 'AT_CARCHIVO', 'AT_CNOMBRE', 'AT_CDESCRIPCION']
        widgets = {
            'AT_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AT_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'AT_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'AT_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formADJUNTO_TAREA_GENERAL, self).__init__(*args, **kwargs)
        self.fields['AT_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['AT_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['AT_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ADJUNTO_TAREA_INGENIERIA model
class formADJUNTO_TAREA_INGENIERIA(forms.ModelForm):
    class Meta:
        model = ADJUNTO_TAREA_INGENIERIA
        fields = ['ATI_TAREA', 'ATI_CARCHIVO', 'ATI_CNOMBRE', 'ATI_CDESCRIPCION']
        widgets = {
            'ATI_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'ATI_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'ATI_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'ATI_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formADJUNTO_TAREA_INGENIERIA, self).__init__(*args, **kwargs)
        self.fields['ATI_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['ATI_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['ATI_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ADJUNTO_TAREA_FINANCIERA model
class formADJUNTO_TAREA_FINANCIERA(forms.ModelForm):
    class Meta:
        model = ADJUNTO_TAREA_FINANCIERA
        fields = ['ATF_TAREA', 'ATF_CARCHIVO', 'ATF_CNOMBRE', 'ATF_CDESCRIPCION']
        widgets = {
            'ATF_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'ATF_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'ATF_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'ATF_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formADJUNTO_TAREA_FINANCIERA, self).__init__(*args, **kwargs)
        self.fields['ATF_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['ATF_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['ATF_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ADJUNTO_ETAPA model
class formADJUNTO_ETAPA(forms.ModelForm):
    class Meta:
        model = ADJUNTO_ETAPA
        fields = ['AE_ETAPA', 'AE_CARCHIVO', 'AE_CNOMBRE', 'AE_CDESCRIPCION']
        widgets = {
            'AE_ETAPA': forms.Select(attrs={'class': 'form-control'}),
            'AE_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'AE_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'AE_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formADJUNTO_ETAPA, self).__init__(*args, **kwargs)
        self.fields['AE_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['AE_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['AE_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_EMPLEADO_TAREA_INGENIERIA model
class formASIGNACION_EMPLEADO_TAREA_INGENIERIA(forms.ModelForm):
    class Meta:
        model = ASIGNACION_EMPLEADO_TAREA_INGENIERIA
        fields = ['AE_EMPLEADO', 'AE_TAREA', 'AE_CESTADO']
        widgets = {
            'AE_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'AE_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AE_CESTADO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_EMPLEADO_TAREA_INGENIERIA, self).__init__(*args, **kwargs)
        self.fields['AE_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['AE_FFECHA_FINALIZACION'].widget = forms.HiddenInput()
        self.fields['AE_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_EMPLEADO_TAREA_FINANCIERA model
class formASIGNACION_EMPLEADO_TAREA_FINANCIERA(forms.ModelForm):
    class Meta:
        model = ASIGNACION_EMPLEADO_TAREA_FINANCIERA
        fields = ['AE_EMPLEADO', 'AE_TAREA', 'AE_CESTADO']
        widgets = {
            'AE_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'AE_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AE_CESTADO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_EMPLEADO_TAREA_FINANCIERA, self).__init__(*args, **kwargs)
        self.fields['AE_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['AE_FFECHA_FINALIZACION'].widget = forms.HiddenInput()
        self.fields['AE_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_EMPLEADO_TAREA_GENERAL model
class formASIGNACION_EMPLEADO_TAREA_GENERAL(forms.ModelForm):
    class Meta:
        model = ASIGNACION_EMPLEADO_TAREA_GENERAL
        fields = ['AE_EMPLEADO', 'AE_TAREA', 'AE_CESTADO']
        widgets = {
            'AE_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'AE_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AE_CESTADO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_EMPLEADO_TAREA_GENERAL, self).__init__(*args, **kwargs)
        self.fields['AE_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['AE_FFECHA_FINALIZACION'].widget = forms.HiddenInput()
        self.fields['AE_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA model
class formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA(forms.ModelForm):
    class Meta:
        model = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA
        fields = ['AEC_EMPLEADO', 'AEC_TAREA', 'AEC_CESTADO']
        widgets = {
            'AEC_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'AEC_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AEC_CESTADO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_INGENIERIA, self).__init__(*args, **kwargs)
        self.fields['AEC_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['AEC_FFECHA_FINALIZACION'].widget = forms.HiddenInput()
        self.fields['AEC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA model
class formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA(forms.ModelForm):
    class Meta:
        model = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA
        fields = ['AEC_EMPLEADO', 'AEC_TAREA', 'AEC_CESTADO']
        widgets = {
            'AEC_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'AEC_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AEC_CESTADO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_FINANCIERA, self).__init__(*args, **kwargs)
        self.fields['AEC_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['AEC_FFECHA_FINALIZACION'].widget = forms.HiddenInput()
        self.fields['AEC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL model
class formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL(forms.ModelForm):
    class Meta:
        model = ASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL
        fields = ['AEC_EMPLEADO', 'AEC_TAREA', 'AEC_CESTADO']
        widgets = {
            'AEC_EMPLEADO': forms.Select(attrs={'class': 'form-control'}),
            'AEC_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'AEC_CESTADO': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_EMPLEADO_CONTRATISTA_TAREA_GENERAL, self).__init__(*args, **kwargs)
        self.fields['AEC_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['AEC_FFECHA_FINALIZACION'].widget = forms.HiddenInput()
        self.fields['AEC_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_RECURSO_TAREA_GENERAL model
class formASIGNACION_RECURSO_TAREA_GENERAL(forms.ModelForm):
    class Meta:
        model = ASIGNACION_RECURSO_TAREA_GENERAL
        fields = ['ART_TAREA', 'ART_PRODUCTO', 'ART_CANTIDAD', 'ART_COSTO_UNITARIO']
        widgets = {
            'ART_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'ART_PRODUCTO': forms.Select(attrs={'class': 'form-control'}),
            'ART_CANTIDAD': forms.NumberInput(attrs={'class': 'form-control'}),
            'ART_COSTO_UNITARIO': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_RECURSO_TAREA_GENERAL, self).__init__(*args, **kwargs)
        self.fields['ART_COSTO_TOTAL'].widget = forms.HiddenInput()
        self.fields['ART_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['ART_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_RECURSO_TAREA_INGENIERIA model
class formASIGNACION_RECURSO_TAREA_INGENIERIA(forms.ModelForm):
    class Meta:
        model = ASIGNACION_RECURSO_TAREA_INGENIERIA
        fields = ['ART_TAREA', 'ART_PRODUCTO', 'ART_CANTIDAD', 'ART_COSTO_UNITARIO']
        widgets = {
            'ART_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'ART_PRODUCTO': forms.Select(attrs={'class': 'form-control'}),
            'ART_CANTIDAD': forms.NumberInput(attrs={'class': 'form-control'}),
            'ART_COSTO_UNITARIO': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_RECURSO_TAREA_INGENIERIA, self).__init__(*args, **kwargs)
        self.fields['ART_COSTO_TOTAL'].widget = forms.HiddenInput()
        self.fields['ART_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['ART_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ASIGNACION_RECURSO_TAREA_FINANCIERA model
class formASIGNACION_RECURSO_TAREA_FINANCIERA(forms.ModelForm):
    class Meta:
        model = ASIGNACION_RECURSO_TAREA_FINANCIERA
        fields = ['ART_TAREA', 'ART_PRODUCTO', 'ART_CANTIDAD', 'ART_COSTO_UNITARIO']
        widgets = {
            'ART_TAREA': forms.Select(attrs={'class': 'form-control'}),
            'ART_PRODUCTO': forms.Select(attrs={'class': 'form-control'}),
            'ART_CANTIDAD': forms.NumberInput(attrs={'class': 'form-control'}),
            'ART_COSTO_UNITARIO': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formASIGNACION_RECURSO_TAREA_FINANCIERA, self).__init__(*args, **kwargs)
        self.fields['ART_COSTO_TOTAL'].widget = forms.HiddenInput()
        self.fields['ART_FFECHA_ASIGNACION'].widget = forms.HiddenInput()
        self.fields['ART_CUSUARIO_CREADOR'].widget = forms.HiddenInput()

# Form for ACTA_REUNION model
class formACTA_REUNION(forms.ModelForm):
    class Meta:
        model = ACTA_REUNION
        fields = ['AR_ETAPA', 'AR_CTITULO', 'AR_CFECHA', 'AR_CLUGAR', 'AR_CPARTICIPANTES', 'AR_CAGENDA', 'AR_CCONTENIDO', 'AR_CACUERDOS', 'AR_CARCHIVO']
        widgets = {
            'AR_ETAPA': forms.Select(attrs={'class': 'form-control'}),
            'AR_CTITULO': forms.TextInput(attrs={'class': 'form-control'}),
            'AR_CFECHA': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'AR_CLUGAR': forms.TextInput(attrs={'class': 'form-control'}),
            'AR_CPARTICIPANTES': forms.Textarea(attrs={'class': 'form-control'}),
            'AR_CAGENDA': forms.Textarea(attrs={'class': 'form-control'}),
            'AR_CCONTENIDO': forms.Textarea(attrs={'class': 'form-control'}),
            'AR_CACUERDOS': forms.Textarea(attrs={'class': 'form-control'}),
            'AR_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formACTA_REUNION, self).__init__(*args, **kwargs)
        self.fields['AR_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['AR_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['AR_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['AR_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for PROYECTO_ADJUNTO model
class formPROYECTO_ADJUNTO(forms.ModelForm):
    class Meta:
        model = PROYECTO_ADJUNTO
        fields = ['PA_PROYECTO', 'PA_CNOMBRE', 'PA_CDESCRIPCION', 'PA_CARCHIVO', 'PA_CTIPO']
        widgets = {
            'PA_PROYECTO': forms.Select(attrs={'class': 'form-control'}),
            'PA_CNOMBRE': forms.TextInput(attrs={'class': 'form-control'}),
            'PA_CDESCRIPCION': forms.Textarea(attrs={'class': 'form-control'}),
            'PA_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'PA_CTIPO': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formPROYECTO_ADJUNTO, self).__init__(*args, **kwargs)
        self.fields['PA_FFECHA_SUBIDA'].widget = forms.HiddenInput()
        self.fields['PA_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['PA_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['PA_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for BOLETA_GARANTIA model
class formBOLETA_GARANTIA(forms.ModelForm):
    class Meta:
        model = BOLETA_GARANTIA
        fields = ['BG_PROYECTO', 'BG_CNUMERO', 'BG_CMONTO', 'BG_CENTIDAD_EMISORA', 'BG_FFECHA_EMISION', 'BG_FFECHA_VENCIMIENTO', 'BG_CESTADO', 'BG_CARCHIVO', 'BG_COBSERVACIONES']
        widgets = {
            'BG_PROYECTO': forms.Select(attrs={'class': 'form-control'}),
            'BG_CNUMERO': forms.TextInput(attrs={'class': 'form-control'}),
            'BG_CMONTO': forms.NumberInput(attrs={'class': 'form-control'}),
            'BG_CENTIDAD_EMISORA': forms.TextInput(attrs={'class': 'form-control'}),
            'BG_FFECHA_EMISION': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'BG_FFECHA_VENCIMIENTO': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'BG_CESTADO': forms.Select(attrs={'class': 'form-control'}),
            'BG_CARCHIVO': forms.FileInput(attrs={'class': 'form-control'}),
            'BG_COBSERVACIONES': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(formBOLETA_GARANTIA, self).__init__(*args, **kwargs)
        self.fields['BG_FFECHA_CREACION'].widget = forms.HiddenInput()
        self.fields['BG_FFECHA_MODIFICACION'].widget = forms.HiddenInput()
        self.fields['BG_CUSUARIO_CREADOR'].widget = forms.HiddenInput()
        self.fields['BG_CUSUARIO_MODIFICADOR'].widget = forms.HiddenInput()

# Form for TAREA_GENERAL_DEPENDENCIA model
class formTAREA_GENERAL_DEPENDENCIA(forms.ModelForm):
    class Meta:
        model = TAREA_GENERAL_DEPENDENCIA
        fields = ['TD_TAREA_PREDECESORA', 'TD_TAREA_SUCESORA', 'TD_TIPO_DEPENDENCIA']
        widgets = {
            'TD_TAREA_PREDECESORA': forms.Select(attrs={'class': 'form-control'}),
            'TD_TAREA_SUCESORA': forms.Select(attrs={'class': 'form-control'}),
            'TD_TIPO_DEPENDENCIA': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for TAREA_FINANCIERA_DEPENDENCIA model
class formTAREA_FINANCIERA_DEPENDENCIA(forms.ModelForm):
    class Meta:
        model = TAREA_FINANCIERA_DEPENDENCIA
        fields = ['TD_TAREA_PREDECESORA', 'TD_TAREA_SUCESORA', 'TD_TIPO_DEPENDENCIA']
        widgets = {
            'TD_TAREA_PREDECESORA': forms.Select(attrs={'class': 'form-control'}),
            'TD_TAREA_SUCESORA': forms.Select(attrs={'class': 'form-control'}),
            'TD_TIPO_DEPENDENCIA': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for TAREA_INGENIERIA_DEPENDENCIA model
class formTAREA_INGENIERIA_DEPENDENCIA(forms.ModelForm):
    class Meta:
        model = TAREA_INGENIERIA_DEPENDENCIA
        fields = ['TD_TAREA_PREDECESORA', 'TD_TAREA_SUCESORA', 'TD_TIPO_DEPENDENCIA']
        widgets = {
            'TD_TAREA_PREDECESORA': forms.Select(attrs={'class': 'form-control'}),
            'TD_TAREA_SUCESORA': forms.Select(attrs={'class': 'form-control'}),
            'TD_TIPO_DEPENDENCIA': forms.Select(attrs={'class': 'form-control'}),
        }
