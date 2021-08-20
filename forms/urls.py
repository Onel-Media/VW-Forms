from django.urls import path
from .views import suvm_landing, SUVM_EncuestaCreateView, SUVM_PrivacidadCreateView, SUVM_Privacidad2CreateView, \
    SUVM_ResponsivaCreateView, NJ_RegistroCreateView, NJ_EncuestaCreateView, nj_landing, nj_avisos

urlpatterns = [
    # path('encuesta/', SUVM_EncuestaCreateView.as_view(), name='encuesta'),
    # path('privacidadyusodeimagen/', SUVM_PrivacidadCreateView.as_view(), name='privacidad'),
    # path('privacidad/', SUVM_Privacidad2CreateView.as_view(), name='privacidad-2'),
    # path('responsiva/', SUVM_ResponsivaCreateView.as_view(), name='responsiva'),
    # path('', suvm_landing, name='suvw-landing'),path('', suvm_landing, name='landing'),
    path('encuesta/', NJ_EncuestaCreateView.as_view(), name='encuesta'),
    path('registro/', NJ_RegistroCreateView.as_view(), name='registro'),
    path('avisos/', nj_avisos, name='avisos'),
    path('', nj_landing, name='suvw-landing'), path('', suvm_landing, name='landing'),
]
