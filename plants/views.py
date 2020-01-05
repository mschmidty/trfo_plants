from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import plant_basics, Family

# Create your views here.

def index(request):
    latest_plants = plant_basics.objects.order_by('genus')
    context = {'latest_plants': latest_plants}
    return render(request, 'plants/index.html', context)

class PlantDetailView(generic.DetailView):
    model = plant_basics
    template_name = 'plants/detail.html'

class PlantCreateView(LoginRequiredMixin, generic.CreateView):
    model = plant_basics
    fields =   ['genus',
                'species',
                'description',
                'image',
                'family'
                ]
class PlantDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = plant_basics
    success_url = reverse_lazy('plants:index')

class PlantUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = plant_basics
    fields = [  'genus',
                'species',
                'description',
                'image',
                'family'
    ]


# Family Views
def familyIndex(request):
    all_families = Family.objects.order_by('family')
    context = {'all_families': all_families}
    return render(request, 'plants/family_list.html', context)

class FamilyDetailView(generic.DetailView):
    model = Family
    template_name = 'plants/family-detail.html'

class FamilyCreateView(LoginRequiredMixin, generic.CreateView):
    model = Family
    fields =   ['family',
                'family_description'
                ]
class FamilyDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Family
    success_url = reverse_lazy('plants:family-index')

class FamilyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Family
    fields = [  'family',
                'family_description'
                ]

def familyJsonIndex(request):
    species = plant_basics.objects.order_by('genus').values('genus', 'species','common_name', 'symbol','id', 'family__family')
    return JsonResponse({'species': list(species)})