from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from . models import Country, State

# Create your views here.


def index(request):
    obj = Country.objects.all()
    param = {'obj':obj}
    return render(request,'myapp/dropdown.html',param)

def load_fetchState(request):
    coun = request.GET.get('country')
    cities = State.objects.filter(country_id=coun).order_by('state')

    return render(request, 'myapp/state.html', {'cities': cities})