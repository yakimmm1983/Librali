
from django import forms


class Booking(forms.Form):
    NameUser = forms.CharField(label='Ваше имя',max_length=20)
    callNumber = forms.CharField(label='Номер телефона',max_length=12)
