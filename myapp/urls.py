from django.contrib import admin
from django.urls import path
from myapp.views import *

admin.site.site_header = "Library Mamagement System"
admin.site.site_title = "Library Mamagement Admin Protal"
admin.site.index_title = "Welcome to Library Mamagement System"
urlpatterns = [
    path('', home, name='home'),
    path('user_login/', user_login, name='user_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('member_add/', member_add, name='member_add'),
    path('member_edit/<int:pid>', member_edit, name='member_edit'),
    path('member_delete/<int:pid>', member_delete, name='member_delete'),
    path('member_table/', member_table, name='member_table'),
    path('book_add/', book_add, name='book_add'),
    path('book_edit/<int:pid>', book_edit, name='book_edit'),
    path('book_delete/<int:pid>', book_delete, name='book_delete'),
    path('book_table/', book_table, name='book_table'),
    path('profile/', profile, name='profile'),
    path('issueBook/', issueBook, name='issueBook'),
    path('publisher_add/', publisher_add, name='publisher_add'),
    path('publisher_edit/<int:pid>', publisher_edit, name='publisher_edit'),
    path('publisher_table/', publisher_table, name='publisher_table'),
    path('publisher_delete/<int:pid>', publisher_delete, name='publisher_delete'),
    path('changePassword/', changePassword, name='changePassword'),
    path('search/', search, name='search'),
    path('search2/', search2, name='search2'),
    path('user_logout/', user_logout, name='user_logout'),
    path('viewRequestDetails/<int:pid>', viewRequestDetails, name='viewRequestDetails'),
]

