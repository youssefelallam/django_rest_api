from rest_framework import serializers
from .models import Filier, Students

class FilierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Filier
        fields = '__all__'

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'