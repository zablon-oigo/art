from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','email','address','postal_code','city']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'px-6 py-4 rounded-lg border-2 border-gray-300 focus:outline-none'}),
            'last_name':forms.TextInput(attrs={'class':'px-6 py-4 rounded-lg border-2 border-gray-300 focus:outline-none'}),
            'email':forms.EmailInput(attrs={'class':'px-6 py-4 rounded-lg border-2 border-gray-300 focus:outline-none'}),
            'address':forms.TextInput(attrs={'class':'px-6 py-4 rounded-lg border-2 border-gray-300 focus:outline-none'}),
            'postal_code':forms.TextInput(attrs={'class':'px-6 py-4 rounded-lg border-2 border-gray-300 focus:outline-none'}),
            'city':forms.TextInput(attrs={'class':'px-6 py-4 rounded-lg border-2 border-gray-300 focus:outline-none'}),
        }
        