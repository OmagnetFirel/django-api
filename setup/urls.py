from django.contrib import admin
from django.urls import path,include
from escola.views import AlunosViewSet,CursosViewSet,MatriculasViewSet,ListaMatriculasAlunos,ListaAlunosMatriculados
from rest_framework import routers


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)
router.register('cursos', CursosViewSet)
router.register('matriculas', MatriculasViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas", ListaMatriculasAlunos.as_view()),
    path("cursos/<int:pk>/matriculas", ListaAlunosMatriculados.as_view())
]
