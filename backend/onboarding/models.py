from django.db import models, transaction
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'Nomia'
        verbose_name_plural = '1. Nomia'

    def __str__(self):
        return self.name


class User(AbstractUser):

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = '2. Пользователи'

    def __str__(self):
        return self.username


class Survey(models.Model):
    id_sur = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = '3. Опросы'

    def __str__(self):
        return self.question_text


class ChoiceSurvey(models.Model):
    id_choice = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='choice', null=True)
    choice_text = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'варианты (опрос)'
        verbose_name_plural = '4. Варианты (опрос)'

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    id_ques = models.AutoField(primary_key=True)
    active = models.BooleanField(default=False)
    question_text = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = '5. Вопросы'

    def __str__(self):
        return self.question_text


class ChoiceQuestion(models.Model):
    id_choice = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice', null=True)
    choice_text = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'варианты (вопрос)'
        verbose_name_plural = '6. Варианты (вопрос)'

    def __str__(self):
        return self.choice_text


class UserSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_survey', null=True)
    survey = models.SlugField(primary_key=True, default='empty', unique=False)
    choices = models.SlugField(unique=False, default='empty')

    class Meta:
        verbose_name = 'ответ (опрос)'
        verbose_name_plural = '7. Ответы (опрос)'

    def __str__(self):
        return f"Ответ {self.user.username} на опрос со slug: {self.survey}"


class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_question', null=True)
    question = models.SlugField(primary_key=True, default='empty', unique=False)
    choices = models.SlugField(unique=True, default='empty')

    class Meta:
        verbose_name = 'ответ (вопрос)'
        verbose_name_plural = '8. Ответы (вопрос)'

    def __str__(self):
        return f"Ответ {self.user.username} на вопрос со slug: {self.question}"
