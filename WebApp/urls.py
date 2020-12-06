from WebApp import views
from django.conf.urls import url

urlpatterns = [

   url(r'^api/task$',views.tasklist),

    url(r'^api/taskdetails/(?P<pk>[0-9]+)$',views.task_details),
    url(r'^api/task/published$',views.published),
]
