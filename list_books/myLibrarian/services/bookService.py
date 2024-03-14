
from myLibrarian.models import Book,Rent

def GetAllBooks():
    return Book.objects.all()

