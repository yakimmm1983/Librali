from django.shortcuts import render
from myLibrarian.services.bookService import GetAllBooks,SaveAllName,SaveRent,CreateRent
from myLibrarian.forms import Booking
from myLibrarian.models import Rent
def main(request):
    return render(request,'main.html')

def redirect(request):
    return render(request,'main.html',)

def catalog(request):
    return render(request,'catalog.html')

def list(request):
    books = GetAllBooks()

    return render(request,'listBook.html',{"books":books})

def form(request,bookId):
    form = Booking()
    return render(request,'form.html',{"form":form,"bookid":bookId})

def youBook(requect):
    return render(requect,"youBook.html")
def GetRent():
    return SaveRent()
def CreateRent(request,bookId):
    userName=nameUser
    callNumber=callNumber
    CreateRent(userName, callNumber, bookId)
    return redirect("list")

# def GetAllUser(request,user,books):
#     user = SaveRent(user,books)
#     rent = Rent.objects.all(user.id = user.id)
#     return render(request,'youBook.html',{'user':user,'books':books})

