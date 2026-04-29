from rest_framework import serializers
from .models import Category, Label, Task, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')
    owner_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'deadline',
            'priority',
            'priority_display',
            'category',
            'category_name',
            'labels',
            'owner',
            'owner_name',
        ]


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'created_at',
            'task',
            'author',
            'author_name',
        ]
