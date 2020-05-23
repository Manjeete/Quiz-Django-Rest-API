from rest_framework import serializers
from question.models import Question, Quiz, Answer
from accounts.api.serializers import QuizUserDetailSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']

       

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'label',
            'order',
            'answers'
        ]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    user = QuizUserDetailSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ['id','user', 'name', 'questions_count', 'questions']
        read_only_fields = ['user']

    def create(self, validated_data):
        questions = validated_data.pop('questions', None)
        quiz = Quiz.objects.create(**validated_data)

        if questions is not None:
            for question in questions:
                answers = question.pop('answers', None)
                question = Question.objects.create(quiz=quiz, **question)
                if answers is not None:
                    for answer in answers:
                        Answer.objects.create(question=question, **answer)
        return quiz

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', None)
        questions = (instance.questions).all()
        questions = list(questions)
        instance.name = validated_data.get('name', instance.name)
        instance.questions_count = validated_data.get('questions_count', instance.questions_count)
        instance.save()
        if questions_data is not None:
            for question_data in questions_data:
                answers_data = question_data.pop('answers')
                question = questions.pop(0)
                answers = (question.answers).all()
                answers = list(answers)

                question.label = question_data.get('label', question.label)
                question.order = question_data.get('order', question.order)
                question.save()
                if answers_data is not None:
                    for answer_data in answers_data:
                        answer = answers.pop(0)
                        answer.text = answer_data.get('text', answer.text)
                        answer.is_correct = answer_data.get('is_correct', answer.is_correct)
                        answer.save()

        return instance                

class QuizInlineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'created']


# Only for question post

class QuestionPostSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'label', 'order', 'answers']
        read_only_fields = ['quiz']    

    def create(self, validated_data):
        answers = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer in answers:
            Answer.objects.create(**answer, question=question)
        return question

    def update(self, instance, validated_data):
        answers_data = validated_data.pop('answers', None)
        answers = (instance.answers).all()
        answers = list(answers)
        instance.label = validated_data.get('label', instance.label)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        if answers_data is not None:
            for answer_data in answers_data:
                answer = answers.pop(0)
                answer.text = answer_data.get('text', answer.text)
                answer.is_correct = answer_data.get('is_correct', answer.is_correct)
                answer.save()
        return instance


# only for quiz detail
# class QuizDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = ['id', 'name', 'questions_count'] 