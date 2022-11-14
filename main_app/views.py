from django.shortcuts import render


finches = [
    {'name': 'House Finch', 'migratory': 'False', 'range': '' },
    {'name': 'Lesser Goldfinch', 'migratory': 'True', 'range': 'All throughout CA' },
    {'name': 'American Goldfinch', 'migratory': 'True', 'range': 'Canada to Southern US' },
    {'name': 'Purple Finch', 'migratory': 'True', 'range': 'All throughout US and Canada' }
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches
    })