from .views import lista_adopcion,asignar_adopcion,adopta_perro
from django.conf.urls import url,include

urlpatterns = [
    url(r'^ver$', lista_adopcion, name='ver'),
    url(r'^asignar$', asignar_adopcion, name='asignar'),
    url(r'^adopta/(?P<id_adopcion>\d+)/$', adopta_perro, name='adopta'),
]