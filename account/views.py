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

            account.save()
            
            user = authenticate(username=username, email=email, password=raw_password)
            if user is not None:
                login(request, user)
            return redirect('account:user_login')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect('account:my_page')  # Redirect to the user's profile or home page
#         else:
#             error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'
#             return render(request, 'account/login.html', {'error_message': error_message})
#     else:
#         return render(request, 'account/login.html')

@login_required
def my_page(request):
    if request.method == 'GET':
        #my_community = Community.objects.filter(author=request.user)
        return render(request, 'account/mypage.html'
        #{'my_community': my_community,}
                      )

@login_required
def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.usr)
        if form.is_valid():
            form.save()
            return redirect('account/mypage.html')
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
    if check_password(origin_password, user.password):
      new_password = request.POST["new_password"]
      confirm_password = request.POST["confirm_password"]
      if new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        auth.login(request, user)
        return redirect('account/mypage.html')
      else:
        messages.error(request, 'Password not same')
    else:
      messages.error(request, 'Password not correct')
    return render(request, 'change_password.html')
  else:
    return render(request, 'change_password.html')