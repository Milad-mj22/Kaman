
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect

from main.forms import DemoUserForm
from .models import BusinessArea, CompanySize, PhoneLead
from django.utils import timezone

def register_phone(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', '').strip()
        if phone.startswith('09') and len(phone) == 11:
            PhoneLead.objects.create(
                phone=phone,
                created_at=timezone.now(),
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
            request.session['phone_number'] = phone
            return redirect('fill_info')  # صفحه بعد برای پر کردن اطلاعات

    return redirect('/')




def fill_info(request):
    # Get phone number from session
    phone_number = request.session.get('phone_number', None)

    if not phone_number:
        return redirect('enter_demo')  # Redirect to enter demo page if no phone number is set

    # Handle the form submission for additional info
    if request.method == 'POST':
        form = DemoUserForm(request.POST)
        if form.is_valid():
            demo_user = form.save(commit=False)
            demo_user.phone = phone_number  # Use phone number from session
            demo_user.save()
            messages.success(request, "کد تایید به شماره شما ارسال شد.")
            return redirect('verify_code')  # Redirect to verify code page

    else:
        form = DemoUserForm()

    # Fetch options for company size and business area
    company_sizes = CompanySize.objects.all()
    business_areas = BusinessArea.objects.all()

    return render(request, 'register/fill_info.html', {
        'form': form,
        'phone_number': phone_number,
        'company_sizes': company_sizes,
        'business_areas': business_areas
    })




def home(request):

    return render(request, 'home/home.html')



def about(request):
    return render(request, "home/about.html", {"active": "about"})

def products(request):
    # create a products.html extending base.html similar to about.html
    return render(request, "products.html", {"active": "products"})

def demo(request):
    return render(request, "demo.html", {"active": "demo"})

def contact(request):
    return render(request, "home/contact.html", {"active": "contact"})



def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)