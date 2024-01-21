from django import forms


class ShoppingCartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Counts')