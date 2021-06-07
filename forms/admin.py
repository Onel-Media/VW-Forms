from django.contrib import admin
from .models import SUVW_Encuesta, SUVW_Privacidad, SUVW_Privacidad_2, SUVW_Carta_Responsiva, TextArticle

# Register your models here.
admin.site.register(SUVW_Encuesta)
admin.site.register(SUVW_Privacidad)
admin.site.register(SUVW_Privacidad_2)
admin.site.register(SUVW_Carta_Responsiva)
admin.site.register(TextArticle)
