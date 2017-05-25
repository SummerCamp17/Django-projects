from django.db import models
from django import forms
from .forms import NominationForm
from django.contrib.auth.models import User


class Questionnaire(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=250, default=u"I'm a description!")
    status = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


    #
    def get_form(self, *args, **kwargs):
        fields = []
        for question in self.question_set.all():
            field = question._get_formfield_class()
            label = question.question
            field_args = question._get_field_args()

            fields.append((label, field, field_args))

        return QuestionForm(*args, extra=fields, **kwargs)



    def add_answer(self, applicant, answer_data):
        answer = FilledForm(questionnaire=self, applicant=applicant)
        # for
        # answer.save()





QUES_TYPES = (
    ('Short_answer', 'Short_answer'),
    ('Paragraph', 'Paragraph')
    ('Integer', 'Integer'),
    ('ChoiceField', 'ChoiceField'),
    ('MultipleChoiceField', 'MultipleChoiceField'),
    ('Date', 'Date'),
)

FIELD_TYPES = (
    ('Short_answer', forms.CharField),
    ('Paragraph', forms.TextField),
    ('Integer', forms.IntegerField),
    ('ChoiceField', forms.ChoiceField),
    ('MultipleChoiceField', forms.MultipleChoiceField),
    ('Date', forms.DateField),
)

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, null=True)
    question_type = models.IntegerField(choices=QUES_TYPES, null=True)
    question = models.CharField(max_length=300, null=True)
    question_choices = models.TextField(max_length=512, null=True, blank=True, help_text='make new line for new choice')

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question

    def _get_formfield_class(self):
        for index, field_class in FIELD_TYPES:
            if self.question_type is index:
                return field_class

    def _get_field_args(self):
        args = {}


        args.update({'required': True})
        return args






class Answer(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    answer = models.TextField(max_length=512)

    def __unicode__(self):
        return self.answer

class FilledForm(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    applicant = models.ForeignKey(User)

    def __str__(self):
        return self.questionnaire.name



class AnswerInstance(models.Model):
    form = models.ForeignKey(FilledForm)
    Question = models.ForeignKey(Question)
    questionnaire = models.ForeignKey(Questionnaire)
    answer = models.CharField()

    def __str__(self):
        return self.answer



