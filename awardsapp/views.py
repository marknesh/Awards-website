from django.shortcuts import render,redirect

def homepage(request):
    return  redirect('/accounts/login')

# Create your views here.
