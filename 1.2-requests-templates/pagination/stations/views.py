from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    csv_file = settings.BUS_STATION_CSV
    with open(csv_file, newline='', encoding='UTF-8') as f:
        bus_stations = list(csv.DictReader(f))
        paginator = Paginator(bus_stations, 20)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page.object_list,
            'page': page,
        }



    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
            'bus_stations': bus_stations,
            'page': page,
    }
    return render(request, 'stations/index.html', context)
