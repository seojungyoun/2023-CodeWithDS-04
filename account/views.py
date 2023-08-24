# from django.contrib import auth
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.hashers import check_password
# from django.core.checks import messages
# from .forms import UserForm, UserChangeForm
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect

# def signup(request):
#     if request.method == "POST":
#         print(request.POST)
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             account = form.save(commit=False)
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')

#             account.save()
            
#             user = authenticate(username=username, email=email, password=raw_password)
#             if user is not None:
#                 login(request, user)
#             return redirect('account:user_login')
#     else:
#         form = UserForm()
#     return render(request, 'account/signup.html', {'form': form})

# @login_required
# def my_page(request):
#     if request.method == 'GET':
#         #my_community = Community.objects.filter(author=request.user)
#         return render(request, 'account/mypage.html'
#         #{'my_community': my_community,}
#                       )

# @login_required
# def update(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.usr)
#         if form.is_valid():
#             form.save()
#             return redirect('account/mypage.html')
#     else:
#         form = UserChangeForm(instance=request.user)
#     context = {
#         'form': form,
#     }

#     return render(request, 'account/update.html', context)

# @login_required
# def change_password(request):
#   if request.method == "POST":
#     user = request.user
#     origin_password = request.POST["origin_password"]
#     if check_password(origin_password, user.password):
#       new_password = request.POST["new_password"]
#       confirm_password = request.POST["confirm_password"]
#       if new_password == confirm_password:
#         user.set_password(new_password)
#         user.save()
#         auth.login(request, user)
#         return redirect('account/mypage.html')
#       else:
#         messages.error(request, 'Password not same')
#     else:
#       messages.error(request, 'Password not correct')
#     return render(request, 'change_password.html')
#   else:
#     return render(request, 'change_password.html')

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm, UserChangeForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('account:my_page')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            account.set_password(raw_password)
            account.save()

            user = authenticate(username=account.username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('account:my_page')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def my_page(request):
    if request.method == 'GET':
        return render(request, 'account/mypage.html')

@login_required
def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:my_page')
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'account/update.html', context)

@login_required
def change_password(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST["origin_password"]
        if user.check_password(origin_password):
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                auth_login(request, user)
                return redirect('account:my_page')
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다')
        else:
            messages.error(request, '잘못된 비밀번호입니다')
    return render(request, 'change_password.html')
