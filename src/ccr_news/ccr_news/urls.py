"""ccr_news URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from news.views import *
from rest_framework import routers

router_new = routers.SimpleRouter()
router_new.register(r"news", NewsViewSets)

router_type = routers.SimpleRouter()
router_type.register(r"types", NewTypeViewSets)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router_new.urls)),
    path("api/v1/", include(router_type.urls)),
    path("api/v1/getnews/<int:pk>/", GetNews.as_view()),
    path("api/v1/allnews/", AllNews.as_view())
]
