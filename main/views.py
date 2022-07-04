from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Monitoring, Sensors
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy


class MonListView(ListView):
    model = Monitoring
    queryset = Monitoring.objects.all().order_by('-date')
    template_name = 'main_list.html'


class MonCreateView(CreateView):
    model = Monitoring
    fields = ['sensor', 'value', 'date']
    template_name = 'main_create.html'

    def get_initial(self):
        return {'date': timezone.now()}


class MonDeleteView(DeleteView):
    model = Monitoring
    success_url = reverse_lazy('mon-list')
    template_name = 'main-del.html'
