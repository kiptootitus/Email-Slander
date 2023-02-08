from django.http import HttpResponse
from django.template import loader

# Create your views here.
def mysite(request):
    template = loader.get_template('mysite.html')
    return HttpResponse(template.render())