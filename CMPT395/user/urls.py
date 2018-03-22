from django.contrib.auth.views import (
    password_change,
    password_change_done,
    password_reset, 
    password_reset_done,
    password_reset_confirm, 
    password_reset_complete,
)
from django.urls import path
from . import views

urlpatterns = [

    path('registor/', views.RegistorView.as_view(), name='registor'),
    path('volunteer/', views.AddVolunteerView.as_view() , name='volunteer'),
    path('family/', views.AddFamilyView.as_view() , name='family'),
    path('child/', views.AddChildView.as_view() , name='child'),
    path('', views.Home.as_view(), name = 'home'),
    path('registor_teacher/', views.RegistorTeacher.as_view(), name='registor_teacher'),
    path('person/', views.AddPerson.as_view() , name='person'),
    path('pick_facilitator/', views.ChooseFacilitatorView.as_view() , name='view_family'),
    path('edit_user/', views.EditUser.as_view(), name='edit_user'),
     path('select_volunteer/', views.ChooseVolunteerView.as_view() , name='select_volunteer'),

    path('password_change', password_change, name='password_change'),
    path('password_change/done/', password_change_done, name='password_change_done'),
    path('password_change', password_change, name='password_change'),
    path('password_change/done/', password_change_done, name='password_change_done'),

    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/', password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
]