from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string
from .forms import Event, EventForm
from .models import Event, EventRegistration
# Create your views here.
def events_list(request):
    events = Event.objects.all().order_by("-datetime_event")
    return render(request, 'events/list.html', {'events':events})

def event_detail(request, event_id):
    event_detail = get_object_or_404(Event, pk=event_id)
    form = EventForm()
    print(event_detail.price)
    return render(request, 'events/detail.html', {'event':event_detail, 'event_form':form})

def register_to_event(request):
    if request.method == 'POST':
        print("form submitted")
        event_id = request.POST["event_id"]
        title = request.POST["title"]
        datetime_event = request.POST["datetime_event"]
        location = request.POST["location"]
        price = request.POST["price"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        eaddress = request.POST["eaddress"]
        tel = request.POST["tel"]
        num_of_people = request.POST.get('num_of_people', 0)
        is_paid = False
        registration_status='submitted'
        print(event_id)

        event_reg_info = EventRegistration(event_id = event_id,title=title, datetime_event=datetime_event, location=location, price=price, fname=fname, lname=lname, eaddress=eaddress,tel = tel, num_of_people=num_of_people, is_paid = is_paid, registration_status=registration_status)
        event_reg_info.save()

        event_id =  request.POST["event_id"] + " :קוד פעילות "
        title = " שם הפעילות: " + request.POST["title"]
        datetime_event = request.POST["datetime_event"] + " :תאריך הפעילו ת"
        location = " מיקום הפעילות: " + request.POST["location"]
        price = request.POST["price"] + " :עלות הפעילות למשתתף "
        num_of_people = request.POST.get('num_of_people', 0) + " :מספר משתתפים "
        first_name =  request.POST['fname'] + " :שם פרטי "
        last_name = request.POST['lname'] + " :שם משפחה "
        email = request.POST['eaddress'] + " :אימייל "
        phone_num = request.POST['tel'] + " :טלפון "
        form_values = '\n'.join([event_id, title, location, datetime_event, price, num_of_people, first_name, last_name, phone_num, email])
        is_paid = False
        send_mail('הרשמה חדשה לפעילות',
        form_values,
        settings.EMAIL_HOST_USER,
        ['rabbi.shani@gmail.com'],
        fail_silently=False)
        note = "הרשמתך התקבלה. נציגנו יחזרו אליך בקרוב. תודה!"
    return redirect("events:thank_you")

def thank_you(request):
    return render(request, 'events/thank_you.html')
