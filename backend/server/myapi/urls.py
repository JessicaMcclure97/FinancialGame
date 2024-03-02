from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
<<<<<<< HEAD
    path('getQuestion/', views.get_Question, name='get_question'),

=======
    path('getQuestion/', views.get_question, name='get_question'),
>>>>>>> ea190a1c915f4ecf5811102d17ba6d5f1727ff92
]