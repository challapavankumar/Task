from rest_framework import serializers
from .models import Task


class Task_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=("__all__")
