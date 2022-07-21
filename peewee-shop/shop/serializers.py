from dataclasses import fields
from abstract.serializers import BaseSerializer
from .models import Product, Comment

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "category", "title", "price", "description", "comments")
        model = Product

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "user", "body", "created_at")
        model = Comment
