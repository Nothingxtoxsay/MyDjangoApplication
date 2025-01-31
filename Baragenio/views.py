from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView

# Home Page View
class HomePageView(TemplateView):
    template_name = 'app/home.html'

# About Page View
class AboutPageView(TemplateView):
    template_name = 'app/about.html'

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page on successful login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "app/login.html")


def register_view(request):
    return render(request, 'app/register.html')