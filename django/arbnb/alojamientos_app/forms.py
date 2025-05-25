from django import forms
from .models import Alojamiento, Alquiler
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class RegistroUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields



class AlojamientoForm(forms.ModelForm):
    
    class Meta:
        model = Alojamiento

        fields=['descripcion', 'precio'] 
        # No mostramos el campo usuario
        exclude=['usuario']
        widget = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),        
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }


class AlquilerForm(forms.ModelForm):

    class Meta:
        model = Alquiler

        fields=['alojamiento','desde','hasta']
        widgets = {
            'alojamiento': forms.Select(attrs={'class': 'form-control'}),           
            'desde': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'hasta': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alojamiento'].queryset = Alojamiento.objects.all()
        self.fields['alojamiento'].label_from_instance = lambda obj: f"{obj.descripcion}"


class ComentarioAlquilerForm(forms.ModelForm): 
    class Meta:
        model = Alquiler
        fields = ['comentario'] 
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
