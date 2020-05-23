from django.db import models
from django.conf import settings


class Quiz(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    questions_count = models.IntegerField(default=0)
    description = models.CharField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return str(self.name)

    @property
    def questions(self):
        return self.question_set.all()

    @property
    def owner(self):
        return self.user


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.label

    @property
    def answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
