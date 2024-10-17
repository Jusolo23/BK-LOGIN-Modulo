from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Sesiones


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesiones
        fields = ('id_sesion', 'usuario_ip', 'estado', 'datos_sesion')
        read_only_fields = ('usuario_ip',)

    def create(self, validated_data):
        request = self.context.get('request')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        validated_data['usuario_ip'] = ip
        return Sesiones.objects.create(**validated_data)
