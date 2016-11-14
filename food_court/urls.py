from django.conf.urls import url
from django.contrib import admin
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index' ), #/
    url(r'^login$', login , name='login' ),
    url(r'^logout$', logout, name = 'logout' ),
    url(r'^registrar$', registrar_usuario, name='registrar-usuario' ),
    url(r'^registrar-cliente$', registrar_cliente, name='registrar-cliente' ),
    url(r'^principal$', principal , name='principal' ),
    url(r'^restaurante$', restaurante , name='restaurante' ),

]
