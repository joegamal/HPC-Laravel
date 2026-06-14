from django.http import HttpResponse

# Create your views here.
def res(request):
    return HttpResponse("Hello, world. You're in your first app.")