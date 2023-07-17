from django.contrib import admin

from proj_suivi.models import Tache, Departement, Collaborateurs, TacheCollaborateur


class AdminTache(admin.ModelAdmin):
    list_display = ('libelle', 'commentaires', )


class AdminDepartement(admin.ModelAdmin):
    list_display = ('libelle', )


class AdminCollaborateurs(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'poste')


admin.site.register(Tache, AdminTache)
admin.site.register(Departement, AdminDepartement)
admin.site.register(Collaborateurs, AdminCollaborateurs)





