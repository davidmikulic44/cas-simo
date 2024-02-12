from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainpage_index'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('add_funds/', views.add_funds, name='add_funds'),
    path('bet-history/',views.bet_history,name='bet_history'),

]