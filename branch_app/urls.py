from django.urls import path
from . import views

app_name = 'branch_app'

urlpatterns = [
    path('ekm_branch/',views.ekm_branch,name='ekm_branch'),
    path('tvm_branch/', views.tvm_branch, name='tvm_branch'),
    path('klm_branch/', views.klm_branch, name='klm_branch'),
    path('ktm_branch/', views.ktm_branch, name='ktm_branch'),
    path('tsr_branch/', views.tsr_branch, name='tsr_branch'),
]