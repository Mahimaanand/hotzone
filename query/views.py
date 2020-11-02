from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Location

# Create your views here.
def index(request):
    ctx = {'inp': '', 'res': ''}
    return render(request, 'query/index.html', {'notFound':False, 'Added':False})


def inquiry(request):
    search_input = request.GET.get('inquiry')
    result = requests.get(f'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q={search_input}')
    try:
        json_result = json.loads(result.text)
    except:
        return render(request, 'query/index.html', {'inp': search_input, 'notFound':True})
    location = json_result[0]
    name = location['nameEN']
    address = location['addressEN']
    x_coordinate = location['x']
    y_coordinate = location['y']
    ctx = {
        'input': search_input,
        'name': name,
        'address':address,
        'x': x_coordinate,
        'y': y_coordinate
    }
    return render(request, 'query/index.html', ctx)

def add_data_to_db(request):
    name = request.GET.get('name')
    address = request.GET.get('address')
    x_coordinate = request.GET.get('x')
    y_coordinate = request.GET.get('y')
    L = Location(name = name, address = address, x_coordinates = x_coordinate, y_coordinates = y_coordinate)
    L.save()
    ctx = {'inp': '', 'Added': True, 'notFound': False}
    return render(request,'query/index.html', ctx)


            