from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from api.models import (Student, Test, Question, Answer)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name']



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['correct_option']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Test
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    is_correct = serializers.SerializerMethodField()   
    question_statement = serializers.SerializerMethodField()   
    selected = serializers.SerializerMethodField()     

    class Meta:
        model = Answer
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Answer.objects.all(),
                fields=['student', 'question']
            )
        ]
    
    def get_is_correct(self, obj):
        isCorrect = obj.selected_option == obj.question.correct_option
        return "Correct" if isCorrect else "Incorrect"
    
    def get_question_statement(self, obj):
        return obj.question.statement

    def get_selected(self, obj):
        return obj.question.options[obj.selected_option]
    
