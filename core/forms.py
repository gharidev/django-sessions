from django import forms

class EmailLogin(forms.Form):
    email = forms.EmailField(
        max_length=100,
        required=True,
    )