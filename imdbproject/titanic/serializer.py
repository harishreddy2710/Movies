from rest_framework.serializers import ModelSerializer
from .models import *


class MovieSerializer(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = "__all__"

