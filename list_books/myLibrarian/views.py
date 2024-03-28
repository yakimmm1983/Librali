from django.shortcuts import render,redirect
from myLibrarian.services.bookService import GetAllBooks,SaveAllName,SaveRent,CreateRent as CreateRentService
from myLibrarian.forms import Booking
from myLibrarian.models import Rent
def main(request):
    return render(request,'main.html')

def returnMain(request):
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
    if request.method == 'POST':
        userName = request.POST.get("nameUser")
        callNumber = request.POST.get("callNumber")
        CreateRentService(userName, callNumber, bookId)
    return redirect("list")

def GetAllUser(request,user,books):
    user = SaveRent(user,books)
    rent = Rent.objects.all(userid = user.id)
    return render(request,'youBook.html',{'user':user,'books':books,'rent':rent})

