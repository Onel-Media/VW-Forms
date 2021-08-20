from django import forms
from .models import SUVW_Encuesta, SUVW_Privacidad, SUVW_Privacidad_2, SUVW_Carta_Responsiva


class EncuestaForm(forms.ModelForm):
    CHOICES_CALIFICACION = [
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
        ('70', '70'),
        ('80', '80'),
        ('90', '90'),
        ('100', '100'),
    ]
    q1_calificacion_del_lugar = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q2_calificacion_del_duracion = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q3_calificacion_del_contenido_presentaciones = forms.ChoiceField(
        widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q4_calificacion_del_informacion_interaccion = forms.ChoiceField(
        widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q5_calificacion_general = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q6_comentarios = forms.Textarea()

    class Meta:
        model = SUVW_Encuesta
        fields = (
            'q1_calificacion_del_lugar',
            'q2_calificacion_del_duracion',
            'q3_calificacion_del_contenido_presentaciones',
            'q4_calificacion_del_informacion_interaccion',
            'q5_calificacion_general',
            'q6_comentarios',
        )
        widgets = {
            'q1_calificacion_del_lugar': forms.RadioSelect,
            'q2_calificacion_del_duracion': forms.RadioSelect,
            'q3_calificacion_del_contenido_presentaciones': forms.RadioSelect,
            'q4_calificacion_del_informacion_interaccion': forms.RadioSelect,
            'q5_calificacion_general': forms.RadioSelect,
        }


class PrivacidadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=149)
    apellido = forms.CharField(max_length=149)
    acepto_terminos = forms.BooleanField()

    class Meta:
        model = SUVW_Privacidad
        fields = (
            'nombre',
            'apellido',
            'acepto_terminos',
        )


class Privacidad2Form(forms.ModelForm):
    nombre = forms.CharField(max_length=149)
    apellido = forms.CharField(max_length=149)
    acepto_terminos = forms.BooleanField()

    class Meta:
        model = SUVW_Privacidad
        fields = (
            'nombre',
            'apellido',
            'acepto_terminos',
        )


class ResponsivaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=149)
    apellido = forms.CharField(max_length=149)
    acepto_terminos = forms.BooleanField()

    class Meta:
        model = SUVW_Privacidad
        fields = (
            'nombre',
            'apellido',
            'acepto_terminos',
        )


##
# Nuevo Jetta Forms
##
class NJEncuestaForm(forms.ModelForm):
    CHOICES_CALIFICACION = [
        ('100', '100'), ('90', '90'), ('80', '80'), ('70', '70'), ('60', '60'), ('50', '50'), ('40', '40'), ('30', '30'), ('20', '20'), ('10', '10'),
    ]
    q1_calificacion_del_formato = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q2_calificacion_de_medidas_sanidad = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q3_calificacion_de_duracion = forms.ChoiceField(
        widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q4_calificacion_de_presentacion_producto = forms.ChoiceField(
        widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q5_calificacion_general_experiencia = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES_CALIFICACION))
    q6_comentarios = forms.Textarea()


class NJRegistroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=149)
    apellido = forms.CharField(max_length=149)
    acepto_recepcion_giveaway = forms.BooleanField()
    acepto_uso_imagen = forms.BooleanField()
    acepto_terminos_privacidad = forms.BooleanField()

    class Meta:
        model = SUVW_Privacidad
        fields = (
            'nombre',
            'apellido',
            'acepto_uso_imagen',
            'acepto_terminos_privacidad',
            'acepto_recepcion_giveaway',
        )
