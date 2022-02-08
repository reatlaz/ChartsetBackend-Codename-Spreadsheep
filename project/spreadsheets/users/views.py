from django.http.response import JsonResponse
from django.shortcuts import render
from users.models import User

from chartsets.serializers import UserSerializer
from rest_framework.response import Response

from .documents import UserDocument
from rest_framework.decorators import api_view

def user_detail(request):
    return JsonResponse({'user': 'User 1'})

@api_view(['GET'])
def usr_search(request):
    queryset = UserDocument.search().filter("term", username=request.GET.get('username'))
    queryset = queryset.to_queryset()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)