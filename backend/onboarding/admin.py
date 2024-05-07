from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')


class SurveyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('question_text',)}
    list_display = ('id_sur', 'question_text', 'slug', 'active')


class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('question_text',)}
    list_display = ('id_ques', 'question_text', 'slug', 'active')


class ChoiceSurveyAdmin(admin.ModelAdmin):
    list_display = ('id_choice', 'choice_text', 'survey', 'slug')


class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('id_choice', 'choice_text', 'question', 'slug')


class UserSurveyAdmin(admin.ModelAdmin):
    list_display = ('user',)


class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Site)
admin.site.register(User, UserAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ChoiceSurvey, ChoiceSurveyAdmin)
admin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
admin.site.register(UserSurvey, UserSurveyAdmin)
admin.site.register(UserQuestion, UserQuestionAdmin)