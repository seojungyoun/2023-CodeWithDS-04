from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'phonenumber', 'birthdate']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(UserChangeForm) :
    class Meta :
        model = User
        fields = ['username', 'name', 'phonenumber', 'birthdate']

def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, 'Password successfully changed')
      return redirect('profile')
    else:
      messages.error(request, 'Password not changed')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'change_password.html',{'form':form})