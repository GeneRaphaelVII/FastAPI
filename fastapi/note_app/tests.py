from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Note, Tag

class NoteAppTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag1 = Tag.objects.create(name="work")
        self.tag2 = Tag.objects.create(name="personal")

    def test_create_tag(self):
        response = self.client.post("/api/tags/", {"name": "urgent"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "urgent")

    def test_list_tags(self):
        response = self.client.get("/api/tags/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_get_tag_with_notes(self):
        note = Note.objects.create(title="Example", description="Something")
        note.tags.add(self.tag1)

        response = self.client.get(f"/api/tags/{self.tag1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.tag1.name)
        self.assertEqual(len(response.data["notes"]), 1)

    def test_create_note_with_tags(self):
        response = self.client.post("/api/notes/", {
            "title": "New Note",
            "description": "With tags",
            "tag_ids": [self.tag1.id, self.tag2.id]
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Note")
        self.assertEqual(len(response.data["tags"]), 2)

    def test_list_notes(self):
        Note.objects.create(title="A", description="Test")
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_note(self):
        note = Note.objects.create(title="Old", description="Text")
        response = self.client.put(f"/api/notes/{note.id}/", {
            "title": "Updated",
            "description": "Updated text",
            "tag_ids": [self.tag1.id]
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated")
        self.assertEqual(len(response.data["tags"]), 1)
