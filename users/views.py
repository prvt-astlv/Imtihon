from django.shortcuts import render, redirect
from .forms import CreateUserF
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def RegistrationView(request):
    form = CreateUserF()

    if request.method == "POST":
        form = CreateUserF(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('basic:home')

    context = {}
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('basic:home')
