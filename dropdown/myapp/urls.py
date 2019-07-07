from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('ajax/load-fetchState/', views.load_fetchState, name = 'ajax_load_fetchState'),
]