from django.shortcuts import render, redirect
from .forms import StageForm

def ajouter_stage(request):
    form = StageForm()
    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            stage = form.save()
            return redirect('stage_detail', pk=stage.pk)
    return render(request, 'ajouter_stage.html', {'form': form})

def stage_detail(request, pk):
    stage = Stage.objects.get(pk=pk)
    return render(request, 'stage_detail.html', {'stage': stage})

def liste_stages(request):
    stages = Stage.objects.all()
    return render(request, 'liste_stages.html', {'stages': stages})
