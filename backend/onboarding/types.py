from graphene_django import DjangoObjectType
from . import models


class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site


class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class SurveyType(DjangoObjectType):
    class Meta:
        model = models.Survey


class ChoiceSurveyType(DjangoObjectType):
    class Meta:
        model = models.ChoiceSurvey


class QuestionType(DjangoObjectType):
    class Meta:
        model = models.Question


class ChoiceQuestionType(DjangoObjectType):
    class Meta:
        model = models.ChoiceQuestion


class UserSurveyType(DjangoObjectType):
    class Meta:
        model = models.UserSurvey


class UserQuestionType(DjangoObjectType):
    class Meta:
        model = models.UserQuestion
