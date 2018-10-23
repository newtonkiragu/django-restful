# from django.shortcuts import render
# from django.http import HttpResponse, jsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins, generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
        context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler401(request, *args, **argv):
    response = render_to_response('401.html', {},
        context_instance=RequestContext(request))
    response.status_code = 401
    return response

def handler400(request, *args, **argv):
    response = render_to_response('400.html', {},
        context_instance=RequestContext(request))
    response.status_code = 400
    return response

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
        context_instance=RequestContext(request))
    response.status_code = 500
    return response


class SnippetList(mixins.ListModelMixin,
    mixins.CreateModelMixin, 
    generics.GenericAPIView):
    """
    List all code snippets or create a new code snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)        


class SnippetDetails(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    """
    retrieve, update or delete a code snippet
    """


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
