import random
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    alfabet = [chr(i) for i in range(97, 123)]
    alfabet_upper_case = [chr(i).upper() for i in range(97, 123)]

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        alfabet.extend(alfabet_upper_case)

    if request.GET.get('special'):
        alfabet.extend('!@#$%^&*()_')

    if request.GET.get('numbers'):
        alfabet.extend('1234567890')
    the_password = ''

    for i in range(length):
        the_password += random.choice(alfabet)

    return render(request, 'generator/password.html', {'password': the_password})
