
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")
def contact(request):
    return HttpResponse("This is the contact page.")
