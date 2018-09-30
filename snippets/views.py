from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from django.shortcuts import render_to_response
from django.template import RequestContext


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
def snippet_list(request):
    """
    List all code snippets or create a new code snippet
    """

    if request.method == 'GET':  # fucntion to display all code snippets
        snippets = Snippet.objects.all()
        serializers = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif request.method == 'POST':  # function to add a new snippet
        data = JSONParser().parse(request)
        print(data)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)  # created
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # bad request


@csrf_exempt
def snippet_detail(request, pk):
    """
    retrieve, update or delete a code snippet
    """

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)  # not found

    if request.method == 'GET':  # function to display a specific serializer
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':  # function to edit a serializer
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # bad request

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)  # no content
