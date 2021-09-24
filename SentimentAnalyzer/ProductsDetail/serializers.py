from rest_framework.serializers import ModelSerializer
from ProductsDetail.models import Product, Review


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_id']


class ReviewSerializer(ModelSerializer):
    pro = ProductSerializer(source='product_id', many=True)
    
    class Meta:
        model = Review
        fields = ['pro', 'product_id', 'reviews', 'polarity', 'score']
        # depth = 1


