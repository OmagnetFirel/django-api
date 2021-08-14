from django.contrib import admin
from .models import Aluno,Curso,Matricula
# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ("id","nome", "email","identidade","nascimento")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 20
    
    
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ("id","codigo_curso","descricao","nivel")
    list_display_links = ("codigo_curso",)
    search_fields = ("codigo_curso", "nivel")
    list_per_page = 10
    

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso")
    list_display_links = ("id", "aluno")
    
admin.site.register(Matricula,Matriculas)