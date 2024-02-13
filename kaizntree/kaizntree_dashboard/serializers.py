from rest_framework import serializers
from .models import Item, Tag
from .models import Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class ItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'sku', 'name', 'category', 'tags', 'stock_status', 'available_stock', 'in_stock']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')  # Extract tags data from validated data
        item_id = validated_data.pop('id', None)

        if item_id is not None:
            # If an ID is provided, try to get the item by ID
            item = Item.objects.get(id=item_id)
        else:
            # If no ID is provided, create a new item
            item = Item.objects.create(**validated_data)

        for tag_data in tags_data:
            # Retrieve tag name from the tag data
            tag_name = tag_data['name']
            # Create tag object or retrieve existing tag if it already exists
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            # Associate tag with the item
            item.tags.add(tag)

        return item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def create(self, validated_data):
        category_id = validated_data.pop('id', None)
        if category_id is not None:
            # If an ID is provided, we'll create the category with that ID
            category, _ = Category.objects.get_or_create(id=category_id, defaults=validated_data)
        else:
            # If no ID is provided, let Django generate one automatically
            category = Category.objects.create(**validated_data)
        return category