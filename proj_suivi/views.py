from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from proj_suivi.models import Tache, Collaborateurs, Departement

""" Taches """
class TacheListView(ListView):
    model = Tache
    context_object_name = "taches"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return "Aucune tache"


@method_decorator(login_required, name='dispatch')
class TacheCreateView(CreateView):
    model = Tache
    template_name = "proj_suivi/creates_tache.html"
    fields = ["libelle", "commentaires", ]


class TacheUpdateView(UpdateView):
    model = Tache
    template_name = "proj_suivi/uodate_tache.html"
    fields = ["libelle", "comment"]


class TacheDeleteView(DeleteView):
    model = Tache
    success_url = reverse_lazy("home")
    template_name = "proj_suivi/tache_confirm_delete.html"


""" Collaborateurs """
class CollabListView(ListView):
    model = Collaborateurs
    context_object_name = "collaborateurs"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return "Aucun collaborateurs"


@method_decorator(login_required, name='dispatch')
class CollabCreateView(CreateView):
    model = Collaborateurs
    template_name = "proj_suivi/create_collaborateur.html"
    fields = ["nom", "prenom", "poste" ]


class CollabUpdateView(UpdateView):
    model = Collaborateurs
    template_name = "proj_suivi/update_collaborateur.html"
    fields = ["nom", "prenom", "poste", "departement_id" ]


class CollabDeleteView(DeleteView):
    model = Collaborateurs
    success_url = reverse_lazy("home")
    template_name = "proj_suivi/collaborateur_confirm_delete.html"


""" Departement """
class DepartListView(ListView):
    model = Departement
    context_object_name = "departements"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return "Aucun departements"


@method_decorator(login_required, name='dispatch')
class DepartCreateView(CreateView):
    model = Collaborateurs
    template_name = "proj_suivi/create_departement.html"
    fields = ["libelle", ]


class DepartUpdateView(UpdateView):
    model = Departement
    template_name = "proj_suivi/update_departement.html"
    fields = ["libelle", ]


class DepartDeleteView(DeleteView):
    model = Departement
    success_url = reverse_lazy("home")
    template_name = "proj_suivi/departement_confirm_delete.html"



