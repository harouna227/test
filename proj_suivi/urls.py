from django.urls import path

from proj_suivi.views import TacheListView, TacheCreateView, TacheUpdateView, TacheDeleteView

urlpatterns = [
    path('home/', TacheListView.as_view(), name="home"),
    path('create/', TacheCreateView.as_view(), name="create"),
    path('edit/<str:lebelle>/', TacheUpdateView.as_view(), name="edit"),
    path('edit/<str:lebelle>', TacheDeleteView.as_view(), name="delete"),

]