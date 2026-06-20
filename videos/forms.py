from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid email or password")

        user = authenticate(username=user_obj.username, password=password)
        if not user:
            raise forms.ValidationError("Invalid email or password")

        self.cleaned_data['user'] = user
        return self.cleaned_data
