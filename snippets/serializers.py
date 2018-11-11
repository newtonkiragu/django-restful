from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    """
     a class that serializes and deserializes the snippet instances
     into representations such as json.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        getting all snippets and adding new snippets
        """
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    """
    a class that serializes and desirializes the user
    instances into representaion
    """
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
