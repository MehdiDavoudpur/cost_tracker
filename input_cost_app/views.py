from django.shortcuts import render, redirect
from .forms import CostEntryForm


def input_cost(request):
    if request.method == 'POST':
        form = CostEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_cost')
    else:
        form = CostEntryForm()
    return render(request, 'input_cost.html', {'form': form})

