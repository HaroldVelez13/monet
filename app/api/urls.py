from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import LoginStudentView, TestView, AnswerView

router = SimpleRouter()
router.register(r'answer', AnswerView, basename='answer')

urlpatterns = [
     # Auth
     path('login', LoginStudentView.as_view(), name='login'),
     path('test', TestView.as_view(), name='test')
]


urlpatterns += router.urls