from django.shortcuts import render

from django.views.generic import ListView

from sources.models import Source


class SourcesListView(ListView):
    model = Source
    template_name = 'sources/sources.html'
