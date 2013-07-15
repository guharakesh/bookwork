from django.views.generic.base import View
from django.shortcuts import render

class Index(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

