from django.shortcuts import redirect, render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'manage_book.html', {'books': books})

def add_book(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['txtCredits']
    book = Book.objects.create(code=code, name=name, credits=credits)
    return redirect('/')


def delete_book(request, code):
    book = Book.objects.get(code=code)
    book.delete()
    return redirect('/')


def edit_book(request, code):
    book = Book.objects.get(code=code)
    return render(request, 'edit_book.html', {'book': book})
    

def book_edition_done(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['txtCredits']
    book = Book.objects.get(code=code)
    book.name = name
    book.credits = credits
    book.save()
    return redirect('/') 

def us(request):
    return render(request, 'us.html')