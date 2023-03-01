from django.contrib import admin
from api.models import (Student, Teacher, Test, Question, Answer, User)
from api.commons import TeacherAdminSite, AnswerAdminSite


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(TeacherAdminSite):
    readonly_fields = ['user']
    def get_list_display(self, request):
        return ['name',] 

@admin.register(Teacher)
class TeacherAdmin(TeacherAdminSite):
    readonly_fields = ['user']
    def get_list_display(self, request):
        return ['name',]    

@admin.register(Test)
class TestAdmin(TeacherAdminSite):
    pass

@admin.register(Question)
class QuestionAdmin(TeacherAdminSite):
    pass

@admin.register(Answer)
class AnswerAdmin(AnswerAdminSite):
    pass

   
           

