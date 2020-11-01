from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['ruc','razon_social','nombre_comercial','direccion_principal','ubigeo',
            'pagina_web','usuario_sol','clave_sol','certificado_pfx','fecha_caduca_certificado',
            'certificado_zip','clave_certificado','texto_encabezado','logo','imagen_pie_pagina',
            'estado']
        labels = {'ruc':'R.U.C.','razon_social':'Razón Social','nombre_comercial':'Nombre Comercial',
            'direccion_principal':'Dirección Principal','ubigeo':'Ubigeo','pagina_web':'Página Web',
            'usuario_sol':'Usuario Sol','clave_sol':'Clave Sol','certificado_pfx':'certificado Pfx',
            'fecha_caduca_certificado':'Fecha Caduca Certificado','certificado_zip':'Certificado Zip',
            'clave_certificado':'Clave Certificado','texto_encabezado':'Texto Encabezado',
            'logo':'Logo','imagen_pie_pagina':'Imagen Pie Página','estado':'Estado'}
        widget = {'ruc':forms.TextInput,'razon_social': forms.TextInput,
                'nombre_comercial': forms.TextInput, 'direccion_principal': forms.TextInput,
                'ubigeo': forms.TextInput, 'pagina_web':forms.URLInput,
                'usuario_sol': forms.TextInput, 'clave_sol': forms.TextInput,
                'certificado_pfx' : forms.FileInput,'clave_certificado': forms.TextInput,
                'texto_encabezado': forms.TextInput,'logo':forms.FileInput,
                'imagen_pie_pagina': forms.FileInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })