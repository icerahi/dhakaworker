from django.urls import path

from apps.pages import views

urlpatterns = [
    path('',views.HomeWorkerListView.as_view(),name='home'),
    path('worker/details/<pk>',views.worker_details,name='worker_detail',),
    path('area/<slug>/',views.area_filter,name='area_filter'),
    path('category/<slug>/',views.category_filter,name='category_filter'),
    path("search/",views.search_view,name='search_view'),
    path('signup/',views.sign_in_up,name='sign_in_up_view'),
    path('logout/',views.user_logout,name='logout'),

    path('<username>/',views.ProfileView.as_view(),name='profile_view'),
    path('edit/<username>',views.profile_edit,name='profile_edit_view'),
    path('messages/<username>',views.MessageListView.as_view(),name="messages"),
]
