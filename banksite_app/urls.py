from django.urls import path
from . import views

app_name = 'banksite_app'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_branches, name='ajax_load_branches'),
    path('success/', views.success, name='success'),

]