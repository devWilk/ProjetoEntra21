"""meu_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pipes import Template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from cliente.views import clientes
from django.conf import settings
from django.conf.urls.static import static
from curso.views import listar_cursos , cadastrar_curso , excluir_curso , alterar_curso

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('inicio',TemplateView.as_view(template_name='index.html'),name='inicio'),
    path('clientes',clientes ,name='clientes'),
    path('padrao',TemplateView.as_view(template_name='base.html')),
    path('professores',TemplateView.as_view(template_name='professores.html'),name='professores'),
    path('alunos',TemplateView.as_view(template_name='alunos.html'),name='alunos'),
    path('alterar-curso/<int:id>',alterar_curso,name='alterar-curso'),
    path('excluir-curso/<int:id>',excluir_curso,name='excluir-curso'),
    path('cadastra-curso',cadastrar_curso,name='cadastrar-cursos'),
    path('cursos',listar_cursos,name='cursos'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
