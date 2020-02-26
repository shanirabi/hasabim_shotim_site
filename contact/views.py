# from django.shortcuts import render, get_object_or_404, redirect
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
# from django.conf import settings
# from django.template.loader import render_to_string
# from .forms import ContactForm
# from .models import Contact
#
# # Create your views here.
# def contact(request):
#     if request.method == 'POST':
#         fname = request.POST["fname"]
#         lname = request.POST["lname"]
#         eaddress = request.POST["eaddress"]
#         tel = request.POST["tel"]
#         message = request.POST["message"]
#
#         contact_reg_info = Contact(fname=fname, lname=lname, eaddress=eaddress, tel = tel, message=message)
#         contact_reg_info.save()
#
#         first_name =  request.POST['fname'] + " :שם פרטי "
#         last_name = request.POST['lname'] + " :שם משפחה "
#         email = request.POST['eaddress'] + " :אימייל "
#         phone_num = request.POST['tel'] + " :טלפון "
#         form_values = '\n'.join([first_name, last_name, phone_num, email])
#
#         send_mail('הודעה חדשה מהאתר',
#         form_values,
#         settings.EMAIL_HOST_USER,
#         ['rabbi.shani@gmail.com'],
#         fail_silently=False)
#         note = "פניתך התקבלה. נציגנו יצרו איתך קשר בקרוב!"
#     return render(request, 'contact/contact.html')
