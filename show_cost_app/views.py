from django.shortcuts import render, redirect
from .forms import CostShowForm


def show_cost(request):
    if request.method == 'POST':
        form = CostShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_cost')
    else:
        form = CostShowForm()
    return render(request, 'show_cost.html', {'form': form})


