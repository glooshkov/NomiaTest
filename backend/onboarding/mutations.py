import graphene
import graphql_jwt
from . import models, types


# Настройте поведение ObtainJSONWebToken, чтобы включить информацию о пользователе.
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


# Мутация сохраняеет данные в сессию и отправляет токен
class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class UpdateUserProfile(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        user_id = graphene.ID(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)

    def mutate(self, info, user_id, first_name='', last_name=''):
        user = models.User.objects.get(pk=user_id)

        user.first_name = first_name
        user.last_name = last_name

        user.save()

        return UpdateUserProfile(user=user)


class CreateSurvey(graphene.Mutation):
    survey = graphene.Field(types.SurveyType)

    class Arguments:
        question_text = graphene.String(required=True)
        description = graphene.String(required=False)
        active = graphene.Boolean(required=False)
        slug = graphene.String(required=True)

    def mutate(self, info, question_text, description, active, slug):
        survey = models.Survey(
            question_text=question_text,
            description=description,
            active=active,
            slug=slug
        )
        survey.save()

        return CreateSurvey(survey=survey)


class UpdateSurvey(graphene.Mutation):
    survey = graphene.Field(types.SurveyType)

    class Arguments:
        slug_old = graphene.String(required=True)
        question_text = graphene.String(required=False)
        description = graphene.String(required=False)
        active = graphene.Boolean(required=False)
        slug = graphene.String(required=False)

    def mutate(self, info, slug_old, question_text, description, active, slug):
        survey = models.Survey.objects.get(slug=slug_old)

        survey.question_text = question_text
        survey.description = description
        survey.active = active
        survey.slug = slug

        survey.save()

        return UpdateSurvey(survey=survey)


class CreateChoiceSurvey(graphene.Mutation):
    choice = graphene.Field(types.ChoiceSurveyType)

    class Arguments:
        id = graphene.ID(required=True)
        choice_text = graphene.String(required=True)
        slug = graphene.String(required=False)

    def mutate(self, info, id, choice_text, slug):
        survey = models.Survey.objects.get(id_sur=id)
        choice = models.ChoiceSurvey(
            survey=survey,
            choice_text=choice_text,
            slug=slug
        )
        choice.save()

        return CreateChoiceSurvey(choice=choice)


class UpdateChoiceSurvey(graphene.Mutation):
    choice = graphene.Field(types.ChoiceSurveyType)

    class Arguments:
        slug_old = graphene.String(required=True)
        choice_text = graphene.String(required=False)
        slug = graphene.String(required=False)

    def mutate(self, info, slug_old, choice_text, slug):
        choice = models.ChoiceSurvey.objects.get(slug=slug_old)

        choice.choice_text = choice_text
        choice.slug = slug

        choice.save()

        return UpdateChoiceSurvey(choice=choice)


class CreateQuestion(graphene.Mutation):
    question = graphene.Field(types.QuestionType)

    class Arguments:
        question_text = graphene.String(required=True)
        description = graphene.String(required=False)
        active = graphene.Boolean(required=False)
        slug = graphene.String(required=True)

    def mutate(self, info, question_text, description, active, slug):
        question = models.Question(
            question_text=question_text,
            description=description,
            active=active,
            slug=slug
        )
        question.save()

        return CreateQuestion(question=question)


class UpdateQuestion(graphene.Mutation):
    question = graphene.Field(types.QuestionType)

    class Arguments:
        slug_old = graphene.String(required=True)
        question_text = graphene.String(required=False)
        description = graphene.String(required=False)
        active = graphene.Boolean(required=False)
        slug = graphene.String(required=False)

    def mutate(self, info, slug_old, question_text, description, active, slug):
        question = models.Question.objects.get(slug=slug_old)

        question.question_text = question_text
        question.description = description
        question.active = active
        question.slug = slug

        question.save()

        return UpdateQuestion(question=question)


class CreateChoiceQuestion(graphene.Mutation):
    choice = graphene.Field(types.ChoiceQuestionType)

    class Arguments:
        id = graphene.ID(required=True)
        choice_text = graphene.String(required=True)
        slug = graphene.String(required=False)

    def mutate(self, info, id, choice_text, slug):
        question = models.Question.objects.get(id_ques=id)
        choice = models.ChoiceQuestion(
            question=question,
            choice_text=choice_text,
            slug=slug
        )
        choice.save()

        return CreateChoiceQuestion(choice=choice)


class UpdateChoiceQuestion(graphene.Mutation):
    choice = graphene.Field(types.ChoiceQuestionType)

    class Arguments:
        slug_old = graphene.String(required=True)
        choice_text = graphene.String(required=False)
        slug = graphene.String(required=False)

    def mutate(self, info, slug_old, choice_text, slug):
        choice = models.ChoiceQuestion.objects.get(slug=slug_old)

        choice.choice_text = choice_text
        choice.slug = slug

        choice.save()

        return UpdateChoiceQuestion(choice=choice)


class CreateUserSurvey(graphene.Mutation):
    answer_survey = graphene.Field(types.UserSurveyType)

    class Arguments:
        id = graphene.ID(required=True)
        slug = graphene.String(required=True)
        choices = graphene.String(required=True)

    def mutate(self, info, id, slug, choices):
        user = models.User.objects.get(pk=id)

        answer_survey = models.UserSurvey(
            survey=slug,
            user=user,
            choices=choices,
        )
        answer_survey.save()

        return CreateUserSurvey(answer_survey=answer_survey)


class UpdateUserSurvey(graphene.Mutation):
    answer_survey = graphene.Field(types.UserSurveyType)

    class Arguments:
        id = graphene.ID(required=True)
        slug = graphene.String(required=True)
        choices = graphene.String(required=True)

    def mutate(self, info, id, slug, choices):
        user = models.User.objects.get(pk=id)
        answer_survey = models.UserSurvey.objects.get(user=user, pk=slug)

        answer_survey.choices = choices
        answer_survey.save()

        return UpdateUserSurvey(answer_survey=answer_survey)


class CreateUserQuestion(graphene.Mutation):
    answer_question = graphene.Field(types.UserQuestionType)

    class Arguments:
        id = graphene.ID(required=True)
        slug = graphene.String(required=True)
        choices = graphene.String(required=True)

    def mutate(self, info, id, slug, choices):
        user = models.User.objects.get(pk=id)

        answer_question = models.UserQuestion(
            question=slug,
            user=user,
            choices=choices,
        )
        answer_question.save()

        return CreateUserQuestion(answer_question=answer_question)


class UpdateUserQuestion(graphene.Mutation):
    answer_question = graphene.Field(types.UserQuestionType)

    class Arguments:
        id = graphene.ID(required=True)
        slug = graphene.String(required=True)
        choices = graphene.String(required=True)

    def mutate(self, info, id, slug, choices):
        user = models.User.objects.get(pk=id)
        answer_question = models.UserQuestion.objects.get(user=user, pk=slug)

        answer_question.choices = choices
        answer_question.save()

        return UpdateUserQuestion(answer_question=answer_question)


class Mutation(graphene.ObjectType):
    # Tokens
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_user = CreateUser.Field()
    update_user_profile = UpdateUserProfile.Field()

    create_survey = CreateSurvey.Field()
    create_question = CreateQuestion.Field()
    create_survey_choice = CreateChoiceSurvey.Field()
    create_question_choice = CreateChoiceQuestion.Field()
    create_user_survey = CreateUserSurvey.Field()
    create_user_question = CreateUserQuestion.Field()

    update_survey = UpdateSurvey.Field()
    update_question = UpdateQuestion.Field()
    update_survey_choice = UpdateChoiceSurvey.Field()
    update_question_choice = UpdateChoiceQuestion.Field()
    update_user_survey = UpdateUserSurvey.Field()
    update_user_question = UpdateUserQuestion.Field()
