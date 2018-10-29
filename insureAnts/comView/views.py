from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, "comView/login.html")


def about(request):
    return  render(request, "comView/about.html")


def index(request):
    return render(request, "comView/index.html")


def tables(request):
    context = { 'posts' : Post.objects.all()}
    return render(request, "comView/tables.html", context)


def charts(request):
    return render(request, "comView/charts.html")


def forgot(request):
    return render(request, "comView/forgot-password.html")

