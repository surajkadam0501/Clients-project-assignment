from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView, ProjectCreateAPIView, ProjectListAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
]
