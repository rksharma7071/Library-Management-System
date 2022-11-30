from django import forms
from .models import *


class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['book_id', 'title', 'author', 'price', 'available', 'publisher']
    labels = {'book_id':'book_id', 'title':'title', 'author':'author', 'price':'price', 'available':'available', 'publisher':'publisher'}
    widgets = {
        'book_id': forms.TextInput(attrs={'class': 'form-select form-control', 'placeholder': 'Enter Book ID'},),
        'title': forms.TextInput(attrs={'class': 'form-select form-control', 'placeholder': 'Enter Title'}),
        'author': forms.TextInput(attrs={'class': 'form-select form-control', 'placeholder': 'Enter Author'}),
        'price': forms.TextInput(attrs={'class': 'form-select form-control', 'placeholder': 'Enter Price'}),
        'available': forms.TextInput(attrs={'class': 'form-select form-control'}),
        'publisher': forms.TextInput(attrs={'class': 'form-select form-control'}),
    }

class Brrowe_byForm(forms.ModelForm):
  class Meta:
    model = Brrowe_by
    fields = ['member', 'book']

class PublisherForm(forms.ModelForm):
  class Meta:
    model = Publisher
    fields = ['pub_id','name', 'address']
