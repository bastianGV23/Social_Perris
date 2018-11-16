"""MisPerris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.formulario.views import formulario_view
from apps.principal.views import IndexView,LogOut
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^formulario/', formulario_view, name='contacto'),
    url(r'^rescate/', include(('apps.rescate.urls','rescate'),namespace='rescate')),
    url(r'^adopcion/', include(('apps.adopcion.urls','adopcion'),namespace='adopcion')),
    url('', include('social.apps.django_app.urls', namespace='social')), 
    url(r'^salir/$', LogOut),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
