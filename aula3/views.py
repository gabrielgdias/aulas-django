from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

def index(request):
    html = "<h1>Bem Vindo</h1>"
    response = HttpResponse(html)
    response['ultimo_acesso'] = timezone.localtime(timezone.now())
    return response

def setacookie(request):
    response = HttpResponse()
    response.set_cookie("my_name", value='Gabriel')

    return response

def redireciona(request):
    return HttpResponseRedirect('https://uol.com.br')