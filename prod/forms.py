from django import forms
from .models import Marca,TipoProducto,Categoria,Producto
from .models import ProductoPrecio,ProductoPreparado

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
                    'numero_parte':'Número Parte','codigo_proveedor':'Código Proveedor',
                    'codigo_interno':'Código Interno','codigo_sunat':'Código Sunat',
                    'nombre':'Nombre Producto','detalle':'Detalle Producto',
                    'imagen':'Imagen Producto','afecto_igv':'Igv Afecto',
                    'estado':'Estado'}
        widget = {'id':forms.HiddenInput,'categoria':forms.Select,'empresa':forms.Select,'marca':forms.Select,
                    'numero_parte':forms.TextInput,'codigo_proveedor':forms.TextInput,
                    'codigo_interno':forms.TextInput,'codigo_sunat':forms.TextInput,
                    'nombre':forms.TextInput,'detalle':forms.Textarea(attrs={'rows':1}),
                    'imagen':forms.FileInput,'afecto_igv':forms.CheckboxInput,
                    'tipo_producto':forms.Select,'estado':forms.CheckboxInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

class ProductoPreparadoForm(forms.ModelForm):
    class Meta:
        model = ProductoPreparado
        fields = ['id','producto','compuesto','descripcion','estado']
        labels = {'producto':'Producto','compuesto':'Compuesto','descripcion':'Descripción',
                    'estado':'Estado'}
        widget = {'id':forms.HiddenInput,'producto':forms.Select,'compuesto':forms.TextInput,
                    'descripcion':forms.TextInput,'estado':forms.CheckboxInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)