"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pages.views import (
    index,
    about,
    article_detail,
    contact,
    article_create,
    article_update,
    register
)

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path(
        'contact/',
        contact,
        name='contact'
    ),
    path(
        'article/<int:pk>/',
        article_detail,
        name='article_detail'
    ),
    path(
     'article/create/',
      article_create,
      name='article_create'
    ),
    path(
      'accounts/',
      include('django.contrib.auth.urls')
    ),
    path(
        'article/<int:pk>/edit/',
        article_update,
        name='article_update'
    ),
    path(
        'accounts/register/',
        register,
        name='register'
    ),
    
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )