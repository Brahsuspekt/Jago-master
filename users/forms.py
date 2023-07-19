from django import forms 
from django.contrib.auth.models import User 


class UserRegisterFrom(forms.ModelForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'enter username',
                'class'      : 'form-control'
            }
        )
    )

    email = forms.EmailField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'enter email',
                'class'      : 'form-control'
            }
        )
    )

    password = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'enter password',
                'class'      : 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class LoginForm(forms.Form):
    username = forms.EmailField(
        required=True, widget=forms.TextInput(
            attrs={

                'placeholder':'enter username',
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'enter password',
                'class':'form-control'
            }
        )
    )




class EmailForm(forms.Form):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'enter email',
                'class':'form-control'
            }
        )
    )


class CodeForm(forms.Form):
    code = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'placeholder':'enter code',
                'class':'form-control'
            }
        )
    )