from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.commons import get_tokens_for_user

class LoginStudentView(APIView):
    def post(self, request):
        data = request.data
        if data['name'] == None or data['password'] == None:
            return Response({'message': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = data['name']
        password = data['password']
        user = authenticate(
            request, username=username, password=password)
        if (user is not None) and user.is_student :
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'message': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
