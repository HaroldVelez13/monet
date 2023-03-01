from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from api.commons import get_tokens_for_user
from api.models import Test, Answer
from api.serializers import TestSerializer, AnswerSerializer

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


class TestView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)

class AnswerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self):
        if self.request.user.id :
            student = self.request.user.student
            return Answer.objects.filter(student=student)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
    def create(self, request, **kwargs):
        data = request.data.copy()
        data['student'] = request.user.student
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
