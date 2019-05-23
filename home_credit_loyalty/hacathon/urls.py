from django.urls import path, re_path
from . import views


urlpatterns = [
    path('get_tasks/', views.TaskView.as_view({'get': 'list'})),
    path('add_task/', views.TaskView.as_view({'get': 'add_task'})),
    path('<int:user_id>/get_tasks', views.TaskView.as_view({'get': 'list_by_id'})),
    path('login/', views.authorize),
    path('add_point/<int:user_id>/<int:task_id>', views.TaskView.as_view({'get': 'add_point'})),
    path('pay/<int:user_id>/<int:balance>', views.make_transaction),
    path('binding/<int:user_id>', views.CardView.as_view({'get': 'create'}))
]