from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import StudentSerializer
from django.contrib import admin


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'token': {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },
        'user': StudentSerializer(user.student).data,
    }

class TeacherAdminSite(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def has_module_permission(self, request):
        user = request.user
        if user.id is not None :
            return user.is_teacher or user.is_superuser
        return False

    def has_view_permission(self, request, obj=None):
        user = request.user
        if user.id is not None :
            return user.is_teacher or user.is_superuser
        return False

    def has_add_permission(self, request, obj=None):
        user = request.user
        if user.id is not None :
            return user.is_teacher or user.is_superuser
        return False

    def has_delete_permission(self, request, obj=None):
        user = request.user
        if user.id is not None :
            return user.is_teacher or user.is_superuser
        return False

class AnswerAdminSite(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_student:
            return qs.filter(student=request.user.student)
        return qs
    def get_list_display(self, request):
        return ["test","question", "selected_option","student"]

    def test(self, obj):
        return obj.question.test.description

    def has_module_permission(self, request):
        user = request.user
        if user.id is not None :
            return user.is_teacher or user.is_superuser or user.is_student
        return False

    def has_view_permission(self, request, obj=None):
        user = request.user
        if user.id is not None :
            return user.is_teacher or user.is_superuser or user.is_student
        return False