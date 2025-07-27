from collections import defaultdict

from django.shortcuts import render

from .models import Kontakt


def index(request):
    kontakts = Kontakt.objects.select_related('department', 'subdivision').all()
    grouped_kontakts = defaultdict(lambda: defaultdict(list))
    for kontakt in kontakts:
        subdivision_title = kontakt.subdivision.title if kontakt.subdivision else ''
        department_title = kontakt.department.title if kontakt.department else ''
        grouped_kontakts[subdivision_title][department_title].append(kontakt)

    grouped_kontakts = {
        subdivision: dict(departments)
        for subdivision, departments in grouped_kontakts.items()
    }

    context = {
        'grouped_kontakts': dict(grouped_kontakts),
    }
    return render(request, 'phonebook/phonebook.html', context)
