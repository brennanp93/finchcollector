from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finch/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/assoc_seed/<int:seed_id>/', views.assoc_seed, name='assoc_seed'),
    path('finches/<int:finch_id>/unassoc_seed/<int:seed_id>/', views.unassoc_seed, name='unassoc_seed'),
    path('seeds/', views.SeedList.as_view(), name='seeds_index'),
    path('seeds/<int:pk>/', views.SeedDetail.as_view(), name='seeds_detail'),
    path('seeds/create/', views.SeedCreate.as_view(), name='seeds_create'),
    path('seeds/<int:pk>/update/', views.SeedUpdate.as_view(), name='seeds_update'),
    path('seeds/<int:pk>/delete/', views.SeedDelete.as_view(), name='seeds_delete'),
]