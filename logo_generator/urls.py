# logo_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('canva/auth/', views.canva_auth, name='canva_auth'),
    path('canva/callback/', views.canva_callback, name='canva_callback'),
    path('canva/fetch-templates/', views.fetch_templates, name='fetch_templates'),
    path('canva/import-design/<str:template_id>/', views.import_design, name='import_design'),
]
