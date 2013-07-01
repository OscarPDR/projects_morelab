# coding: utf-8

from django.shortcuts import render_to_response
from django.contrib.auth import logout

# Create your views here.


#########################
# View: home
#########################

def home(request):
    return render_to_response('projects_morelab/index.html')


#########################
# View: logout
#########################

def logout_view(request):
    logout(request)
    return render_to_response('projects_morelab/index.html')


#########################
# View: view404
#########################

def view404(request):
    return render_to_response('projects_morelab/404.html')
