from django.contrib import admin
from api.models import (Student, Teacher, Test, Question, Answer, User)
from api.commons import TeacherAdminSite, AnswerAdminSite

admin.site.site_header  =  "Monet Test"  
admin.site.site_title  =  "Test"
admin.site.index_title  =  "Monet Admin"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    icon_name = 'group'

@admin.register(Student)
class StudentAdmin(TeacherAdminSite):
    readonly_fields = ['user']
    icon_name = 'face'
    def get_list_display(self, request):
        return ['name',] 

@admin.register(Teacher)
class TeacherAdmin(TeacherAdminSite):
    readonly_fields = ['user']
    icon_name = 'school'
    def get_list_display(self, request):
        return ['name',]    

@admin.register(Test)
class TestAdmin(TeacherAdminSite):
    icon_name = 'assignment'

@admin.register(Question)
class QuestionAdmin(TeacherAdminSite):
    icon_name = 'format_list_bulleted'

@admin.register(Answer)
class AnswerAdmin(AnswerAdminSite):
    icon_name = 'rate_review'

   
           

