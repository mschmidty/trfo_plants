from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import plant_basics, Family, PlantImages

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
                'symbol',
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
                'symbol',
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
    species = plant_basics.objects.order_by('genus').values('genus', 'species','common_name', 'symbol','image','id', 'family__family')
    return JsonResponse({'species': list(species)})

## Additional Images Views

class PlantImagesCreateView(LoginRequiredMixin, generic.CreateView):
    model = PlantImages
    fields =   [
      'additional_image',
      'additional_image_description'
      ]

    def form_valid(self, form):
        form.instance.plant_basics = plant_basics.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)

class PlantImagesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PlantImages
    success_url = reverse_lazy('plants:index')

class PlantImagesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PlantImages
    fields =   [
      'additional_image',
      'additional_image_description'
      ]
#Random View for testing
def testView(request):
    return render(request, 'plants/test_page.html')