"""outlab_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic.base import TemplateView 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('accounts/', include('accounts.urls'),name='accounts_app'),
    path('accounts/', include('django.contrib.auth.urls'),name='accounts_auth'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('explore/',views.explore,name='explore'),
    path('my_profile',views.show_profile,name='my_profile'),
    path('update/',views.update_profile,name='update'),
    path('explore/<str:user_name>',views.explore_profile,name='explore_profile')
]
