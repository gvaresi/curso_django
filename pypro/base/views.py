from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('<html lang="pt-br">'
                        '<head> <meta charset=UTF-8> </head>'
                        '<body> Olá Django, Versão 40 </body>'
                        '</html>')
