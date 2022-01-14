from django.shortcuts import render

# Create your views here.
from .models import Main


def test_dashboard_index(request):

    grid_table = Main.objects.all().order_by('pk')

    for i in grid_table:
        print(i)

    #print(grid_table)
    return render(request, 'main/test_dashboard.html')