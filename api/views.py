from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from api.models import Biodigester
from api.serializers import BiodigesterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class BiodigestersViewSet(ModelViewSet):
    """
    List all code biodigesters, or create a new biodigester.
    """
    queryset = Biodigester.objects.all()
    serializer_class = BiodigesterSerializer

    def list(self, request):
        """
        API endpoint that allows list BiodigesterSerializer
        ---
        Response example:
        ```
        [
          {
            "id": 1,
            "water_flow": 110.5,
            "temperature": 40,
            "internal_pressure": 60,
            "ph": 7,
            "gas_production": 136
          },
          {
            "id": 2,
            "water_flow": 110.5,
            "temperature": 40,
            "internal_pressure": 60,
            "ph": 7,
            "gas_production": 136
          }
        ]
        ```
        """
        return super(BiodigestersViewSet, self).list(request)

    def create(self, request):
        """
        API endpoint biodigesters ...
        ---
        Body example:
        ```
        {
          "id": 2,
          "water_flow": 110.5,
          "temperature": 40,
          "internal_pressure": 60,
          "ph": 7,
          "gas_production": 136
        }
        ```
        Response example:
        ```
        {

        }
        ```
        """
        return super(BiodigestersViewSet, self).create(request)
# @csrf_exempt
# def biodigester_list(request):
#     """
#     List all code biodigesters, or create a new biodigester.
#     """
#     if request.method == 'GET':
#         biodigesters = Biodigester.objects.all()
#         serializer = BiodigesterSerializer(biodigesters, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BiodigesterSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def biodigester_detail(request, pk):
#     """
#     Retrieve, update or delete a code biodigester.
#     """
#     try:
#         biodigester = Biodigester.objects.get(pk=pk)
#     except Biodigester.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = BiodigesterSerializer(biodigester)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BiodigesterSerializer(biodigester, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         biodigester.delete()
#         return HttpResponse(status=204)
