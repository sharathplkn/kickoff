from django import forms
from .models import Team


class AuctionForm(forms.Form):
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        initial=20,
        label="Set Price"
    )

    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'radio-inputs'}),
        label="Select Team"
    )
