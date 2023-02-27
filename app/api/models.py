from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jsonform.models.fields import ArrayField


# Defining our users
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            user = User.objects.create_user(
                username=self.name, password=self.password, is_student = True)
            self.user = user
        super(Student, self).save(*args, **kwargs)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            user = User.objects.create_user(
                username=self.name, password=self.password, is_teacher = True)
            self.user = user
        super(Teacher, self).save(*args, **kwargs)


#Defining the models for the app logic
class Test(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.description}"


OPTION_TYPE_CHOICES = [
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ]

class Question(models.Model):  
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    statement = models.CharField(max_length=200)
    options = ArrayField( models.CharField(max_length=200), size=4 )
    correct_option = models.IntegerField(
        choices=OPTION_TYPE_CHOICES
    )  

    def __str__(self):
        return f"{self.statement}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    selected_option = models.IntegerField(
        choices=OPTION_TYPE_CHOICES
    )

    def __str__(self):
        return f"{self.question.statement}"
    
    class Meta:
        unique_together = ('question', 'student',)