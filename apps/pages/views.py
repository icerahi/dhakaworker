from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.accounts.models import WorkerProfile, WorkingArea, WorkerCategory


class HomeWorkerListView(ListView):
    model = WorkerProfile
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeWorkerListView, self).get_context_data(**kwargs)
        context['area_list']=WorkingArea.objects.all()
        context['category_list']=WorkerCategory.objects.all()
        return context
