from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CadastroUsuarioForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.is_superuser = True
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class EditarUsuarioForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'email']

