from django.urls import path
from. import views

urlpattern=[
    path('',views.postlist.as_view(),name='home'),
    path('<slug:slug>/', views.postdetail.as_view(), name='postdetail')

]