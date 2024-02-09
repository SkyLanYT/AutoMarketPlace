from django.shortcuts import render


def index(request):
    return render(request, 'AutoMarketPlace/index.html')


def log_in(request):
    return render(request, 'AutoMarketPlace/log_in.html')


def reg(request):
    return render(request, 'AutoMarketPlace/reg.html')


def advertisement(request):
    return render(request, 'AutoMarketPlace/advertisement.html')
