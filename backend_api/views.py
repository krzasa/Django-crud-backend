from django.http import JsonResponse
from .models import Wood
from .models import Lighting
from .models import Appliances
from .models import Paint
from .models import Landscaping

def all_products(request):
    all_products = {
        'wood': list(Wood.objects.values()),
        'lighting': list(Lighting.objects.values()),
        'appliances': list(Appliances.objects.values()),
        'paint': list(Paint.objects.values()),
        'landscaping': list(Landscaping.objects.values())
    }
    return JsonResponse(all_products)

def wood_list(request):
    woods = Wood.objects.all()
    data = {'wood': list(woods.values())}
    return JsonResponse(data)

def lighting_list(request):
    lightings = Lighting.objects.all()
    data = {'lighting': list(lightings.values())}
    return JsonResponse(data)

def appliance_list(request):
    appliances = Appliances.objects.all()
    data = {'appliances': list(appliances.values())}
    return JsonResponse(data)

def paint_list(request):
    paints = Paint.objects.all()
    data = {'paint': list(paints.values())}
    return JsonResponse(data)

def landscaping_list(request):
    landscapings = Landscaping.objects.all()
    data = {'landscaping': list(landscapings.values())}
    return JsonResponse(data)