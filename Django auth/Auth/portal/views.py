from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'portal/homepage.html')

def log_in(request):
    if request.method == 'POST':
        # Handle the form
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'portal/dashboard.html', {'user': user})
        else:
            return render(request, 'portal/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'portal/login.html')

def register(request):
    if request.method == 'POST':
        # Handle the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
      
        
        if password == confirm_password:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'portal/register.html', {'error': 'Username already exists'})
            else:
                # Check if the email already exists
                if User.objects.filter(email=email).exists():
                    return render(request, 'portal/register.html', {'error': 'Email already exists'})
                else:
                    # Create the user
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return render(request, 'portal/dashboard.html', {'success': 'User created successfully'})
                
        else:
            return render(request, 'portal/register.html', {'error': 'Passwords do not match'})
        
    else:
        return render(request, 'portal/register.html')

def log_out(request):
    logout(request)
    return render(request, 'portal/homepage.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'portal/dashboard.html', {'user': request.user})