from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

def edit(request, author_id):
  author = Author.objects.get(pk=author_id)
  context = { 'author': author }
  return render(request, 'books/edit.html', context)

def update(request, author_id):
  author = Author.objects.get(pk=author_id)
  author.name = request.POST['name']
  author.age = request.POST['age']
  author.save()

  authors = Author.objects.all()
  context = { 'authors': authors }
  return render(request, 'books/index.html', context)


def destroy(request, author_id):
  author = Author.objects.get(pk=author_id)
  author.delete()

  authors = Author.objects.all()
  context = { 'authors': authors }
  return render(request, 'books/index.html', context)

def create(request):
  print("----------------------create-------------------------------")
  print('name: %s' % request.POST['name'])
  author = Author(name=request.POST['name'], age=request.POST['age'])
  author.save()

  authors = Author.objects.all()
  context = { 'authors': authors }
  return render(request, 'books/index.html', context)

def new(request):
  return render(request, 'books/new.html', '')

def index(request):
  authors = Author.objects.all()
  context = { 'authors': authors }
  return render(request, 'books/index.html', context)

def show(request, author_id):
  author = Author.objects.get(pk=author_id)
  context = { 'author': author }
  return render(request, 'books/show.html', context)
