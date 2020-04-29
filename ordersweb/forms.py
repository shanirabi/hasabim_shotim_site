from django import forms
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

DELIVERY_METHOD_CHOICES = (
    ('pickup', 'איסוף עצמי'),
    ('shipping', 'משלוח בתשלום'),
)

class OrderWebForm(forms.Form):
    first_name = forms.CharField(
            widget = forms.TextInput(
                attrs = {
                    "class": "form-control form-control-lg col-md-12 form-group" ,
                    "placeholder": ""
                            }
                    ),
                label='שם פרטי'
            )

    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control form-control-lg col-md-12 form-group" ,
                "placeholder": "",
                    }
            ),
        label='שם משפחה'
    )

    email = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control form-control-lg col-md-12 form-group",
                        "placeholder": ""
                        }
                    ),
                label='כתובת מייל'
    )

    phone_number = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control form-control-lg col-md-12 form-group",
                        "placeholder": ""
                        }
                    ),
                label= 'טלפון'
            )

    address_line_1 = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg col-md-12 form-group",
                    "placeholder": ""
                    }
                ),
            label= 'רחוב'
            )

    # address_line_2 = forms.CharField(
    #         widget=forms.TextInput(
    #             attrs={
    #                 "class": "form-control form-control-lg col-md-12 form-group",
    #                 "placeholder": ""
    #                 }
    #             ),
    #         label='מספר בית'
    #         )

    city = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg col-md-12 form-group",
                    "placeholder": ""
                    }
                ),
            label='עיר'
            )

    country = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg col-md-12 form-group",
                    "placeholder": "",
                    "readonly": "readonly",
                    },

                ),
            initial ='ישראל',
            label='מדינה'
            )

    postal_code = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg col-md-12 form-group",
                    "placeholder": ""
                    }
                ),
            label='מיקוד'
            )

    delivery_method = forms.ChoiceField(
            widget=forms.Select(
                attrs={
                    "class": "form-control form-control-lg col-md-12 form-group",
                    "placeholder": ""
                    }
                ),
            label='צורת אספקה',
            choices=DELIVERY_METHOD_CHOICES,
            )

    approve_terms_and_age_above_18 = forms.CharField(
            widget=forms.CheckboxInput(
                attrs={
                    "class": "checkbox",
                    "placeholder": ""
                    }
                ),
            label= mark_safe('אני מאשר/ת שקראתי את  <a href="terms" target="_blank">התקנון</a> ושאני מעל גיל 18 ' )
            )
