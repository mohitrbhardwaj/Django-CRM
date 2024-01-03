from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()


    # check to see if logging in
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in. Please try again...")
            return redirect('home')
    else: 
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Congrats! You have successfully Signed Up.")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    return render(request, 'signup.html', {'form': form})

def user_record(request, pk):
    if request.user.is_authenticated:
        # Look up records
        user_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'user_record': user_record})
    else:
        messages.success(request, "You must be logged in to access user records")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to access user records")
        return redirect('home')