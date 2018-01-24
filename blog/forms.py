from django import forms
from .models import Suggest


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        fields = ['suggest']
        widgets = {
            'suggest': forms.Textarea(attrs={
                'placeholder': '写下你的意见吧~',
                'class': 'form-control',
                'rows': 4,
                'cols': 80,
                })
        }



