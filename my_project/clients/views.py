from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, Client, Project
from .serializers import UserSerializer, ClientSerializer, ProjectSerializer, ProjectCreateSerializer

# API View for Listing and Creating Users
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# API View for Retrieving, Updating, and Deleting a Specific User
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create a new client or list all clients
class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Retrieve, update, or delete a client
class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

# Create a new project for a specific client
class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, args, kwargs):
        client_id = self.kwargs.get('client_id')
        client = get_object_or_404(Client, id=client_id)
        serializer = self.get_serializer(data=request.data, context={'client': client, 'created_by': request.user})
        if serializer.is_valid():
            project = serializer.save()
            output_serializer = ProjectSerializer(project)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all projects assigned to the logged-in user
class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
