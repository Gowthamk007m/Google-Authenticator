from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# from .forms import SignUpForm


# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("frontpage")
#     else:
#         form = SignUpForm()

#     return render(request, 'core/signup.html', {'form': form})

@login_required
def profile_view(request):
    
    return render(request,'account.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Use the authenticate method to check the user's credentials
            user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # Use the login method to log the user in
                login(request, user)

                # Redirect to your desired page after login
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    # Include non-field errors in the context
    non_field_errors = form.non_field_errors()

    return render(request, 'account/login.html', {'form': form, 'non_field_errors': non_field_errors})


    # Your code to use the retrieved information goes here
