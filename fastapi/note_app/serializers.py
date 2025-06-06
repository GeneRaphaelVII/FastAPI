from rest_framework import serializers
from .models import Note, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'tags', 'tag_ids']

    def create(self, validated_data):
        tag_ids = validated_data.pop('tag_ids', [])
        note = Note.objects.create(**validated_data)
        note.tags.set(tag_ids)
        return note

    def update(self, instance, validated_data):
        tag_ids = validated_data.pop('tag_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if tag_ids is not None:
            instance.tags.set(tag_ids)
        return instance
