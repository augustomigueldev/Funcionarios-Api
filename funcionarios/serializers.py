from rest_framework import serializers
from .models import Funcionario, Cargo

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
