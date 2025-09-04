from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class UserProfile(TemplateView):
    template_name = 'phonebook/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
