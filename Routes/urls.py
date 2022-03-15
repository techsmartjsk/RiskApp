from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('platform/',views.platform,name='platform'),
    path('create_project/',views.create_project,name='create_project'),
    path('project/<int:project_number>',views.check_project_number,name='check_project_number'),
    path('show_projects/',views.show_projects,name='show_projects'),
    path('get_risk/<str:project_name>',views.get_risk,name='get_risk'),
    path('sort/<str:sortBy>',views.sort_by,name='sort_by'),
]