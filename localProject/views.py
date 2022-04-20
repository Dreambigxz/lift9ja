from django.shortcuts import redirect, render
from django.contrib import messages

def errorhandler404(request, exception):

    return redirect('/')


def errorhandler403(request, exception, template_name='trade/home.html'):
    return redirect('/')

def errorhandler(request):

    return redirect('/')
