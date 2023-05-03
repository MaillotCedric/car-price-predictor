from django.db import models

class Carburant(models.Model):
    id_carburant = models.AutoField(primary_key=True)
    type_carburant = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'carburant'

    def __str__(self):
        return f"{self.id_carburant} : {self.type_carburant}"

class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorie'

    def __str__(self):
        return f"{self.id_categorie} : {self.nom_categorie}"

class Couleur(models.Model):
    id_couleur = models.AutoField(primary_key=True)
    nom_couleur = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'couleur'

    def __str__(self):
        return f"{self.id_couleur} : {self.nom_couleur}"

class IntervalleProduction(models.Model):
    id_intervalle_production = models.AutoField(primary_key=True)
    debut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'intervalle_production'

    def __str__(self):
        return f"{self.id_intervalle_production} : {self.debut}"

class Marque(models.Model):
    id_marque = models.AutoField(primary_key=True)
    nom_marque = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'marque'

    def __str__(self):
        return f"{self.id_marque} : {self.nom_marque}"

class Modele(models.Model):
    id_modele = models.AutoField(primary_key=True)
    nom_modele = models.CharField(max_length=50, blank=True, null=True)
    id_marque = models.ForeignKey(Marque, db_column='id_marque', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'modele'

class RoueMotrice(models.Model):
    id_roue_motrice = models.AutoField(primary_key=True)
    type_roue_motrice = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'roue_motrice'

    def __str__(self):
        return f"{self.id_roue_motrice} : {self.type_roue_motrice}"

class Transmission(models.Model):
    id_transmission = models.AutoField(primary_key=True)
    type_transmission = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transmission'

    def __str__(self):
        return f"{self.id_transmission} : {self.type_transmission}"

class Voiture(models.Model):
    id_voiture = models.AutoField(primary_key=True)
    prix = models.IntegerField(blank=True, null=True)
    levy = models.IntegerField(blank=True, null=True)
    interieur_cuir = models.BooleanField(blank=False, null=True, default=False)
    cylindree = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nombre_cylindres = models.IntegerField(blank=True, null=True)
    kilometrage = models.IntegerField(blank=True, null=True)
    nombre_portes = models.IntegerField(blank=True, null=True)
    nombre_airbags = models.IntegerField(blank=True, null=True)
    id_intervalle_production = models.ForeignKey(IntervalleProduction, db_column='id_intervalle_production', on_delete=models.CASCADE)
    id_couleur = models.ForeignKey(Couleur, db_column='id_couleur', on_delete=models.CASCADE)
    id_roue_motrice = models.ForeignKey(RoueMotrice, db_column='id_roue_motrice', on_delete=models.CASCADE)
    id_transmission = models.ForeignKey(Transmission, db_column='id_transmission', on_delete=models.CASCADE)
    id_carburant = models.ForeignKey(Carburant, db_column='id_carburant', on_delete=models.CASCADE)
    id_categorie = models.ForeignKey(Categorie, db_column='id_categorie', on_delete=models.CASCADE)
    id_marque = models.ForeignKey(Marque, db_column='id_marque', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'voiture'
