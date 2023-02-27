import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Student, Test, Answer

user_name = 'testing_login'
psw = 'admin123'
payloadAnswer = {           
    "question":1,
    "selected_option":2            
}

class ApiTestCase(TestCase):
    fixtures = ['api_fixture.json', ]
    
    def setUp(self):
        user = Student(
            name=user_name,
            password=psw
        )
        user.save()              
   
        client = APIClient()
        response = client.post(
                '/api/login', {
                'name': user_name,
                'password': psw,
                },
                format='json'
        )        
        result = json.loads(response.content)
        access_token = result['token']['access']
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        self.client = client

    def test_get_tests(self):
        client = APIClient()
        response = client.get('/api/test')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(result['detail'], 'Authentication credentials were not provided.')
    
    def test_create_answer(self):
        client = APIClient()
        response = client.post('/api/answer/', payloadAnswer) 
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(result['detail'], 'Authentication credentials were not provided.')
    
    def test_update_answer(self):
        res = self.client.post('/api/answer/', payloadAnswer) 
        created = json.loads(res.content)
        pk = created["id"]
        payload = {
            "selected_option":3,
            "student":created["student"],
            "question":created["question"],
            "id":pk
        }
        client = APIClient()
        response = client.put(
            f'/api/answer/{pk}/', 
            payload,
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(result['detail'], 'Authentication credentials were not provided.')
    
    def test_delete_answer(self):
        res = self.client.post('/api/answer/', payloadAnswer) 
        created = json.loads(res.content)
        pk = created["id"]
        client = APIClient()
        response = client.delete(
            f'/api/answer/{pk}/', 
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(result['detail'], 'Authentication credentials were not provided.')