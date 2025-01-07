from django.urls import path
from . import views

urlpatterns = [
    path('', views.TareaListView.as_view(), name='tarea_list'),
    path('create/', views.TareaCreateView.as_view(), name='tarea_create'),
    path('detail/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detail'),
    path('delete/<int:pk>/', views.TareaDeleteView.as_view(), name='tarea_delete'),
    path('update/<int:pk>/', views.TareaUpdateView.as_view(), name='tarea_update')
    
]
