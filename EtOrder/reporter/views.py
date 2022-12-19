from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .models import Counties,Incidences
from Product.models import Order

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'

def data(request):
    order = serialize('geojson', Order.objects.all())
    return HttpResponse(order, content_type='json')

def counties(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')


def county_datasets(request):
    points = Order.objects.all()
    counties = Counties.objects.all()
    data = []

    for a in points:
        for c in counties:
            data.append(c.county)

    return JsonResponse(data,safe=False)

def point_datasets(request):
    points = Order.objects.all()
    county = Counties.objects.all().first()
    data = []

    for a in points:
        data.append(a)
    if data:
        final = serialize('geojson', data)
    else:
        final='null'


    return JsonResponse(final,safe=False)
'''
def individual_data(request,pk):
    print(pk)
    points = Order.objects.all()
    county = Counties.objects.filter(pk=pk).first()
    data = []

    for a in points:
        if Counties.geom.contains(a.location):
            data.append(a)
    if data:
        final = serialize('geojson', data)
    else:
        final='null'


    return JsonResponse(final,safe=False)

'''
