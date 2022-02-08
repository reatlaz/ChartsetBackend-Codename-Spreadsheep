from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseNotFound, HttpResponseForbidden
from chartsets.models import Chartset
from chartsets.tasks import email_admin
from users.models import User
from chartsets.serializers import ChartsetSerializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from .documents import ChartsetDocument
from rest_framework.decorators import api_view

from application.decorators import login_required, rest_login_required
#Создание объекта---НЕ работает с авторизацией
#@login_required
@require_POST
def create_chartset(request):
    newchartset = Chartset.objects.create(name=request.POST.get('chartset_name'))
    #newchartset.userschartsets.add(request.user)
    newchartset.userschartsets.add(User.objects.get(first_name = 'ReAtlaz'))
    #не нужен сейв
    objinfo = {'pk': newchartset.pk, 'name': request.POST.get('chartset_name')}

    email_admin.delay(objinfo)
    
    return JsonResponse(objinfo)

#Детальная информация об объекте---работает с авторизацией
@login_required
@require_GET
def chartset_detail(request, chartset_id):
    try:
        mychartset = Chartset.objects.get(id=chartset_id)
    except Chartset.DoesNotExist:
        return HttpResponseNotFound('Chartset not found')
    if(mychartset.userschartsets != request.user):
        return HttpResponseForbidden('You do not have access to this chartset')
    return JsonResponse({'id': mychartset.id, 'name': mychartset.name, 'Последнее изменение': mychartset.date_modified})

#Редактирование объекта---НЕ работает
@login_required
@require_POST
def edit_chartset(request, chartset_id):
    try:
        mychartset = Chartset.objects.get(id=chartset_id, userschartsets = request.user)
    except Chartset.DoesNotExist:
        return HttpResponseNotFound('Chartset not found')
    old_name = mychartset.name
    mychartset.name = request.POST.get('new_name')
    mychartset.save()
    return JsonResponse({'old name': old_name, 'new name': mychartset.name})

#Удаление объекта---НЕ работает с авторизацией
@login_required
@require_POST
def delete_chartset(request, chartset_id):
    try:
        mychartset = Chartset.objects.get(id=chartset_id, userschartsets = request.user)
    except Chartset.DoesNotExist:
        return HttpResponseNotFound('Chartset not found')
    name = mychartset.name
    mychartset.delete()
    return JsonResponse({'deleted chartset': name})

#Список объектов---работает с авторизацией
@login_required
@require_GET
def list_chartsets(request):
    allchartsets = Chartset.objects.filter(userschartsets=request.user)
    resp =[]
    for obj in allchartsets:
        resp.append({'id': obj.id, 'name': obj.name})
    return JsonResponse({'all chartsets': resp})

#Функция, которая возвращает отрендеренный html (например, главная страница приложения)
@require_GET
def home(request):
    return render(request, 'home.html')

#проверка реляционной связи
#SELECT chartsets_chartset.name, users_user.username FROM chartsets_chartset INNER JOIN chartsets_chartset_userschartsets ON chartsets_chartset_userschartsets.chartset_id = chartsets_chartset.id INNER JOIN users_user ON chartsets_chartset_userschartsets.user_id = users_user.id;

@require_GET
def login(request):
    return render(request, 'login.html')


class ChartsetViewSet(viewsets.ModelViewSet):
    serializer_class = ChartsetSerializer
    queryset = Chartset.objects.all()

    @rest_login_required
    def list(self, request):
        queryset = Chartset.objects.filter(userschartsets=request.user)
        serializer = ChartsetSerializer(queryset, many=True)
        return Response(serializer.data)

    @rest_login_required
    def retrieve(self, request, pk=None):
        queryset = Chartset.objects.filter(userschartsets=request.user)
        chartset = get_object_or_404(queryset, pk=pk)
        serializer = ChartsetSerializer(chartset)
        return Response(serializer.data)

    @rest_login_required
    def create(self, request):
        chartset = Chartset.objects.create(name=request.POST.get('name'))
        chartset.save()
        chartset.userschartsets.add(request.user)
        serializer = ChartsetSerializer(chartset)

        email_admin.delay(serializer.data)

        return Response(serializer.data)

@api_view(['GET'])
def сhs_search(request):
    queryset = ChartsetDocument.search().filter("term", name=request.GET.get('name'))
    queryset = queryset.to_queryset()
    serializer = ChartsetSerializer(queryset, many=True)
    return Response(serializer.data)

    #def validate():
