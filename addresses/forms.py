from django import forms

from .models import Address

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = (
            #'billing_profile',
            #'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            # 'state',
            'postal_code',
        )
        widgets = {
        'country': forms.TextInput(attrs={'readonly': 'readonly'}),
        'address_line_2': forms.TextInput(attrs={'type': 'number'}),

    }
        labels = {
            "address_line_1": "כתובת",
            "address_line_2": "דירה",
            "city": "עיר",
            "country": "מדינה",
            "postal_code": "מיקוד",
            # "state": "כתובת",
        }
