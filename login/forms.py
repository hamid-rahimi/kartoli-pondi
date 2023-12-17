from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری", widget=forms.TextInput(
        attrs={'placeholder': "نام کاربری...", 'class': "border",}))
    password = forms.CharField(label="رمز ورود", widget=forms.PasswordInput(
        attrs={'placeholder': "رمز ورود...", 'class': "border",}))
