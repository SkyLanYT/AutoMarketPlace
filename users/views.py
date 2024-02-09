from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import RegisterUserForm, AuthenticationForm
from django.contrib.auth import logout, login
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from .models import Advertisement

def home(request):
    return HttpResponse("<h1>Home<h1>")


def index(request):
    return render(request, 'AutoMarketPlace/index.html')


class RegistrationUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'AutoMarketplace/reg.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class AuthUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'AutoMarketPlace/log_in.html'

    def get_success_url(self):
        return '/'


def logout_user(request):
    logout(request)
    return redirect('index')


def detail_user(request):
    return render(request, 'AutoMarketplace/logout.html')


def add_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.author = request.user
            advertisement.save()
            return redirect('home')
    else:
        form = AdvertisementForm()
    return render(request, 'AutoMarketPlace/advertisement.html', {'form': form})


def index(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'AutoMarketPlace/index.html', {'advertisements': advertisements})

