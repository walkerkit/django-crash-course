from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    email = serializers.CharField()
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.tilte = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data('email', instance.email)
        instance.date = validated_data('date', instance.date)

        instance.save()
        return instance
