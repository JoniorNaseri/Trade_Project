from django.shortcuts import render, redirect
from .forms import MyUserForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from history.models import Trade
from django.views import generic


def register(request):
    if request.method == "POST":
        form = MyUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save()
            login(request, user)
            messages.success(request, f"User {username} was created successfully!")
            return redirect('trade_list')

        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = MyUserForm()
    return render (request, 'users/register.html', {'form' : form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Dear {username} you have logged in successfully!")
                return redirect('trade_list')
            else:
                messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form' : form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have logged out seccessfully!")
    return redirect('trade_list')



def profile_view(request):
    user = request.user

    profile = Profile.objects.get(user=user)

    # Get current trade stats from database
    total_trades = Trade.objects.filter(user=user).all().count()
    successful_trades = Trade.objects.filter(user=user).filter(trade_result="SUCCESS").count()
    failed_trades = Trade.objects.filter(user=user).filter(trade_result="FAILED").count()

    if total_trades > 0:
        # Calculate the win rate
        win_rate = successful_trades / total_trades * 100
    else:
        # Set the win rate to zero
        win_rate = 0

    # Add context
    context = {
        'profile': profile,
        'win_rate': win_rate,
        'successful_trades': successful_trades,
        'failed_trades': failed_trades,
        'total_trades': total_trades,
    }

    return render(request, 'users/profile.html', context)