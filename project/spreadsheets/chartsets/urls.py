from django.contrib import admin
from django.urls import path
from chartsets.views import chartset_detail, home, create_chartset, list_chartsets, edit_chartset, delete_chartset

urlpatterns = [
    path('<int:chartset_id>/', chartset_detail, name='chartset_detail'),
    path('<int:chartset_id>/edit/', edit_chartset, name='edit_chartset'),
    path('<int:chartset_id>/delete/', delete_chartset, name='delete_chartset'),
    path('create_chartset/', create_chartset, name='create_chartset'),
    path('list/', list_chartsets, name='list_chartsets'),
    path('home/', home, name='home'),
]