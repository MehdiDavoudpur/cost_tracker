# views.py

from django.shortcuts import render
from .models import CostEntry
import matplotlib.pyplot as plt
import io
import urllib, base64

def cost_analysis(request):
    # Retrieve data from the database
    cost_entries = CostEntry.objects.all()
    cost_groups = ['Food', 'Clothes', 'Housing', 'Health', 'Education', 'Entertainment & Welfare', 'Transportation']

    # Calculate the total cost for each group
    cost_group_totals = {group: 0 for group in cost_groups}
    for entry in cost_entries:
        cost_group_totals[entry.cost_group] += entry.price

    # Generate pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(cost_group_totals.values(), labels=cost_group_totals.keys(), autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    pie_chart = get_graph()

    # Generate bar chart
    fig2, ax2 = plt.subplots()
    ax2.bar(cost_group_totals.keys(), cost_group_totals.values())
    ax2.set_ylabel('Total Cost')
    bar_chart = get_graph()

    return render(request, 'cost_analysis.html', {'pie_chart': pie_chart, 'bar_chart': bar_chart})

def get_graph():
    # Convert plot to PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode PNG image to base64 string
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    plt.close()

    return graphic
