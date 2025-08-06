from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import ContestForm
from phonebook.models import Kontakt


class ContestMixin:
    model = Kontakt
    success_url = reverse_lazy('phonebook:index')


class FormTemplateMixin(ContestMixin):
    form_class = ContestForm
    template_name = 'contest/form.html'


class ContestCreateView(FormTemplateMixin, CreateView):
    pass


class ContestUpdateView(FormTemplateMixin, UpdateView):
    pass


class ContestDeleteView(ContestMixin, DeleteView):
    pass
