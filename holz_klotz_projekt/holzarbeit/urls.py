from django.urls import path
from .views import HolzListView, BrettCreateView, ScheibenCreateView, HolzTabelleListView, HolzCreateView

urlpatterns = [
    path('', HolzListView.as_view(), name='home-page'),
    path('holzarten/', HolzTabelleListView.as_view(), name='holz-tabelle'),
    path('holzarten/create/', HolzCreateView.as_view(), name='create-holz'),
    path('createBrett/', BrettCreateView.as_view(), name='brett-create'),
    path('createScheibe/', ScheibenCreateView.as_view(), name='scheibe-create'),
]
