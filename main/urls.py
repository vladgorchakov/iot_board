from django.urls import path, include
from main import views

urlpatterns = [
    path('monitoring/', views.show_monitoring, name='show_monitoring'),
    path('monitoring/<int:mon_id>', views.show_info, name='show_info'),
    path('monitoring/new', views.take_info, name='take_info')
]
