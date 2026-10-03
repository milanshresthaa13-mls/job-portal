from django.contrib.auth.forms import UserCreationForm

from .models import User


class BaseRegistrationForm(UserCreationForm):
    role_value = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.order_fields((
            'first_name', 'last_name', 'email', 'username',
            'password1', 'password2',
        ))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.role_value
        if commit:
            user.save()
        return user


class JobSeekerRegistrationForm(BaseRegistrationForm):
    role_value = User.ROLE_CHOICES[0][0]


class EmployerRegistrationForm(BaseRegistrationForm):
    role_value = User.ROLE_CHOICES[1][0]
