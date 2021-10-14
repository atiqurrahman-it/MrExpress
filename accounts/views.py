from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse, redirect
from accounts.forms import RegisterCreateUserForm
from userApp.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# email Register Email verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


# Create your views here.


def Register(request):
    if request.method == "POST":
        form = RegisterCreateUserForm(request.POST)
        if User.objects.filter(email=request.POST['email']).exists():
            messages.info(request, 'email already taken ')
            return HttpResponseRedirect(reverse('accounts:register'))
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            username = email.split('@')[0]
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already taken ')
                    return HttpResponseRedirect(reverse('accounts:register'))
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'already taken email')
                    return HttpResponseRedirect(reverse('accounts:register'))
                else:
                    # username is required  so ami to  register page theke username collect koreini tai ai vabe nilam
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                    username=username,
                                                    password=password)
                    # user.phone_number=phone_number if phone_number fields user in register page
                    # user.save(commit=False)
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    email_subject = 'Activate Your Account'
                    message = render_to_string('Account_page/confrim_emai.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': user.id,
                        'token': default_token_generator.make_token(user),
                    })
                    to_email = form.cleaned_data.get('email')
                    email = EmailMessage(email_subject, message, to=[to_email])
                    email.send()
                    return HttpResponse(
                        'We have sent you an email, please confirm your email address to complete registration')

                    # username = username
                    # password_raw = password
                    # user = authenticate(username=username, password=password_raw)
                    # login(request, user)
                    # current_user = request.user
                    # data = User_Profile()
                    # data.user_id = current_user.id
                    # data.image = "user_img/avatar.jpg"
                    # data.save()
            else:
                messages.info(request, 'password not matching ')
                return HttpResponseRedirect(reverse('accounts:register'))
        messages.info(request, 'form invalid')
        return HttpResponseRedirect(reverse('accounts:register'))
    form = RegisterCreateUserForm()
    data = {
        "form": form
    }
    return render(request, 'Account_page/register.html', data)


# # login when email verification  link
def activate(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
    except:
        raise Http404("No user found ")
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('MrExpressShop:homepage'))
    else:
        return HttpResponse('Activation link is invalid!')


def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('MrExpressShop:homepage'))
        else:
            # error show
            return HttpResponseRedirect(reverse('accounts:login'))

    return render(request, 'Account_page/login.html')


def LogOUt(request):
    logout(request)
    # messages.warning(request, 'Your are logged Out')
    return HttpResponseRedirect(reverse('MrExpressShop:homepage'))
