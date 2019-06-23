from django.urls import path
from . import views

urlpatterns = [
    path('', views.personage, name='personage'),

    path('personage/', views.personage, name='personage'),
    path('personage/new/', views.personage_new, name='personage_new'),
    path('personage/<int:id>/edit', views.personage_detail, name='personage_datail'),
    path('personage/<int:id>/delete', views.personage_delete, name='personage_delete'),

    path('inventory/', views.inventory, name='inventory'),
    path('inventory/new/', views.inventory_new, name='inventory_new'),
    path('inventory/<int:id>/edit', views.inventory_detail, name='inventory_detail'),
    path('inventory/<int:id>/delete', views.inventory_delete, name='inventory_delete'),

    path('personagetransfer/', views.personagetransfer, name='personagetransfer'),
    path('personagetransfer/new', views.personagetransfer_new, name='personagetransfer_new'),
    path('personagetransfer/<int:id>/edit', views.personagetransfer_detail, name='personagetransfer_detail'),
    path('personagetransfer/<int:id>/delete', views.personagetransfer_delete, name='personagetransfer_delete'),
]