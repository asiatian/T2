from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm,ProfileForm
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def profile(request):
    args = {'user': request.user}
    return render(request,'profile.html',args)


def update_profile(request):
    try:
        profile = request.user.profile
        #print(profile)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Su perfil fue actualizado con exito.')
            return redirect('profile')
        else:
            messages.error(request, ('Error.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
