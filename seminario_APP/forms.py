from django import forms
from .models import Inscrito, Institucion
import re  # Para las expresiones regulares

class InscritoForm(forms.ModelForm):
    nueva_institucion = forms.CharField(
        required=False,
        label="Nueva Institución",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: INACAP'}),
    )

    class Meta:
        model = Inscrito
        fields = '__all__'
        widgets = {
            'nombre_institucion': forms.Select(attrs={'class': 'form-control'}),
            'numero_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '30'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'persona_que_inscribe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Pérez'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_numero_personas(self):
        numero_personas = self.cleaned_data.get('numero_personas')
        if not isinstance(numero_personas, int) or numero_personas < 1 or numero_personas > 30:
            raise forms.ValidationError("El número de personas debe ser un número entero entre 1 y 30.")
        return numero_personas

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\d{8}$', telefono):
            raise forms.ValidationError("El número de teléfono debe contener exactamente 8 dígitos.")
        if not telefono.startswith('+569'):
            telefono = f"+569{telefono}"
        return telefono

    def clean_persona_que_inscribe(self):
        persona = self.cleaned_data.get('persona_que_inscribe')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', persona):
            raise forms.ValidationError("El nombre debe contener solo letras y espacios.")
        return persona

    def save(self, commit=True):
        # Crear una institución si el campo nueva_institucion tiene valor
        nueva_institucion = self.cleaned_data.get('nueva_institucion')
        if nueva_institucion:
            institucion, created = Institucion.objects.get_or_create(nombre=nueva_institucion)
            self.instance.nombre_institucion = institucion
        return super().save(commit=commit)
    
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la institución'}),
        }