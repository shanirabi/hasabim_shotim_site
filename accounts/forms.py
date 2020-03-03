from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
        email = forms.EmailField(
                widget=forms.EmailInput(
                        attrs={
                            "class": "form-control form-control-lg col-md-12 form-group",
                            # "placeholder": "כתובת מייל"
                            }
                        ),
                    label='כתובת מייל'
                )


class LoginForm(forms.Form):
    username = forms.CharField(
                widget=forms.TextInput(
                        attrs={
                            "class": "form-control form-control-lg col-md-12 form-group rtl",
                            # "placeholder": "שם משתמש"
                            }
                        ),
                    label='שם משתמש'
                )

    password = forms.CharField(
                    widget=forms.PasswordInput(
                            attrs={
                                "class": "form-control form-control-lg col-md-12 form-group rtl",
                                # "placeholder": "סיסמה"
                                }
                            ),
                        label='סיסמה'
                    )
    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(
                widget=forms.TextInput(
                        attrs={
                            "class": "form-control form-control-lg col-md-12 form-group rtl",
                            # "placeholder": "שם משתמש"
                            }
                        ),
                    label='שם משתמש'
                )

    email = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control form-control-lg col-md-12 form-group",
                        # "placeholder": "כתובת מייל"
                        }
                    ),
                label='כתובת מייל'
            )

    password = forms.CharField(
                    widget=forms.PasswordInput(
                            attrs={
                                "class": "form-control form-control-lg col-md-12 form-group rtl",
                                # "placeholder": "סיסמה"
                                }
                            ),
                        label='סיסמה'
                    )
    password2 = forms.CharField(
                    widget=forms.PasswordInput(
                            attrs={
                                "class": "form-control form-control-lg col-md-12 form-group rtl",
                                # "placeholder": "אימות סיסמה"
                                }
                            ),
                        label='אימות סיסמה'
                    )


    #
    # username = forms.CharField()
    # email    = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("שם משתמש תפוס, נא הזן שם משתמש אחר")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("כתובת המייל תפוסה, נא הזן כתובת אחרת")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("סיסמאות לא זהות, אנא ודא שהזנת סיסמה זהה")
        return data
