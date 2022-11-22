from rest_framework import serializers
from teste_backend.models import Campos


class CamposSerializers(serializers.ModelSerializer):
    class Meta:
        model = Campos
        fields = "__all__"

    def create(self, validated_data):
        return Campos.objects.create(**validated_data)


class CamposUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ["file"]


class CamposListSerializer(serializers.Serializer):
    loja = serializers.CharField(read_only=True)
    tipo = serializers.CharField(read_only=True)
    valor = serializers.CharField(read_only=True)
