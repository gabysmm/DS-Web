#vai definir as rotas da minha aplicação. Ou seja, vai dizer qual função o django deve executar de acordo com a url q for colocada

from django.urls import path
from . import views

urlpatterns = [ 
    path('tabuada/<int:num>/', views.tabuada, name='tabuada'), #deifnimos aq a url q vai esperar um número através de uma lista
    path('', views.semnum, name="semnum"),
]