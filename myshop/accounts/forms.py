from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Profile



class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(initial = 'Your name')
    # last_name = forms.CharField(initial='tatarov')
    # email = forms.EmailField()
    address = forms.CharField()
    postal_code = forms.IntegerField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ('username',  'password1', 'password2',
                  'first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'postal_code', 'city')#'first_name', 'last_name', 'email',