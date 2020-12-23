from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User


# Create your views here.
from django.views.generic import FormView

from apps.accounts.forms import RegisterForm, CustomLoginForm, ProfileForm
# Create your views here.
from django.views.generic import ListView, DetailView

from apps.accounts.models import WorkerProfile, WorkingArea, WorkerCategory, Message


class HomeWorkerListView(ListView):
    model = WorkerProfile
    template_name = 'home.html'

    def get_queryset(self):
        return super(HomeWorkerListView, self).get_queryset().filter(status=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeWorkerListView, self).get_context_data(**kwargs)
      #  context['object_list']=WorkerProfile.published.all()

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

    recommend_worker = WorkerProfile.objects.filter(category=worker.category,status=True).exclude(pk=pk)

    context={
        'object':worker,
        'recommend_worker':recommend_worker,
        'category_list':WorkerCategory.objects.all(),
    }
    return render(request,'worker_detail.html',context)


def area_filter(request,slug):

    worker=WorkerProfile.objects.filter(working_area__slug=slug)


    context={
        'object_list':worker,
        'category_list': WorkerCategory.objects.all(),

    }
    return render(request,'filterview.html',context)


def category_filter(request, slug):
    worker = WorkerProfile.objects.filter(category__slug=slug)
    print(slug)
    print(worker)

    context = {
        'object_list': worker,
        'category_list': WorkerCategory.objects.all(),

    }
    return render(request, 'filterview.html', context)


def search_view(request):
    query=request.GET.get("search")
    print(query)
    context = {}
    if query:
        result=WorkerProfile.objects.filter(
            Q(user__username__icontains=query)|
            Q(fullname__icontains=query)|
            Q(category__name__icontains=query)|
            Q(working_area__name__icontains=query)|
            Q(working_time__icontains=query)|
            Q(hourly_rate__icontains=query)|
            Q(extra_service__icontains=query)|
            Q(experience__icontains=query)|
            Q(phone__icontains=query)
        )
        print(result)
        context={
            "object_list":set(result),
             'category_list': WorkerCategory.objects.all(),
        }
    return render(request,'filterview.html',context)


class ProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'worker_profile.html'
    login_url = 'sign_in_up_view'

    def get_object(self, queryset=None):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context=super(ProfileView, self).get_context_data(**kwargs)
        context['category_list']=WorkerCategory.objects.all()

        return context

class MessageListView(LoginRequiredMixin,ListView):
    model = Message
    template_name = 'messages.html'
    login_url ="sign_in_up_view"

    def get_queryset(self):
        return super(MessageListView, self).get_queryset().filter(worker__user=self.request.user)



@login_required(login_url="sign_in_up")
def profile_edit(request,username):
    username=request.user.username
    if request.method == "POST":
        form = ProfileForm(request.POST or None,request.FILES,instance=request.user.worker_profile)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,f"You have been update your informations  in successfully !")

            return redirect("profile_view",username=request.user.username)
    else:
        form = ProfileForm(instance=request.user.worker_profile)

    context={
        'form':form,
        'object':get_object_or_404(User,username__iexact=username),
        'category_list': WorkerCategory.objects.all(),

    }

    return render(request,"profile_edit.html",context)

def sign_in_up(request):
    if request.method== "POST":
        signup_form = RegisterForm(request.POST)
        signin_form = CustomLoginForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=True)
            user.save()
            login(request,user)
            messages.success(request,f"Welcome {request.user.username} ! you have logged in successfully !")
            return redirect('home')

        if signin_form.is_valid():
            user = authenticate(
                username = signin_form.cleaned_data['username'],
                password = signin_form.cleaned_data['password'])
            if user:
                login(request,user)
                messages.success(request,f"Welcome {request.user.username} ! you have logged in successfully !")
                return redirect('home')
            else:
                return redirect('sign_in_up_view')


    else:
        signup_form=RegisterForm()
        signin_form = CustomLoginForm
    context = {
        'signup_form': signup_form,
        'signin_form': signin_form,
        'category_list': WorkerCategory.objects.all(),

    }
    return render(request,'sign_in_up.html',context)

def user_logout(request):
    logout(request)
    messages.success(request,"Logout Successfully !")
    return redirect('home')