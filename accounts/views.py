from django.shortcuts import render,HttpResponseRedirect,reverse,HttpResponse
from accounts.forms import RegisterCreateUserForm
from userApp.models import User
# Create your views here.

def Register(request):
    if request.method == "POST":
        form = RegisterCreateUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0] # username is required  so ami to  register page theke username collect koreini tai ai vabe nilam
            user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            # user.phone_number=phone_number if phone_number fields user in register page
            user.save()
            return HttpResponseRedirect(reverse('accounts:login'))

    form=RegisterCreateUserForm()
    data={
        "form":form
    }
    return render(request,'Account_page/register.html',data)

def Login(request):
    return render(request,'Account_page/login.html')

def LogOUt(request):
    pass


