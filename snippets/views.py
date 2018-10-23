from django.shortcuts import render
# from django.http import HttpResponse, jsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@csrf_exempt  # used to prevent cross site request forgery
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets or create a new code snippet
    """

    if request.method == 'GET':  # fucntion to display all code snippets
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # function to add a new snippet
        data = JSONParser().parse(request)
        print(data)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # bad request


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    retrieve, update or delete a code snippet
    """

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)  # not found

    if request.method == 'GET':  # function to display a specific serializer
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':  # function to edit a serializer
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # bad request

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status.HTTP_204_NO_CONTENT)  # no content
