from django.shortcuts import render

a = "Senai"
def home(request):
    return render (request, "page/home.html", context=
                   {'nome': a,                       
                   })

# Create your views here.
