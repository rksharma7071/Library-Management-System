import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime
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

    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        try:
            memberSearch = Member.objects.filter(Q(memb_id=sd) | Q(name__icontains=sd) | Q(address__icontains=sd))
        except:
            memberSearch = ""

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
        name = request.POST['name']
        memb_type = request.POST['memb_type']
        address = request.POST['address']

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
    # error = ""
    publisher = Publisher.objects.all()
    book = BookForm(request.POST)
    if request.method == "POST":
        try:
            if book.is_valid():
                book.save()
                error = "no"
                book = BookForm()
        except:
            book = BookForm()
            error = 'yes'
   
    return render(request, 'book_add.html', locals())


def book_table(request):
    books = Book.objects.all()

    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        try:
            bookSearch = Book.objects.filter(Q(book_id=sd) | Q(title__icontains=sd) | Q(author__icontains=sd) | Q(publisher__icontains=sd))
        except:
            bookSearch = ""
    return render(request, 'book_table.html', locals())

def book_edit(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    book = Book.objects.get(id = pid)
    publisher = Publisher.objects.all()
    error = ""
    if request.method == "POST":
        book_id = request.POST['book_id']
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        available = request.POST['available']
        publisher = request.POST['publisher']

        book.book_id = book_id
        book.title = title
        book.author = author
        book.price = price
        book.available = available
        book.publisher = publisher


        try:
            book.save()
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



def issueBook(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    form = Brrowe_byForm(request.POST)

    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
                error = "no"
                form = Brrowe_byForm()
        except:
            form = Brrowe_byForm()
            error = 'yes'


    books = Book.objects.all()
    return render(request, 'issueBook.html', locals())


def viewRequestDetails(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    form = Brrowe_byForm(request.POST)
    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
                error = "no"
                form = Brrowe_byForm()
        except:
            form = Brrowe_byForm()
            error = 'yes'

    member = Member.objects.get(id=pid)
    issue = Brrowe_by.objects.filter(member=member)
    issue_count = issue.count()
    return render(request, 'viewRequestDetails.html', locals())



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


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'admin/changePassword.html', locals())


def search(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        try:
            member = Member.objects.filter(Q(name__icontains=sd) | Q(memb_id=sd) | Q(address__icontains=sd))
        except:
            member = ""
    return render(request, 'search.html', locals())


def search2(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        try:
            member = Member.objects.filter(Q(name__icontains=sd) | Q(memb_id=sd) | Q(address__icontains=sd))
        except:
            member = ""
    return render(request, 'search2.html', locals())


def user_logout(request):
    logout(request)
    return redirect(home)
    # return render(request, 'login.html')


def publisher_add(request):
    publisher = PublisherForm(request.POST)
    if request.method == 'POST':
        try:
            if publisher.is_valid():
                pub_id = request.POST['pub_id']
                name = request.POST['name']
                address = request.POST['address']
                pub = Publisher(pub_id=pub_id, name=name, address=address)
                pub.save()
                error = "no"
                publisher = PublisherForm()
        except:
            publisher = PublisherForm()
            error = 'yes'
    return render(request, 'publisher_add.html', locals())


def publisher_edit(request, pid):
    publisher = Publisher.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        pub_id = request.POST['pub_id']
        name = request.POST['name']
        address = request.POST['address']

        publisher.pub_id = pub_id
        publisher.name = name
        publisher.address = address

        try:
            publisher.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'publisher_edit.html', locals())


def publisher_table(request):
    publishers = Publisher.objects.all()
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        try:
            pubSearch = Publisher.objects.filter(Q(pub_id=sd) | Q(name__icontains=sd) | Q(address__icontains=sd))
        except:
            pubSearch = ""
    return render(request, 'publisher_table.html', locals())


def publisher_delete(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    publisher = Publisher.objects.get(id=pid)
    publisher.delete()
    return redirect('publisher_table')