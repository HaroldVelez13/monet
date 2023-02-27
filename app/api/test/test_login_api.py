import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Student, Test

user_name = 'testing_login'
psw = 'admin123'

class LoginStudentViewTestCase(TestCase):
    access_token = ''
    def setUp(self):
        user = Student(
            name=user_name,
            password=psw
        )
        user.save()      
            
    def test_login_student(self):
        client = APIClient()
        response = client.post(
                '/api/login', {
                'name': user_name,
                'password': psw,
                },
                format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        result = json.loads(response.content)
        self.assertIn('token', result)
        self.assertIn('message', result)
        self.assertIn('user', result)
        self.access_token = result['token']['access']
        self.user = result['user']