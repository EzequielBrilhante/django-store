from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = {
    path('lojas', LojaList.as_view()),
    url('lojas/(?P<pk>[0-9]+)$', LojaDetalhes.as_view()),

}