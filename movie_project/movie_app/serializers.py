from rest_framework import serializers
from .models import Movies, Director, Gerne

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class GerneSerializer(serializers.ModelSerializer):
        class Meta:
            model = Gerne
            fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
        director= serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(), many=True)   

        genre = serializers.PrimaryKeyRelatedField(queryset=Gerne.objects.all(), many=True)
        class Meta:
          model = Movies
          fields = '__all__'