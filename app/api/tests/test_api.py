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

class ApiTestGuestCase(TestCase):
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
        response = self.client.get('/api/test')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('description', result[0])
        self.assertIn('questions', result[0])

    def test_create_answer(self):        
        response = self.client.post('/api/answer/', payloadAnswer) 
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('is_correct', result)
        self.assertIn('question_statement', result)
        self.assertIn('selected', result)
    
    def test_cant_create_answer_duplicate(self):        
        response = self.client.post('/api/answer/', payloadAnswer) 
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/api/answer/', payloadAnswer) 
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', result)
        self.assertEqual(result['non_field_errors'][0],  "The fields student, question must make a unique set.")

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
        response = self.client.put(
            f'/api/answer/{pk}/', 
            payload,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(pk, result["id"])
    
    def test_delete_answer(self):
        res = self.client.post('/api/answer/', payloadAnswer) 
        created = json.loads(res.content)
        pk = created["id"]
        response = self.client.delete(
            f'/api/answer/{pk}/', 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        exists = Answer.objects.filter(pk=pk)
        self.assertFalse(exists)
