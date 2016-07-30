from django.shortcuts import render

from django.http import HttpResponse

def index(request):
  return HttpResponse("hello, word. you are at the client page.")

def show():
  return HttpResponse("hello, you are run in show page.")
