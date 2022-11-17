from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Seed
from .forms import SightingForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    # Get the seeds the finch doesnt have...
    # First, create a list of the seed ids that the finch DOES have
    id_list = finch.seeds.all().values_list('id')
    # Now we can query for seeds whose ids are not in the list using exclude
    seeds_finch_doesnt_have = Seed.objects.exclude(id__in=id_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'sighting_form': sighting_form,
        # Add the seeds to be displayed
        'seeds': seeds_finch_doesnt_have
    })

class FinchCreate(CreateView):
    model = Finch
    fields = ['common_name', 'migratory', 'range']

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

def add_sighting(reqest, finch_id):
    form = SightingForm(reqest.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

class SeedList(ListView):
    model = Seed

class SeedDetail(DetailView):
    model = Seed

class SeedCreate(CreateView):
    model = Seed
    fields = '__all__'

class SeedUpdate(UpdateView):
    model = Seed
    fields = ['name']

class SeedDelete(DeleteView):
    model = Seed
    success_url = '/seeds'

def assoc_seed(request, finch_id, seed_id):
    Finch.objects.get(id=finch_id).seeds.add(seed_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_seed(request, finch_id, seed_id):
    Finch.objects.get(id=finch_id).seeds.remove(seed_id)
    return redirect('detail', finch_id=finch_id)