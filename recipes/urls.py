from django.urls import path
from .views import FoodRecipeListCreateView, FoodRecipeUpdateView

urlpatterns = [
    path('recipes/', FoodRecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:id>/', FoodRecipeUpdateView.as_view(), name='recipe-update'),
]
