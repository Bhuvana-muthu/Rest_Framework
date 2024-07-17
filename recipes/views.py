from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import status
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer

class FoodRecipeListCreateView(generics.ListCreateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class FoodRecipeUpdateView(generics.UpdateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
