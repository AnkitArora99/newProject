from django.contrib import admin
from django.urls import include, path

from newApp import views

urlpatterns = [
    path('',views.current_time,name='time'),
    path('status',views.my_view,name='status'),
    path('create',views.create_view,name='create'),
    path('c-create',views.MyCreateView.as_view(),name='class-create'),
    path('list',views.list_view,name='list'),
    path('list/<id>',views.detail_view,name='detail'),
    path('update/<id>',views.update_view,name='update'),
    path('delete/<id>',views.delete_view,name='delete'),
    path('c-list',views.MyView.as_view(),name='class-list'),
    path('c-list-2',views.MyListView.as_view(),name='class-list-2'),
    path('c-list-2/<pk>',views.MyDetailView.as_view(),name='class-detail'),
    path('c-update/<pk>',views.MyUpdateView.as_view(),name='class-update'),
    path('c-delete/<pk>',views.MyDeleteView.as_view(),name='class-delete'),
    path('form', views.MyFormView.as_view(),name='class-form'),
    path('get-post', views.MyFormVIew2.as_view(),name='get-post-class'),
]
