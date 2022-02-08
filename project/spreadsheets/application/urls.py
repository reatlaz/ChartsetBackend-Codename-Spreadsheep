"""spreadsheets URL Configuration

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
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from chartsets.views import ChartsetViewSet, сhs_search
from users.views import usr_search

from django.contrib.auth import views as auth_views
from chartsets import views as views

router = DefaultRouter()
router.register(r'api/chartsets', ChartsetViewSet, basename='chartsets')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chartsets/', include('chartsets.urls')),
    path('users/', include('users.urls')),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
    path('', views.home, name='home'),
    path('api/search/chartsets', сhs_search, name='chartsets_search'),
    path('api/search/users', usr_search, name='users_search'),
]


urlpatterns += router.urls
