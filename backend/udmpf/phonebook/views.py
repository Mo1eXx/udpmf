from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import viewsets

from .models import Department, Kontakt, Subdivision


def index(request):
    kontakts = Kontakt.objects.all()
    departments = Department.objects.all()
    subdivisions = Subdivision.objects.all()
    template_name = 'phonebook/index.html'
    context = {
        'kontakts': kontakts,
        'departments': departments,
        'subdivisions': subdivisions
    }
    return render(request, template_name, context)
