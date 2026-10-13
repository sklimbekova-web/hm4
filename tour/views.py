from django.shortcuts import render, get_object_or_404
from .models import Tour

def tour_list_view(request):
    tours = Tour.objects.all()  
    return render(request, 'tour/tour_list.html', {'tours': tours})

def tour_detail_view(request, pk):
    tour = get_object_or_404(Tour, pk=pk)  
    return render(request, 'tour/tour_detail.html', {'tour': tour})
