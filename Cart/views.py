from django.shortcuts import render

# Create your views here.
def Cart_view(request):
    return render(request,'Cart/checkout.html')