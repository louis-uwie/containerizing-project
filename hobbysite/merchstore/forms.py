from django import forms

from .models import Product, Transaction

class TransactionForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, label="quantity")


    class Meta:
        model = Transaction
        fields = ["quantity"]


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["owner"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].widget = forms.HiddenInput()