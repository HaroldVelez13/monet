from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Defining our users
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        self.is_student = True
        super(Student, self).save(*args, **kwargs)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        self.is_teacher = True
        super(Teacher, self).save(*args, **kwargs)


#Defining the models for the app logic
class Test(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"


OPTION_TYPE_CHOICES = [
        ('A', 0),
        ('B', 1),
        ('C', 2),
        ('D', 3),
    ]

class Question(models.Model):  
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    statement = models.CharField(max_length=200)
    options = ArrayField( models.CharField(max_length=200), size=4 )
    correct_option = models.CharField(
        max_length=1,
        choices=OPTION_TYPE_CHOICES
    )  

    def __str__(self):
        return f"{self.statement}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    selected_option = models.CharField(
        max_length=1,
        choices=OPTION_TYPE_CHOICES
    )

    def __str__(self):
        return f"{self.question.statement}"
    
    class Meta:
        unique_together = ('question', 'student',)