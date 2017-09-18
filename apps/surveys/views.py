# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Hello World"
    return render(request,'index.html')

def postinfo(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    print request.session['attempt']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    print "it worked!"
    return redirect('/surveys/result')

def result(request):
    context = {
        'attempt': request.session['attempt'],
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment']
    }
    print context 
    return render(request, 'result.html',context)

# Create your views here.
