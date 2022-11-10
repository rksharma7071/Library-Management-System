from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('member_add/', views.member_add, name='member_add'),
    path('member_edit/<int:pid>', views.member_edit, name='member_edit'),
    path('member_delete/<int:pid>', views.member_delete, name='member_delete'),
    path('member_table/', views.member_table, name='member_table'),
    path('book_add/', views.book_add, name='book_add'),
    path('book_edit/<int:pid>', views.book_edit, name='book_edit'),
    path('book_delete/<int:pid>', views.book_delete, name='book_delete'),
    path('book_table/', views.book_table, name='book_table'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
]

