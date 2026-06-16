from django import forms
from .models import Article

class FeedbackForm(forms.Form):

    subject = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )

class ArticleForm(forms.ModelForm):

      class Meta:

        model = Article

        fields = [
            'title',
            'description',
            'price',
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'description': forms.Textarea(
                attrs={'class': 'form-control'}
            ),

            'price': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }