from apps.rescate.views import lista_rescate,crea_rescate,edita_rescate,elimina_rescate
from django.conf.urls import url,include

urlpatterns = [
    url(r'^ver$', lista_rescate, name='ver'),
    url(r'^crea$', crea_rescate, name='crea'),
    url(r'^modifica/(?P<id_perrito>\d+)/$', edita_rescate, name='edita'),
    url(r'^delete/(?P<id_perrito>\d+)/$', elimina_rescate, name='r_delete'),
]