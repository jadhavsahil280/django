from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
# Create your views here.


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you are registered succesfully')
            return redirect('food:index')
    else:
            form = RegisterForm
    return render(request, 'user/register.html', {"form":form})

@login_required
def user_profile(request):
     return render(request, 'user/profile.html')