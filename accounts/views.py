from django.contrib import messages,auth
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account


# USER REGISTRATION VIEWs
def register(request):
    """
        Handle user registration.

        Validates the registration form submitted via POST request.
        If valid, creates a new user account and redirects to registration page with success message.
        If invalid, redirects back to registration page with error messages displayed.

        Args:
        - request: HTTP request object

        Returns:
        - HTTP response redirecting to registration page

        """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.phone_number = phone
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('register')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
