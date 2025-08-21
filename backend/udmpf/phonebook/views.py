from collections import defaultdict

from django.views.generic import ListView

from .models import Kontakt


class PhonebookListView(ListView):
    model = Kontakt
    template_name = 'phonebook/phonebook.html'

    def get_queryset(self):
        return Kontakt.objects.select_related('department', 'subdivision').order_by(
            '-subdivision__output_order', '-department__output_order', '-output_order'
        )

    def get_context_data(self, **kwargs):
        grouped_kontakts = defaultdict(lambda: defaultdict(list))
        for kontakt in self.get_queryset():
            subdivision_title = kontakt.subdivision.title if kontakt.subdivision else ''
            department_title = kontakt.department.title if kontakt.department else ''
            grouped_kontakts[subdivision_title][department_title].append(kontakt)

        grouped_kontakts = {
            subdivision: dict(departments)
            for subdivision, departments in grouped_kontakts.items()
        }
        context = super().get_context_data(**kwargs)
        context['grouped_kontakts'] = dict(
            grouped_kontakts
        )
        return context
