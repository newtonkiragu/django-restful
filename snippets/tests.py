import unittest
import json
from django.urls import include, path, reverse
from rest_framework.test import APITestCase
from . import models
from . import serializers
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import status


class SnippetTest(APITestCase):
    # url_patterns = [
    #     path('snippet/', include('snippets.urls'))
    # ]

    def setUp(self):
        self.new_snippet = models.Snippet(title='monkey', code='foo = "bar"\n', language='python', style='friendly')

    def test_view_snippets(self):
        old_count = models.Snippet.objects.count()
        self.new_snippet.save()
        new_count = models.Snippet.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_view_snippet(self):
        snippet_id = 1
        self.new_snippet.save()
        snippet = models.Snippet.objects.get(pk=snippet_id)
        response = self.client.get(reverse('snippet', kwargs={'pk': snippet.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, snippet)

    def test_update_snippet(self):
        snippet_id = 1
        self.new_snippet.save()
        snippet = models.Snippet.objects.get(pk=snippet_id)
        change_snippet = {'code': 'return False'}
        res = self.client.put(
            reverse('snippet', kwargs={'pk': snippet.id}),
            change_snippet, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_snippet(self):
        snippet_id = 1
        # self.new_snippet.save()
        snippet = models.Snippet.objects.get(pk=snippet_id)
        response = self.client.delete(
            reverse('snippet', kwargs={'pk': snippet.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def tearDown(self): pass
