from django.urls import path
from .views import suvm_landing, SUVM_EncuestaCreateView, SUVM_PrivacidadCreateView, SUVM_Privacidad2CreateView, SUVM_ResponsivaCreateView

urlpatterns = [
    path('encuesta/', SUVM_EncuestaCreateView.as_view(), name='encuesta'),
    path('privacidad/', SUVM_PrivacidadCreateView.as_view(), name='privacidad'),
    path('privacidad-2/', SUVM_Privacidad2CreateView.as_view(), name='privacidad-2'),
    path('responsiva/', SUVM_ResponsivaCreateView.as_view(), name='responsiva'),
    path('', suvm_landing, name='suvw-landing'),path('', suvm_landing, name='landing'),
]