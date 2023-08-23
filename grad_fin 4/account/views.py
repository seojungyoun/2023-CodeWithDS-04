from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.checks import messages
from .forms import UserForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password)
            if user is not None:
                login(request, user)
            account.save()
            return redirect('account:login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def my_page(request):
    if request.method == 'GET':
        #my_community = Community.objects.filter(author=request.user)
        return render(request, 'mypage.html'
        #{'my_community': my_community,}
                      )


@login_required
def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.usr)
        if form.is_valid():
            form.save()
            return redirect('mypage.html')
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)

@login_required
def change_password(request):
  if request.method == "POST":
    user = request.user
    origin_password = request.POST["origin_password"]
    if check_password(origin_password, user.password):
      new_password = request.POST["new_password"]
      confirm_password = request.POST["confirm_password"]
      if new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        auth.login(request, user)
        return redirect('mypage.html')
      else:
        messages.error(request, 'Password not same')
    else:
      messages.error(request, 'Password not correct')
    return render(request, 'change_password.html')
  else:
    return render(request, 'change_password.html')