from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fname = forms.CharField(
            widget = forms.TextInput(
                attrs = {
                    "class": "form-control form-control-lg col-md-12 form-group" ,
                    "placeholder": "שם פרטי"
                            }
                    ),
                label=''
            )

    lname = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control form-control-lg col-md-12 form-group" ,
                "placeholder": "שם משפחה",
                    }
            ),
        label=''
    )

    eaddress = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control form-control-lg col-md-12 form-group",
                        "placeholder": "אימייל"
                        }
                    ),
                label=''
            )
    tel = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control form-control-lg col-md-12 form-group",
                        "placeholder": "טלפון"
                        }
                    ),
                label=''
            )
    message = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control form-control-lg col-md-12 form-group',
                    "placeholder": "הודעה"
                    }
                ),
            label=''
            )

    def clean_email(self):
        email = self.cleaned_data.get("eaddress")
        if not "@" in eaddress:
            raise forms.ValidationError("חובה להזין כתובת אימייל")
        return email

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
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data
