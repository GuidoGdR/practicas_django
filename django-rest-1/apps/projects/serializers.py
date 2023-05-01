from rest_framework import serializers

from .models import project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project

        fields = ('title', 'description', 'technology', 'created_date')

        read_only_fields = ('created_date',)