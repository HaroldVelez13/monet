from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import StudentSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'token': {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },
        'user': StudentSerializer(user.student).data,
    }