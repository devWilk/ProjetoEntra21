from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from curso.form import FormCurso
from .models import Curso

# Create your views here.
# crud
def listar_cursos(request):
    cursos = Curso.objects.all()
    total = cursos.count
    return render(request, 'cursos.html',{'lista_curso' : cursos, 'total_registro' : total} )

@login_required
def cadastrar_curso(request):
    form = FormCurso(request.POST or None)
    if form.is_valid():  
        try:  
            form.save()
            return redirect(listar_cursos)
        except:
            pass

    return render(request,'cadastrar_curso.html',{'form' :form})

@login_required
def alterar_curso(request,id):
    curso = Curso.objects.get(id=id)
    form = FormCurso(request.POST,instance=curso)
    if form.is_valid():
        form.save()
        return redirect(listar_cursos)
    return render(request,'alterar_curso.html',{'curso' : curso})

@login_required
def excluir_curso(request,id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect(listar_cursos)
    return render(request,'excluir_curso.html',{'curso' : curso})

