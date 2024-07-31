from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',) 
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        for field in self.fields.values():
            field.error_messages = {
                'required': f'{field.label} is required',
                'invalid': f'enter a valid {field.label}',
            }

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password', )


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name', required=False,
                             widget=forms.TextInput(attrs={'class': 'form-group' 'form-group label ', 'placeholder': 'Name'}))
    email = forms.EmailField(label='email', required=False,
                             widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Email'}))
    subject = forms.CharField(label='subject', required=False,
                             widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Subject'}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'Message'}))

    def __str__(self):
        return self.name