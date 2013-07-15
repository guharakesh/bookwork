from django.http import HttpResponse
from django.views.generic.base import View

class Index(View):
    def get(self, request):
        return HttpResponse("This is the bookwork homepage template")

