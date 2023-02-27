from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import LoginStudentView

router = SimpleRouter()

urlpatterns = [
     # Auth
     path('login', LoginStudentView.as_view(), name='login')
]


urlpatterns += router.urls