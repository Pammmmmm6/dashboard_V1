from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {'fieldValues': request.POST}

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password is too short !')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account successfully created ! Now you can login.')
                return render(request, 'authentication/login.html')

        messages.error(request, 'The email or the username is already taken.')
        return render(request, 'authentication/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, 'Welcome, ' + user.username + ' you are now logged in ! ')
                return redirect('trade')

            messages.error(request, 'Invalid informations, try again ! ')
            return render(request, 'authentication/login.html')

        messages.error(request, 'Please fill all fields. ')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out, see you soon !')
        return redirect('login')
