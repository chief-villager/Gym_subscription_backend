from typing import Any
from django.shortcuts import render, redirect
from .forms import  UserRegistrationForm
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login
from .models import Plan,UserPlan,User
from django.contrib import messages
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta




def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST ['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('alangba')
            login(request,user)
            return redirect('/Gym/homepage/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect ("/Gym/login")
    return render(request,'subscription_app/login.html')


@login_required(login_url="/Gym/login")
def home_page(request):
    plan = Plan.objects.all()
    return render(request,"subscription_app/homepage.html",{'plan': plan})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            email_subject = 'Welcome to our website!'
            email_body = 'Thank you for registering with our website.'
            from_email = 'noreply@example.com'
            to_email = [user.email]

            email = EmailMessage(
                email_subject,
                email_body,
                from_email,
                to_email,
            )
            email.send()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/Gym/homepage/')
    else:
        form = UserRegistrationForm()
    return render(request, 'subscription_app/register.html', {'form': form})


@login_required(login_url="/Gym/login")
def select_page(request,id):
    if request.user.is_authenticated:
        userplan = UserPlan(request.user)
        user = User.objects.get(username = request.user)
        if request.method == "GET":
            select_plan = Plan.objects.get(id = id)
            existing_user_filter = UserPlan.objects.filter(user = user)
            userplan = existing_user_filter.first()
            if userplan is not None:
                existing_user_filter.update(plan=select_plan)
            else:
                userplan, created = UserPlan.objects.get_or_create(user=user, plan = select_plan)
            context = {
                'select_plan':select_plan,
                'new_userplan': userplan,
                'user':user
            }
        return render(request,'subscription_app/select.html',context)


@login_required(login_url="/Gym/login")
def confirm_payment(request):
    data = json.loads(request.body)
    reference = data.get('reference')
    userplan = data.get('userplan')
    if request.method == 'POST':
        userplan_id = UserPlan.objects.get(id = userplan)
        if  reference:
            userplan_id.is_Active = True
            userplan_id.save()
            print(userplan_id)
            print("shola")
            user_plan = UserPlan.objects.filter(user=request.user, is_Active=True).first()
            if user_plan:
                user_plan.end_date = timezone.now().date() + timedelta(days=30)
                user_plan.save()
                print(userplan)

            return redirect ("/Gym/login")










