from rest_framework import serializers
from .models import MovieData

class MovieSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = MovieData
        fields = '__all__'