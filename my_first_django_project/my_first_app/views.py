from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse

def redirect_example(request):

    return redirect('hello_world', name='Anton')

def hello_world(request, name=None):
    response_text = "<h1>Hello, World!</h1>"
    if name:
        response_text = f"<h1>Hello, {name}!</h1>"
    
    age = request.GET.get('age')
    if age:
        response_text = f"<h1>Hello, {name}! You are {age} years old.</h1>"
    
    response = HttpResponse(response_text)
    
    if name:
        response.set_cookie('username', name)
    
    return response


def json_example(request):
    data = {
        'name': 'Andtei',
        'age': 21,
        'city': 'Muho'
    }
    return JsonResponse(data)

def show_cookies(request):
    cookies = request.COOKIES
    
    cookies_list = [f"<li>{key}: {value}</li>" for key, value in cookies.items()]
    html_content = "<h1>Cookies:</h1><ul>" + "".join(cookies_list) + "</ul>"
    return HttpResponse(html_content)
