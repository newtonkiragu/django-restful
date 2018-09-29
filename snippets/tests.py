import unittest
import json
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from models import Snippet
from serializers import SnippetSerializer


class SnippetTest(APITestCase, URLPatternsTestCase):
    url_patterns = [
        path('snippet/', include('snippets.urls'))
    ]

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.new_snippet = {
            "id": 1,
            "title": "Monkey",
            "code": "foo = \"bar\"\n",
            "language": "python",
            "style": "friendly"
        }
    
    def tearDown(self):
        self.app_context.pop()
