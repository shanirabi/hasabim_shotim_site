from django.shortcuts import render
from .models import Vendor

# Create your views here.
def vendors_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/list.html', {'vendors':vendors})
