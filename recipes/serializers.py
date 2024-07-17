from rest_framework import serializers
from .models import FoodRecipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = ['id', 'name', 'description', 'ingredients', 'method', 'category']

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Name cannot be blank.")
        if not data.get('description'):
            raise serializers.ValidationError("Description cannot be blank.")
        if not data.get('ingredients'):
            raise serializers.ValidationError("Ingredients cannot be blank.")
        if not data.get('method'):
            raise serializers.ValidationError("Method cannot be blank.")
        if not data.get('category'):
            raise serializers.ValidationError("Category cannot be blank.")
        return data
