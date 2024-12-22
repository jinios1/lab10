from django.http import HttpResponse

def nested_home(request):
    return HttpResponse("<h2>Welcome to the Nested App Home!</h2>")

def nested_about(request):
    return HttpResponse("<h2>About the Nested App</h2>")

def nested_contacts(request):
    return HttpResponse("<h2>Contacts Page of Nested App</h2>")
