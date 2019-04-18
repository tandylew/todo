from django import forms
import datetime

class ContactForm(forms.Form):
    email = forms.EmailField(max_length=254,required=False)
    password = forms.CharField(widget=forms.PasswordInput(),required=False)
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput(),
        required=False
    )

class DateForm(forms.Form):
    todo = forms.CharField(max_length=254,required=False)
    date = forms.DateField(label='Date: ', widget=forms.SelectDateWidget,required=False)
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput(),
        required=False
    )

    def clean(self):
        cleaned_data = super(DateForm, self).clean()
        todo = cleaned_data.get('todo')
        date = cleaned_data.get('date')
        #if not name and not email and not message:
        #    raise forms.ValidationError('You have to write something!')
