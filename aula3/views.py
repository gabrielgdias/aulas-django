from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

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

def show_code(request, code):
    html = '<h1> O código é {code}</h1>'
    response = HttpResponse(html)
    return response

def redirect_cat(request, cat):
    return HttpResponseRedirect('https://http.cat/'+str(cat))

def show_get_values(request):
    nome=request.GET.get('nome', None)
    if nome is None:
        html = '<h1>Bem vindo usuário anonimo</h1>'
    else:
        html = "<h1> Bem Vindo "+nome+"</h1>"
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head = ""
    if request.method == "POST":
        nome = request.POST.get("name")
        sobrenome = request.POST.get("sobrenome")
        head += "<h1> bem vindo " + nome + " " + sobrenome + "</h1>"

    html = """
    <form method=POST>
        <label for="fname">First name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="sobrenome" name="sobrenome"><br><br>
        <input type="submit" value="Submit">
    </form>
    """
    html_to_response = head + html
    return HttpResponse(html_to_response)