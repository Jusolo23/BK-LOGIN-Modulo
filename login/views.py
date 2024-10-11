from django.shortcuts import render
import requests
import msal
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth.models import User
from login import serializers
import json


def _build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        settings.MSAL_CONFIG['CLIENT_ID'],
        authority=settings.MSAL_CONFIG['AUTHORITY'],
        client_credential=settings.MSAL_CONFIG['CLIENT_SECRET'],
        token_cache=cache
    )


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        recaptcha_token = data.get('recaptchaToken')

        if not username or not password:
            return JsonResponse({"error": "Se requiere nombre de usuario y contraseña."}, status=400)

        recaptcha_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_token
            }
        )

        recaptcha_result = recaptcha_response.json()

        if not recaptcha_result.get('success'):
            return JsonResponse({"error": "reCAPTCHA no válido."}, status=400)

        app = _build_msal_app()

        result = app.acquire_token_by_username_password(
            username=f"{username}@unp.gov.co",
            password=password,
            scopes=settings.MSAL_CONFIG['SCOPE']
        )

        if 'access_token' in result:
            data = obtener_datos(result['access_token']).json()
            data['password'] = password
            save_data = guardar_datos(data)
            if isinstance(save_data, JsonResponse) and save_data.status_code == 400:
                return JsonResponse({'error': "Ocurrio un error"}, status=400)
            return JsonResponse({'access_token': result['access_token']})
        else:
            #  result.get("error_description", "Error de autenticación")
            return JsonResponse({'error': "Credenciales incorrectas"}, status=400)

    return JsonResponse({"error": "Método no permitido."}, status=405)


@api_view(['POST'])
def logout(request):
    auth_header = request.headers.get('Authorization', None)

    if not auth_header:
        return Response({"error": "No se proporcionó token de autorización."}, status=400)

    access_token = auth_header.split(' ')[1]

    revoke_url = f"{settings.MSAL_CONFIG['AUTHORITY']}/oauth2/v2.0/logout"

    response = requests.post(revoke_url, headers={
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    })

    if response.status_code != 200:
        return Response({"error": "No se pudo revocar el token."}, status=response.status_code)

    return Response({"message": "Logout exitoso."}, status=200)


def obtener_datos(access_token):
    graph_url = 'https://graph.microsoft.com/v1.0/me'
    response = requests.get(
        graph_url, headers={'Authorization': f'Bearer {access_token}'})

    if response.status_code == 200:
        return response

    return JsonResponse({"error": "No se pudo obtener datos del usuario."}, status=response.status_code)


def guardar_datos(data):
    existing_user = User.objects.filter(
        username=data['userPrincipalName']).first()
    if not existing_user:
        user_serializer = serializers.UserSerializer(data={
            'username': data['userPrincipalName'],
            'email': data['mail'],
            'password': data['password'],
            'first_name': data.get('givenName', ''),
            'last_name': data.get('surname', ''),
            'is_active': True,
        })

        if user_serializer.is_valid():
            user_serializer.save()
            JsonResponse(
                {'message': 'Usuario creado exitosamente'}, status=200)
        else:
            return JsonResponse(user_serializer.errors, status=400)

    return JsonResponse({'message': 'Usuario ya existe'}, status=409)
