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

class ProfileFormHoraA(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('horatomadaA',)
    def save(self, user=None):
        profile = super(ProfileFormHoraA, self).save(commit=False)
        if user:
            profile.user = user
        profile.save()
        return profile

class ProfileFormHoraF(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('horatomadaF',)
    def save(self, user=None):
        profile = super(ProfileFormHoraF, self).save(commit=False)
        if user:
            profile.user = user
        profile.save()
        return profile

class ProfileFormHoraT(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('horatomadaT',)
    def save(self, user=None):
        profile = super(ProfileFormHoraT, self).save(commit=False)
        if user:
            profile.user = user
        profile.save()
        return profile
