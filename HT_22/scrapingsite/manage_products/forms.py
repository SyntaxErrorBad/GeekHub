from django import forms


class AddProductsForm(forms.Form):
    product_ids = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
