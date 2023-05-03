from django.contrib import admin
from app.models import Carburant, Categorie, Couleur, IntervalleProduction, Marque, Modele, RoueMotrice, Transmission, Voiture

class CarburantAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

class CategorieAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class CouleurAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class IntervalleProductionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class MarqueAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class ModeleAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class RoueMotriceAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class TransmissionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
    
class VoitureAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

admin.site.register(Carburant, CarburantAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Couleur, CouleurAdmin)
admin.site.register(IntervalleProduction, IntervalleProductionAdmin)
admin.site.register(Marque, MarqueAdmin)
admin.site.register(Modele, ModeleAdmin)
admin.site.register(RoueMotrice, RoueMotriceAdmin)
admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Voiture, VoitureAdmin)
