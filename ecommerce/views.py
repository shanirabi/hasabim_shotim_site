from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, LoginForm, RegisterForm
from contact.models import Contact
from vendors.models import Vendor



def terms(request):
    return render(request, "terms.html")


def about(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render(request, "about.html", context)

def homepage(request):
    vendors = Vendor.objects.all()
    return render(request, "homepage.html",{'vendors':vendors})

    # return render(request, "homepage.html")


def contact(request):
    contact_form = ContactForm()
    # context = {
    #     "title": "Contact",
    #     "content": "",
    #     "form": contact_form,
    #     "note": ""
    # }

    note = "אתם מוזמנים לפנות אלינו בכל שאלה. אנחנו מבטיחים לחזור אליכם בהקדם"
    if request.method == "POST":
                fname = request.POST["fname"]
                lname = request.POST["lname"]
                eaddress = request.POST["eaddress"]
                tel = request.POST["tel"]
                message = request.POST["message"]

                # print(request.POST.get('fname'))
                # print(request.POST.get('lname'))
                # print(request.POST.get('eaddress'))
                # print(request.POST.get('tel'))
                # print(request.POST.get('message'))

                contact_reg_info = Contact(fname=fname, lname=lname, eaddress=eaddress, tel = tel, message=message)
                contact_reg_info.save()
                #email alert
                subject = 'צור קשר - אתר הסבים שותים'

                alert_message = "{alert_fname}\n{alert_lname}\n{alert_eaddress}\n{alert_tel}\n{alert_message}".format(
                        alert_fname = "שם פרטי: " + fname,
                        alert_lname = "שם משפחה: " + lname,
                        alert_eaddress = "אימייל: " + eaddress,
                        alert_tel = "טלפון: " + tel,
                        alert_message= "הודעה: " + message,
                    )
                from_email = settings.EMAIL_HOST_USER
                to_list_alert = ['rabbi.shani@gmail.com']
                send_mail(subject, alert_message, from_email, to_list_alert, fail_silently = True)

                note = "פנייתך התקבלה, אנו ניצור איתך קשר בהקדם"
    return render(request, "contact/view.html", {'form':contact_form ,'note':note})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)

def logout_request(request):
    logout(request)
    return redirect("/")


User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
