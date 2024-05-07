import graphene
from . import models
from . import types


class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)
    all_user = graphene.List(types.UserType)
    current_user = graphene.Field(types.UserType, username=graphene.String())

    all_surveys = graphene.List(types.SurveyType)
    all_questions = graphene.List(types.QuestionType)

    survey_by_slug = graphene.List(types.SurveyType, slug=graphene.String())
    question_by_slug = graphene.List(types.QuestionType, slug=graphene.String())

    choice_survey_by_slug = graphene.List(types.ChoiceSurveyType, slug=graphene.String())
    choice_question_by_slug = graphene.List(types.ChoiceQuestionType, slug=graphene.String())

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )

    def resolve_all_user(root, info):
        return (
            models.User.objects.all()
        )

    def resolve_current_user(root, info, username):
        return (
            models.User.objects.get(username__iexact=username)
        )

    def resolve_all_surveys(root, info):
        return (
            models.Survey.objects.all()
        )

    def resolve_all_questions(root, info):
        return (
            models.Question.objects.all()
        )

    def resolve_survey_by_slug(root, info, slug):
        return (
            models.Survey.objects.get(slug__iexact=slug)
        )

    def resolve_question_by_slug(root, info, slug):
        return (
            models.Question.objects.get(slug__iexact=slug)
        )

    def resolve_choice_survey_by_slug(root, info, slug):
        return (
            models.ChoiceSurvey.objects.get(slug__iexact=slug)
        )

    def resolve_choice_question_by_slug(root, info, slug):
        return (
            models.ChoiceQuestion.objects.get(slug__iexact=slug)
        )