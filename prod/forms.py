from django import forms
from .models import Marca,TipoProducto,Categoria,Producto

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['id','nombre','estado']
        labels = {'nombre':'Nombre Marca','estado':'Estado'}
        widget = {'id':forms.HiddenInput,'nombre':forms.TextInput,
                'estado': forms.CheckboxInput }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class CategoriaForm(forms.ModelForm):    
    class Meta:
        model = Categoria
        fields = ['id','nombre','estado']
        labels = {'nombre':'Nombre','estado':'Estado'}
        widget = {'id':forms.HiddenInput,'nombre':forms.TextInput,
                'estado': forms.CheckboxInput }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id','empresa','categoria','tipo_producto','numero_parte','codigo_proveedor',
                'codigo_interno','codigo_sunat','marca','nombre','detalle','imagen',
                'afecto_igv','estado']
        labels = {'empresa':'Empresa','categoria':'Categoría','tipo_producto':'Tipo Producto',
                    'estado':'Estado'}
        widget = {'id':forms.HiddenInput,'categoria':forms.Select,'empresa':forms.Select,'marca':forms.Select,
                    'tipo_producto':forms.Select,'estado':forms.CheckboxInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)