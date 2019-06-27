from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('rut', 'sede', 'tipo')

class ProfileFormHora(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('horatomada',)
    def save(self, user=None):
        profile = super(ProfileFormHora, self).save(commit=False)
        if user:
            profile.user = user
        profile.save()
        return profile
