from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseBadRequest
from django.conf import settings
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)




def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_url = request.build_absolute_uri(f"/password_reset_confirm/{uid}/{token}/")

            subject = 'Password Reset Request'
            message = f'Hi {user.username},\n\nClick the link below to reset your password:\n{reset_url}'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

            return redirect('password_reset_done')

    return render(request, 'users/password_reset.html')


def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')

            if password == password_confirm:
                user.set_password(password)
                user.save()
                return redirect('password_reset_complete')
            else:
                return HttpResponseBadRequest('Passwords do not match.')

        return render(request, 'users/password_reset_confirm.html', {'validlink': True})
    else:
        return render(request, 'users/password_reset_confirm.html', {'validlink': False})


def password_reset_complete(request):
    return render(request, 'users/password_reset_complete.html')