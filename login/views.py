import requests
import msal
import json
import re
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth.models import User
from login import serializers

# Función para construir app de msal (microsoft)


def _build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        settings.MSAL_CONFIG['CLIENT_ID'],
        authority=settings.MSAL_CONFIG['AUTHORITY'],
        client_credential=settings.MSAL_CONFIG['CLIENT_SECRET'],
        token_cache=cache
    )

# Función para ingresar


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        recaptcha_token = data.get('recaptchaToken')

        # Verificación del reCAPTCHA
        recaptcha_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_token
            }
        )
        recaptcha_result = recaptcha_response.json()

        # Verificación fallida de reCAPTCHA
        if not recaptcha_result.get('success'):
            return JsonResponse({"error": "reCAPTCHA no válido."}, safe=False, status=status.HTTP_400_BAD_REQUEST)

        # Verificación de campos
        if not username or not password:
            return JsonResponse({"error": "Se requiere nombre de usuario y contraseña."}, safe=False, status=status.HTTP_400_BAD_REQUEST)

        # Lógica de validación de usuario
        user_type = validar_usuario(username)
        if user_type == 'interno':
            app = _build_msal_app()

            result = app.acquire_token_by_username_password(
                username=f"{username}@unp.gov.co",
                password=password,
                scopes=settings.MSAL_CONFIG['SCOPE']
            )

            if 'access_token' in result:
                guardar_sesion(request, "Inicio de sesion exitoso", "Exitoso")
                return JsonResponse({'access_token': result['access_token']})
            else:
                guardar_sesion(request, "Credenciales incorrectas", "Fallido")
                return JsonResponse({'error': "Credenciales incorrectas"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)

        elif user_type == 'externo':
            guardar_sesion(request, "Usuario externo", "Exitoso")
            return JsonResponse(
                {"message": "Usuario externo"}, safe=False, status=status.HTTP_200_OK)

        elif user_type == 'invalido':
            guardar_sesion(request, "Usuario no válido", "Fallido")
            return JsonResponse(
                {"error": "Usuario no valido o no existe"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)

    return JsonResponse({"error": "Método no permitido."}, safe=False, status=status.HTTP_501_NOT_IMPLEMENTED)

# Función para salir


@api_view(['POST'])
def logout(request):
    auth_header = request.headers.get('Authorization', None)

    if not auth_header:
        return Response({"error": "No se proporcionó token de autorización."}, safe=False, status=status.HTTP_400_BAD_REQUEST)

    access_token = auth_header.split(' ')[1]

    revoke_url = f"{settings.MSAL_CONFIG['AUTHORITY']}/oauth2/v2.0/logout"

    response = requests.post(revoke_url, headers={
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    })

    if response.status_code != 200:
        return Response({"error": "No se pudo revocar el token."}, safe=False, status=response.status_code)

    return Response({"message": "Logout exitoso."}, safe=False, status=status.HTTP_200_OK)


def obtener_datos(access_token):
    graph_url = 'https://graph.microsoft.com/v1.0/me'
    response = requests.get(
        graph_url, headers={'Authorization': f'Bearer {access_token}'})

    if response.status_code == 200:
        return response

    return JsonResponse({"error": "No se pudo obtener datos del usuario."}, status=response.status_code)

# Función para guardar la sesión


def guardar_sesion(request, datos_sesion, estado):
    sesion_serializer = serializers.SesionSerializer(data={
        'estado': estado,
        'datos_sesion': datos_sesion
    }, context={'request': request})

    print(sesion_serializer)
    if sesion_serializer.is_valid():
        print('es valido')
        sesion_serializer.save()
    else:
        return JsonResponse(sesion_serializer.errors, status=400)

# Función para validar el tipo de usuario


def validar_usuario(usuario: str) -> str:
    # Limpiar espacios
    usuario = usuario.strip()
    # Verifica si el usuario es externo
    if re.fullmatch(r'^[A-Z][A-Z0-9]*$', usuario):
        return "externo"  # Es un usuario externo en el formato correcto
    # Verifica si el usuario es interno
    elif re.fullmatch(r'^[a-z]+\.[a-z]+$', usuario):
        return "interno"  # Es un usuario interno en el formato correcto
    else:
        return "invalido"  # No cumple ninguna de las validaciones
