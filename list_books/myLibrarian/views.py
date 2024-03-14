from django.shortcuts import render
from myLibrarian.services.bookService import GetAllBooks

def main(request):
    return render(request,'main.html')

def redirect(request):
    return render(request,'main.html',)

def catalog(request):
    return render(request,'catalog.html')

def list(request):
    books = GetAllBooks()
    return render(request,'listBook.html',{"books":books})

def form(request):
    return render(request,'form.html')