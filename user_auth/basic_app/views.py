from django.shortcuts import render
from .forms import UserForm, ProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


import time
# Create your views here.
def index(request):
    return render(request, "basic_app/index.html")

def signup(request):
    signedup = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = ProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # save form data in model
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            return HttpResponseRedirect(redirect_to='login')

        else :
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = ProfileInfoForm()

    return render(request, "basic_app/signup.html", context={'user_form': user_form,
                                                                            'profile_form': profile_form,
                                                                            'signedup': signedup})

def user_login(request):
    context = {"user":None}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                print("Loging... ... ..", time.sleep(2))
                login(request,user)
                print("Successfully logged in....")
                time.sleep(2)
                return HttpResponseRedirect(redirect_to='/basicapp/')
            else:
                return HttpResponse("<h4>User is not active</h4>")
        else:
            print(f"Something went wrong with Username: {username} , Password: {password}")

    return render(request, "basic_app/login.html", context=context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(redirect_to="/basicapp")















