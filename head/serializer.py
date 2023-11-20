from rest_framework.serializers import ModelSerializer

from main.models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'