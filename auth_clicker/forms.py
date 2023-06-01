from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        username = self.changed_data['username']
        password = self.changed_data['password']
        user = User.objects.create_user(username, '', password)
        if commit:
            user.save()
        return user