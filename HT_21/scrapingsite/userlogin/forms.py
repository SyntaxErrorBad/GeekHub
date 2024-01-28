from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label='Login:',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput()
    )
