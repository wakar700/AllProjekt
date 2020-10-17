from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Holzarten, Brett, Scheiben, Holz


def home(request):
    context = {
        'holzarten': Holzarten.objects.all()
    }
    return render(request, 'holzarbeit/homePage.html', context)


def getAllHolzTyp(request):
    context = {
        'holz': Holz.objects.all()
    }
    return render(request, 'holzarbeit/preisTabelle.html', context)


class HolzListView(ListView):
    model = Holzarten
    template_name = 'holzarbeit/homePage.html'  # <app>/<model>_.html
    context_object_name = 'holzarten'
    ordering = ['-date_posted']


class HolzTabelleListView(ListView):
    model = Holz
    template_name = 'holzarbeit/preisTabelle.html'  # <app>/<model>_.html
    context_object_name = 'holz'


class HolzCreateView(CreateView):
    model = Holz
    template_name = 'holzarbeit/holz-anlegen.html'
    fields = ['name', 'preis']
    success_url = '/holzarten/'


class BrettCreateView(CreateView):
    model = Brett
    template_name = 'holzarbeit/bretter.html'
    fields = ['brettnummer', 'holzart', 'laenge', 'breite', 'staerke']


class ScheibenCreateView(CreateView):
    model = Scheiben
    template_name = 'holzarbeit/scheiben.html'
    fields = ['scheibennummer', 'holzart', 'durchmesser', 'staerke']


def bretter(request):
    return render(request, 'holzarbeit/homePage.html')


def scheiben(request):
    return render(request, 'holzarbeit/homePage.html')