from django.shortcuts import render
from django.views.generic import CreateView
from .models import SUVW_Encuesta, SUVW_Privacidad, SUVW_Privacidad_2, SUVW_Carta_Responsiva, TextArticle
from .forms import EncuestaForm, PrivacidadForm, Privacidad2Form, ResponsivaForm


# Create your views here.
def suvm_landing(request):
    return render(request, 'spa/forms/suvw/landing.html')


class SUVM_EncuestaCreateView(CreateView):
    model = SUVW_Encuesta
    fields = (
        'q1_calificacion_del_lugar',
        'q2_calificacion_del_duracion',
        'q3_calificacion_del_contenido_presentaciones',
        'q4_calificacion_del_informacion_interaccion',
        'q5_calificacion_general',
    )
    form = EncuestaForm
    template_name = 'spa/forms/suvw/encuesta.html'
    success_url = '../'


class SUVM_PrivacidadCreateView(CreateView):
    model = SUVW_Privacidad
    fields = (
        'nombre',
        'apellido',
        'acepto_terminos',
    )
    form = PrivacidadForm
    template_name = 'spa/forms/suvw/privacidad.html'
    success_url = '../'

    def get_context_data(self, **kwargs):
        et = super(SUVM_PrivacidadCreateView, self).get_context_data(**kwargs)
        et['article'] = TextArticle.objects.get(key="privacidad")
        return et


class SUVM_Privacidad2CreateView(CreateView):
    model = SUVW_Privacidad_2
    fields = (
        'nombre',
        'apellido',
        'acepto_terminos',
    )
    form = PrivacidadForm
    template_name = 'spa/forms/suvw/privacidad.html'
    success_url = '../'

    def get_context_data(self, **kwargs):
        et = super(SUVM_Privacidad2CreateView, self).get_context_data(**kwargs)
        et['article'] = TextArticle.objects.get(key="privacidad2")
        return et


class SUVM_ResponsivaCreateView(CreateView):
    model = SUVW_Carta_Responsiva
    fields = (
        'nombre',
        'apellido',
        'acepto_terminos',
    )
    form = PrivacidadForm
    template_name = 'spa/forms/suvw/privacidad.html'
    success_url = '../'

    def get_context_data(self, **kwargs):
        et = super(SUVM_ResponsivaCreateView, self).get_context_data(**kwargs)
        et['article'] = TextArticle.objects.get(key="responsiva")
        return et
