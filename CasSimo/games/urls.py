from django.urls import path
from . import views

urlpatterns = [
    path('coinflip/', views.coin_flip, name='coin_flip'),
    path('roulette/',views.roulette,name='roulette'),

]
