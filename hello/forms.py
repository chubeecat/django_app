from django import forms
from .models import Friend, Message


class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)


class CheckForm(forms.Form):
    str = forms.CharField(label='Name')

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if str.lower().startswith('no'):
            raise forms.ValidationError('You input "NO"! ')


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']
