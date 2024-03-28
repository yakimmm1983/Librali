
from myLibrarian.models import Book,Rent,User

def GetAllBooks():
    return Book.objects.all()

def SaveAllName(cell,name):
    user = User()
    user.name = name
    user.cellPhoneNumber = cell
    user.save()
def SaveRent(user,books):
    rent = Rent()
    rent.user = user
    rent.books = books
    rent.save()
def GetUserById(userid):
    return User.objects.get(id = userid)
def GetRentsByUser(userId):
    user = GetUserById(userId)
    return Rent.objects.all(user = user)
def CreateRent(userName,userPhone,bookId):
    try:
        user = User.objects.get(cellPhoneNumber = userPhone)
    except:
        user = User()
        user.name = userName
        user.cellPhoneNumber = userPhone
        user.save()
    book = Book.objects.get(id = bookId)
    rent = Rent()
    rent.status = "Забронированно"
    rent.save()
    rent.user.add(user)
    rent.books.add(book)
    rent.save()


