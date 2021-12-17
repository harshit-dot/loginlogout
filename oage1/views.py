from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import  User
from django.contrib import messages


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password1!=password:
            messages.error(request, 'Password not Matched')
            return redirect('/')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password Wrong')

            return redirect('/')
def main(request):
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']

        password=request.POST['password']

        password1=request.POST['password1']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        if username=='' or password=='' or password1=='' or first_name=='' or last_name=='' or email=='':
            messages.error(request,'Enter All The Fields')
            return redirect('/')


        if password1!=password:
            messages.error(request,'Password Not Matched')

            return redirect('/')
        bog = User.objects.get(username=username)
        if bog is not None:
            messages.error(request, 'Username already exists')

            return redirect('/')



        send_mail(
            'Wow you have just signed up in LoginLogoutSystem',
            'congratulations your account is now setup. you can login through the main website and enjoy.....',
            'loginlogoutsystem@gmail.com',
            [email],
            fail_silently=False,
        )
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.success(request, 'User Created')
        return redirect('/')





def logout(request):
    auth_logout(request)
    return redirect('/')
def forgot(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']

        if email=='' or username=='':
            messages.error(request,'Enter All The Fields')
            return redirect('forgot')
        bog=User.objects.get(username=username, email=email)
        if bog is None:
            messages.error(request,'Username or Password Wrong')

            return redirect('/')


        harsh='This is the link, click it http://loginlogoutsystems.herokuapp.com/forgotpass/'+str(bog.id)
        print(harsh)
        print(bog.password)
        send_mail(
            'Click the link to change your password LoginLogoutSystem',
            harsh,
            'loginlogoutsystem@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Mail has been sent to your email address.')
        return render(request, 'index.html')

    else:
        return render(request, 'forgot.html')


def forgotpass(request, id):


    bog = get_user_model().objects.get(id=int(id))
    return render(request, 'forgetpass.html', {'bog': bog})
def changepassword(request,id):
    if request.method=='POST':
        password=request.POST['password']
        password1=request.POST['password1']
        if password!=password1:
            messages.error(request,'Password Not Matched')
            bog = get_user_model().objects.get(id=int(id))
            return render(request, 'forgetpass.html', {'bog': bog})
        bog = get_user_model().objects.get(id=int(id))
        bog.set_password(password)
        bog.save()
        messages.success(request,'Password Changed')
        return render(request, 'index.html')


