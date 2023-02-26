from django.contrib import admin
from api.models import (Student, Teacher, Test, Question, Answer, User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
    def get_list_display(self, request):
        return ['name',]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
    def get_list_display(self, request):
        return ['name',]

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

