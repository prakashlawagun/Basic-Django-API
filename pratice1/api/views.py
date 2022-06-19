from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse


# Create your views here.

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created.'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/data')
            return  JsonResponse(serializer.data)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/data')
        return JsonResponse(serializer.data)
