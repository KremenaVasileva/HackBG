from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message


def index(request):
    return render(request, "index.html")


def logged(request):

    if request.user.is_authenticated:
        return redirect('/home')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)
            return redirect("/home")

    return render(request, "logged.html", locals())


def home(request):
    messages = Message.objects.all().order_by("datetime")
    return render(request, "home.html", locals())


def logout_user(request):
    logout(request)
    return redirect('/')


def post_message(request):
    user = request.user
    content = request.POST['content']
    Message.objects.create(user=user, content=content)
