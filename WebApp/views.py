from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .models import Task
from .serilazers import Task_Serializers

# Create your views here.


@api_view(['GET','POST'])
def task_details(request,pk):
    try:
        task=Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'message':'task does not exist'},status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        task_serializer=Task_Serializers(task)
        return JsonResponse(task_serializer.data)
@api_view(['GET'])
def published(request):
    task=Task.objects.filter(published=True)
    if request.method=='GET':
        task_serializer=Task_Serializers(task,many=True)
        return JsonResponse(task_serializer.data,safe=False)

@api_view(['GET','POST'])
def tasklist(request):
        if request.method=='GET':
            task=Task.objects.all().order_by('-id')
            title=request.GET.get('title',None)
            if title is not None:
                task=Task.filter(title__icontains=title)
            task_serializer=Task_Serializers(task,many=True)
            return JsonResponse(task_serializer.data,safe=False)

        elif request.method=='POST':
            task_data=JSONParser().parse(request)
            task_serializer=Task_Serializers(data=task_data
                                             )
            if task_serializer.is_valid():
                task_serializer.save()
                return JsonResponse(task_serializer.data,status=status.HTTP_201_CREATED)
            return JsonResponse(task_serializer.errors,status=status.HTTP_400_BAD_REQUEST)




