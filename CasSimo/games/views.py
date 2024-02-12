from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
import random
from .forms import CoinFlipForm, RouletteForm  
from mainpage.models import User
from django.utils import timezone
from mainpage.models import BetHistory

def games(request):
    context = {}
    return render(request, 'games/index.html', context)

@login_required(login_url='login')
def coin_flip(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')
    multiplier = Decimal(2)
    

    form = CoinFlipForm()
    if request.method == "POST":
        form = CoinFlipForm(request.POST)
        if form.is_valid():
            
            bet_amount = form.cleaned_data['bet_amount']
            bet_side = form.cleaned_data['bet_side']
            messages.info(request, 'test')


            if user.money >= bet_amount:
                user.money -= bet_amount
                user.save()
                
      
                
                coin_result = random.choice(['Heads', 'Tails'])
                if coin_result == bet_side:
                    BetHistory.objects.create(
                        user=user,
                        game='Coin Flip',
                        bet_amount=bet_amount,
                        win_amount=bet_amount * multiplier,
                        timestamp=timezone.now(),
                    )
                    user.money += (bet_amount * multiplier)
                    user.save()

                    main_account.money -= (bet_amount * multiplier)
                    main_account.save()
                    messages.success(request, f'You won {round(bet_amount*multiplier,2)}€! {coin_result}')
                    
                else:
                    BetHistory.objects.create(
                        user=user,
                        game='Coin Flip',
                        bet_amount=bet_amount,
                        win_amount=Decimal(0),
                        timestamp=timezone.now(),
                    )
                    messages.error(request, f'You lose! {coin_result}')
                    main_account.money += bet_amount
                    main_account.save()
                    user.save()


            else:
                messages.error(request, "You don't have enough money")


    context = {
        'form': form
    }

    return render(request, 'games/play_coin_flip.html', context)

@login_required(login_url='login')
def roulette(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')
    color_multiplier = Decimal(2)  
    combined_multiplier = Decimal(5.0)  
    green_multiplier=Decimal(10.0)
    number_multiplier=Decimal(2.0)
    form = RouletteForm()
    
    if request.method == "POST":
        
        form = RouletteForm(request.POST)
        if form.is_valid():
            
            bet_amount = form.cleaned_data['bet_amount']
            bet_color = form.cleaned_data['bet_color']
            bet_number = form.cleaned_data['bet_number']
            condition=form.cleaned_data['condition']
        
            if user.money >= bet_amount:
                user.money -= bet_amount
                user.save()


                roulette_result = random.randint(0, 36) 

                if (roulette_result == 0):
                    color='Green'
                elif (roulette_result % 2 == 1):
                    color='Black'
                else:
                    color='Red'

                color_win_condition = (color=='Red' and bet_color == 'Red') or (color=='Black' and bet_color == 'Black')
                green_win_condition = color=='Green' and bet_color=='Green'
                                      

                number_win_condition = (roulette_result == bet_number)

                
                if green_win_condition:
                    user.money += (bet_amount *green_multiplier)
                    BetHistory.objects.create(
                        user=user,
                        game='Roulette',
                        bet_amount=bet_amount,
                        win_amount=bet_amount * green_multiplier,
                        timestamp=timezone.now(),
                    )
                    user.save()

                    main_account.money -= (bet_amount * green_multiplier)
                        
                    main_account.save()

                    messages.success(request, f'You won {bet_amount * combined_multiplier}! The ball landed on color {color}, number {roulette_result}')



                elif condition=='all':
                    if color_win_condition and number_win_condition:
                        
                        user.money += (bet_amount * combined_multiplier)
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=bet_amount * combined_multiplier,
                            timestamp=timezone.now(),
                        )
                        user.save()
                        main_account.money -= (bet_amount * combined_multiplier)
                        main_account.save()
                        messages.success(request, f'You won {bet_amount * combined_multiplier}! The ball landed on color {color}, number {roulette_result}')

                    else:
                        messages.error(request, f'Sorry, not this time.. The ball landed on color {color}, number {roulette_result}')
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=Decimal(0),
                            timestamp=timezone.now(),
                        )
                        main_account.money += bet_amount           
                        main_account.save()
                        user.save()
                    
                elif condition=='color':
                    if color_win_condition:
                        user.money += (bet_amount * color_multiplier)
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=bet_amount * color_multiplier,
                            timestamp=timezone.now(),
                        )
                        user.save()

                        main_account.money -= (bet_amount * color_multiplier)
                        
                        main_account.save()

                        messages.success(request, f'You won {bet_amount * color_multiplier}! The ball landed on color {color}, number {roulette_result}')
                    else:
                        messages.error(request, f'Sorry, not this time.. The ball landed on color {color}, number {roulette_result}')
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=Decimal(0),
                            timestamp=timezone.now(),
                        )
                        main_account.money += bet_amount           
                        main_account.save()
                        user.save()

                elif condition=='number':
                    if number_win_condition:
                        user.money+=(bet_amount*number_multiplier)
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=bet_amount * number_multiplier,
                            timestamp=timezone.now(),
                        )
                        user.save()
                        main_account.money-=(bet_amount*number_multiplier)
                        main_account.save()
                        messages.success(request, f'You won {bet_amount * number_multiplier}! The ball landed on color {color}, number {roulette_result}')

                    else:
                        messages.error(request, f'Sorry, not this time.. The ball landed on color {color}, number {roulette_result}')
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=Decimal(0),
                            timestamp=timezone.now(),
                        )
                        main_account.money += bet_amount           
                        main_account.save()
                        user.save()


                        
            
                else:
                        messages.error(request, f'Sorry, not this time.. The ball landed on color {color}, number {roulette_result}')
                        BetHistory.objects.create(
                            user=user,
                            game='Roulette',
                            bet_amount=bet_amount,
                            win_amount=Decimal(0),
                            timestamp=timezone.now(),
                        )
                        main_account.money += bet_amount           
                        main_account.save()
                        user.save()


                                            
                    
                    


            else:
               messages.error(request, "You don't have enough money")
    
    context = {
        'form': form
    }
    
    return render(request, 'games/play_roulette.html', context)

