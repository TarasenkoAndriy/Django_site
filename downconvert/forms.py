from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Name', 'class':'form-control valid'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class':'form-control valid'}
        )
    )
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message','cols':30, 'rows': 9,'class': 'form-control w-100'}
        )
    )
# для скачивания на user_downloud
from django import forms
class UserForm(forms.Form):
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        email = forms.EmailField()
