import unittest
import json
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from . import models
from . import serializers


class SnippetTest(APITestCase):
    # url_patterns = [
    #     path('snippet/', include('snippets.urls'))
    # ]

    def setUp(self):
        self.new_snippet = models.Snippet(title='monkey', code='foo = "bar"\n', language='python', style='friendly')

    def test_api_endpoints(self): pass

    def test_view_snippets(self):
        old_count = models.Snippet.objects.count()
        self.new_snippet.save()
        new_count = models.Snippet.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_snippet_validation(self): pass
    
    def test_add_more_snippets(self): pass

    def test_view_snippet(self): pass

    def test_update_snippet(self): pass

    def test_delete_snippet(self): pass
    
    def tearDown(self): pass
