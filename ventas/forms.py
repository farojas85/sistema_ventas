from django import forms
from .models import ComprobanteVenta

class ComprobanteVentaForm(forms.ModelForm):
    class Meta:
        model = ComprobanteVenta
        fields = [
            'sucursal','tipo_comprobante','serie_comprobante','numero_comprobante',
            'fecha','forma_pago']
        labels = {
            'sucursal':'Sucursal', 'tipo_comprobante':'Tipo Comprobante',
            'serie_comprobante':'Serie','numero_comprobante':'Número',
            'fecha':'Fecha','forma_pago':'Forma Pago'}
        widget = {
            'sucursal':forms.Select, 'tipo_comprobante':forms.Select,
            'serie_comprobante':forms.TextInput,'numero_comprobante': forms.TextInput,
            'fecha' : forms.DateInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })