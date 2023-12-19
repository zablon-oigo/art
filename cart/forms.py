from django import forms

PRODUCT_QUANTITY_CHOICES=[(i, str(i)) for i in range(1, 4)]

class CartAddProductForm(forms.Form):
    #quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,label='', coerce=int,widget=forms.Select(attrs={
        #'class':''
    # }))
     # Adding a field to track the action of adding to the cart
    add_to_cart = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    override=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())
    