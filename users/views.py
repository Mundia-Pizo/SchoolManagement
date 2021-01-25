from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegistrationForm

class RegistrationView(FormView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = 'login'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

