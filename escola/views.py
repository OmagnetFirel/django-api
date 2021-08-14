from rest_framework import  viewsets, generics
from .models import  Aluno,Curso,Matricula
from .serializer import AlunoSerializer, CursoSerializer,MatriculaSerializer,ListaMatriculasAlunosSerializer,AlunosMatriculadosNoCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibe Todos os Alunos(as)'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class CursosViewSet(viewsets.ModelViewSet):
    '''Exibe Todos os Cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    '''Exibe todas as Matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaMatriculasAlunos(generics.ListAPIView):
    '''Listando as matriculas dos alunos(as)'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class ListaAlunosMatriculados(generics.ListAPIView):
    '''Listando Alunos Matriculados Em Um Curso'''
    def get_queryset(self):
        queryset  = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = AlunosMatriculadosNoCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    