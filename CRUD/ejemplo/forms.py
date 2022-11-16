from django.forms import ModelForm,TextInput,DateInput,TimeInput,Select
from .models import *

class ClienteForm(ModelForm):
    class Meta:
        model = cliente
        #Fields = Campos
        fields = '__all__'

class CitasForm(ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'
        widgets = {
            'cliente':Select(attrs={'class':'form-control'}),
            'especialidad':TextInput(attrs={'class':'form-control'}),
            'especialista':TextInput(attrs={'class':'form-control'}),
            'fecha':DateInput(attrs={'type':'date','class':'form-control'}),
            'lugar':TextInput(attrs={'class':'form-control'}),
            'hora':TimeInput(attrs={'class':'form-control','type':'time'}),
            'observaciones':TextInput(attrs={'class':'form-control'}),
        }


