# coding: utf-8

from modeltranslation.translator import translator, TranslationOptions
from django_textflow.models import FlowObject


class FlowObjectTranslationOption(TranslationOptions):
    fields = ('text',)

translator.register(FlowObject, FlowObjectTranslationOption)
