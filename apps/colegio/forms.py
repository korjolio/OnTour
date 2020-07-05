from django import forms
from .models import Contrato

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['fecha_contrato', 'adjunto_contrato', 'institucion_id', 'vendedor_id', 'seguro_id', 'monto']