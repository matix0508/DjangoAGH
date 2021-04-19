from django import forms
from .models import Subject


class SubjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    max_pkt = forms.FloatField(label='Max pkt')
    your_pkt = forms.FloatField(label='Your pkt')
    extended = forms.BooleanField(initial=True)


class FieldForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    r1 = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label='[Extended Level]')
    r2 = forms.ModelChoiceField(empty_label='[Second Extended Subject]', queryset=Subject.objects.all())
    p = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label='[Basic Level]')
