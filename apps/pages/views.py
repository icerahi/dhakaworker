from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.accounts.models import WorkerProfile, WorkingArea, WorkerCategory


class HomeWorkerListView(ListView):
    model = WorkerProfile
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeWorkerListView, self).get_context_data(**kwargs)
        context['area_list']=WorkingArea.objects.all()
        context['category_list']=WorkerCategory.objects.all()
        return context




def worker_details(request,pk):
    worker = get_object_or_404(WorkerProfile,id=pk)

    viewed = request.session.get('viewed',[])
    if viewed:
        if worker.id not in viewed:
            viewed.append(worker.id)
            request.session['viewed']=viewed
            worker.views +=1
            worker.save()
    else:
        viewed = [worker.id]
        request.session['viewed']=viewed
        worker.views +=1
        worker.save()

    recommend_worker = WorkerProfile.objects.filter(category=worker.category).exclude(pk=pk)

    context={
        'object':worker,
        'recommend_worker':recommend_worker,
        'category_list':WorkerCategory.objects.all(),
    }
    return render(request,'worker_detail.html',context)
