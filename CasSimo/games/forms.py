from django import forms

class RouletteForm(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "roulette-input",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))
    CONDITION_CHOICE=[('color','color'),
                      ('number','number'),
                      ('all','all')]

    condition = forms.ChoiceField(choices=CONDITION_CHOICE, required=True, initial="color",
                                  widget=forms.Select(attrs={"class": "form-control"}))

    CHOICES_COLOR = [('Red', 'Red'), ('Black', 'Black'), ('Green', 'Green')]
    bet_color = forms.ChoiceField(choices=CHOICES_COLOR, required=False,
                                  widget=forms.Select(attrs={"class": "form-control"}))
    
    bet_number = forms.IntegerField(min_value=0, max_value=36, required=True, initial=0,
                                    widget=forms.NumberInput(attrs={"class": "roulette-input",
                                                                    "style": "text-align:center",
                                                                    "step":1,
                                                                    "placeholder": "0 - 36"}))


class CoinFlipForm(forms.Form):
    bet_amount = forms.DecimalField(
        initial=1, min_value=1, max_value=10000, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "style": "text-align:center", "step": 0.5})
    )

    CHOICES = [('Heads', 'Heads'), ('Tails', 'Tails')]
    bet_side = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={"class": "coin-radio"}),
        initial='Heads',  # Set the initial value if needed
    )