"""fic_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.views import home

urlpatterns = [
	#URLs Gerais
	path('', home, name='home'),
	path('admin/', admin.site.urls),

	#URL do perfil
	path('perfil/', perfil, name='perfil'),

	#URLs de registro de Usuário
	path('registro/', registro, name='registro'),
	path('dados/<int:id>/', dados, name='dados'),

	#Autenticação
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #URLs de Área
    path('areas/', areas_listar, name='areas'),
    path('area_cadastrar/', area_cadastrar, name='area_cadastrar'),
    path('area_atualizar/<int:id>', area_atualizar, name='area_atualizar'),
    path('area_remover/<int:id>', area_remover, name='area_remover'),

    #URLs de Públicos
    path('publicos/', publicos_listar, name='publicos'),
    path('publico_cadastrar/', publico_cadastrar, name='publico_cadastrar'),
    path('publico_atualizar/<int:id>', publico_atualizar, name='publico_atualizar'),
    path('publico_remover/<int:id>', publico_remover, name='publico_remover'),

    #URLs de Cursos
    path('cursos/', cursos_listar, name='cursos'),
    path('curso_cadastrar/', curso_cadastrar, name='curso_cadastrar'),
    path('curso_atualizar/<int:id>', curso_atualizar, name='curso_atualizar'),
    path('curso_remover/<int:id>', curso_remover, name='curso_remover'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)