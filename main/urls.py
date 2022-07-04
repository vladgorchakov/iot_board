from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.MonListView.as_view(), name='mon-list'),
    path('new/', views.MonCreateView.as_view(), name='mon-create'),
    path('<int:pk>/delete', views.MonDeleteView.as_view(), name='mon-del'),
]
