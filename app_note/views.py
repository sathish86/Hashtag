from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context_dict = {'test_data': "Test data"}
    return render(request, 'app_note/index.html', context_dict)