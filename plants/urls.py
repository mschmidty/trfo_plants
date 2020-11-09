from django.urls import path

from . import views

app_name = 'plants'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.PlantDetailView.as_view(), name = 'detail'),
    path('new/', views.PlantCreateView.as_view(), name = "create"),
    path('<int:pk>/update/', views.PlantUpdateView.as_view(), name = "update"),
    path('<int:pk>/delete/', views.PlantDeleteView.as_view(), name = "delete"),
    path('family/', views.familyIndex, name='family-index'),
    path('family/<int:pk>/', views.FamilyDetailView.as_view(), name = 'family-detail'),
    path('family/new/', views.FamilyCreateView.as_view(), name = "family-create"),
    path('family/<int:pk>/update/', views.FamilyUpdateView.as_view(), name = "family-update"),
    path('family/<int:pk>/delete/', views.FamilyDeleteView.as_view(), name = "family-delete"),
    path('family_api/', views.familyJsonIndex, name = "family_api"),
    path('<int:pk>/plant-images/new/', views.PlantImagesCreateView.as_view(), name = "plant-images-create"),
    path('plant-images/<int:pk>/update/', views.PlantImagesUpdateView.as_view(), name = "plant-images-update"),
    path('plant-images/<int:pk>/delete/', views.PlantImagesDeleteView.as_view(), name = "plant-images-delete"),
    path('test-page', views.testView,name="test-view"),
]
