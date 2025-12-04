from django.contrib import admin
import .models 

#Forma 1 Usando Decorador
@admin.register(Receita)
class ReceitaAdmin(admin.MOdelAdmin):
    ...


#Forma 2 Registrando Manualmente
class CategoriaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Categoria, CategoriaAdmin)
