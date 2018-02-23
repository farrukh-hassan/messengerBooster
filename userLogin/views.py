from django.http import HttpResponse
from django.template import loader
from .models import userLogin

def index(request):
    users = userLogin.objects.all()
    template = loader.get_template('')
    return HttpResponse()
def username(request, username):
    return HttpResponse('''<h1>this is the user page</h1><br>''')