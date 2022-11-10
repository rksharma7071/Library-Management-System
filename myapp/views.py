import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect(dashboard)
    

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect(user_login)
    
    total_book = Book.objects.all().count()
    total_member = Member.objects.all().count()
    return render(request, 'dashboard.html', locals())


def member_table(request):
    members = Member.objects.all()
    total_member = members.count()
    return render(request, 'member_table.html', locals())


def member_add(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == 'POST':
        memb_id = request.POST['memb_id']
        name = request.POST['name']
        memb_type = request.POST['memb_type']
        address = request.POST['address']
        # memb_date = request.POST['memb_date']
        # expiry_date = request.POST['expiry_date']

        try:
            Member.objects.create(memb_id=memb_id, name=name, memb_type=memb_type,address=address)
            error = "no"

        except Exception:
            error = "yes"
    return render(request, 'member_add.html', locals())

def member_edit(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    member = Member.objects.get(id = pid)
    error = ""
    if request.method == "POST":
        memb_id = request.POST['memb_id']
        name = request.POST['name']
        memb_type = request.POST['memb_type']
        address = request.POST['address']

        member.memb_id = memb_id
        member.name = name
        member.memb_type = memb_type
        member.address = address

        try:
            member.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'member_edit.html', locals())

def member_delete(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('member_table')


def book_add(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == 'POST':
        book_id = request.POST['book_id']
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        available = request.POST['available']
        publisher = request.POST['publisher']
        
        try:            
            Book.objects.create(book_id = book_id, title=title, author=author, price=price, available=available, publisher=publisher )
            error = "no"
        except Exception:
            error = "yes"
    return render(request, 'book_add.html', locals())


def book_table(request):
    books = Book.objects.all()
    total_book = books.count()
    return render(request, 'book_table.html', locals())

def book_edit(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    book = Book.objects.get(id = pid)
    error = ""
    if request.method == "POST":
        book_id = request.POST['book_id']
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        available = request.POST['available']

        book.book_id = book_id
        book.title = title
        book.author = author
        book.price = price
        book.available = available


        try:
            member.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'book_edit.html', locals())

def book_delete(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    book = Book.objects.get(id=pid)
    book.delete()
    return redirect('book_table')

def profile(request):
    pass
    # return render(request, 'profile.html')


def user_login(request):
    if not request.user.is_authenticated:
        error = ""
        if request.method == 'POST':
            u = request.POST['uname']
            p = request.POST['password']
            user = authenticate(username=u, password=p)
            try:
                if user.is_staff:
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except Exception:
                error = "yes"
        return render(request, 'login.html', locals())
    else:
        return redirect('dashboard')


def user_logout(request):
    logout(request)
    return redirect(home)
    # return render(request, 'login.html')

def error404(request, exception):
    return render(request, '404.html')