from django.urls import path

from apps.pages import views

urlpatterns = [
    path('',views.HomeWorkerListView.as_view(),name='home'),
]
