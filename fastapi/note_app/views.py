from rest_framework import generics
from rest_framework.response import Response
from .models import Note, Tag
from .serializers import NoteSerializer, TagSerializer


# Note Views
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Existing views...
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def retrieve(self, request, *args, **kwargs):
        tag = self.get_object()
        notes = tag.notes.all()
        note_data = NoteSerializer(notes, many=True).data
        tag_data = TagSerializer(tag).data
        tag_data['notes'] = note_data
        return Response(tag_data)

