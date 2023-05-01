from rest_framework import viewsets, permissions

from .models import project

from .serializers import ProjectSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    
    queryset = project.objects.all()

    permission_classes = [permissions.AllowAny]

    serializer_class = ProjectSerializer