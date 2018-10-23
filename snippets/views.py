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


class SnippetList(APIView):
    """
    List all code snippets or create a new code snippet
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # bad request


class SnippetDetails(APIView):
    """
    retrieve, update or delete a code snippet
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404  # not found
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
            status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # bad request

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status.HTTP_204_NO_CONTENT)  # no content
