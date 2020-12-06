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
