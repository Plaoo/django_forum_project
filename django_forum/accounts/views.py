from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm


def registrationView(request):
    if request.methos == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            User.objects.create_user(username = username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponsePermanentRedirect("/")
        else:
            form = RegistrationForm()
        context = {"form": form}
        return render(request, 'accounts/registration.html', context)