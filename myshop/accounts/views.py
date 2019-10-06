from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, ProfileForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.postal_code = form.cleaned_data.get('postal_code')
            user.profile.city = form.cleaned_data.get('city')
            user.save()
            # my_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=my_password)
            # login(request, user)
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# for field in form.fields:
#     if form.cleaned_data.get(field) != '':
#         print(field +": "+form.cleaned_data.get(field))
#         user.profile[field] = form.cleaned_data.get(field)
#     # print(form.cleaned_data.get(field))
#     # print(getattr(user.profile, 'postal_code'))
#     # print(user.profile.address)
#     print(getattr(user.profile, field))
#     if field.has_changed():
#         user.profile[field]=form.cleaned_data.get(field)
# if form.fields['fisrt_name']:

@login_required
def profile_view(request):
    user = User.objects.get(pk=request.user.id)
    fields = user._meta.get_fields()
    # field_values =
    return render(request, 'profile.html', {'fields': fields})
# сначала вывести пару полей руками

@login_required
def profile_change(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        profile_form = ProfileForm(request.POST)
        user_form = UserChangeForm(request.POST)
        # form = UserChangeForm(request.POST)
        if user_form.is_valid():
            if user_form.cleaned_data.get('first_name') != '':
                user.first_name = user_form.cleaned_data.get('first_name')
            if user_form.cleaned_data.get('last_name') != '':
                user.last_name = user_form.cleaned_data.get('last_name')
            if user_form.cleaned_data.get('email') != '':
                user.email = user_form.cleaned_data.get('email')
        if profile_form.is_valid():
            if profile_form.cleaned_data.get('address') != '':
                user.profile.address = profile_form.cleaned_data.get('address')
            if profile_form.cleaned_data.get('postal_code') != '':
                user.profile.postal_code = profile_form.cleaned_data.get('postal_code')
            if profile_form.cleaned_data.get('city') != '':
                user.profile.city = profile_form.cleaned_data.get('city')

            user.save()
        return render(request, 'profile_change.html', {'user_form': user_form, 'profile_form': profile_form})

    else:
        profile_form = ProfileForm(request.POST)
        user_form = UserChangeForm(request.POST)
    return render(request, 'profile_change.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def password_edit(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Исправьте ошибки!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_edit.html', {
        'form': form
    })