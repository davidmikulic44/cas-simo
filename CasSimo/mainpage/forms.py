from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DjangoUser
from .models import User as UserProfile
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = DjangoUser
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'login-input',
                                                     'aria-describedby': 'inputGroup-sizing-default',
                                                     'placeholder': 'username',
                                                     'style': 'text-align: center'})

        self.fields['password1'].widget.attrs.update({'class': 'login-input',
                                                      'aria-describedby': 'inputGroup-sizing-default',
                                                      'placeholder': 'password',
                                                      'style': 'text-align: center'})

        self.fields['password2'].widget.attrs.update({'class': 'login-input',
                                                      'aria-describedby': 'inputGroup-sizing-default',
                                                      'placeholder': 'confirm password',
                                                      'style': 'text-align: center'})
class AddFundsForm(forms.Form):
    user = forms.ModelChoiceField(queryset=UserProfile.objects.all(), empty_label=None)
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0,
        widget=forms.TextInput(attrs={'placeholder': 'Enter amount'}),  # Add a placeholder
    )