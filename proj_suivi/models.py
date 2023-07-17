from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tache(models.Model):
    libelle = models.CharField(max_length=123)
    commentaires = models.CharField(max_length=225)

    class Meta:
        verbose_name = 'tache'

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("home")


class Departement(models.Model):
    libelle =models.CharField(max_length=123)

    class Meta:
        verbose_name = 'département'

    def __str__(self):
        return self.libelle


class Collaborateurs(models.Model):
    departement_id = models.ForeignKey(Departement, on_delete=models.CASCADE)
    nom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nom', null=True)
    prenom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prenom', null=True)
    poste = models.CharField(max_length=123)

    class Meta:
        verbose_name = 'collaborateur'

    def __str__(self):
        return self.nom and self.prenom


class TacheCollaborateur(models.Model):
    tache_id = models.ManyToManyField(Tache)
    collaborateur_id = models.ManyToManyField(Collaborateurs)

    class Meta:
        verbose_name = 'tache_collab'




