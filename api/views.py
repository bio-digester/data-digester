from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Biodigester
from api.serializers import BiodigesterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BiodigesterList(APIView):
    """
    List all biodigesters, or create a new biodigester.
    """
    def get(self, request, format=None):
        biodigester = Biodigester.objects.all()
        serializer = BiodigesterSerializer(biodigester, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BiodigesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BiodigesterDetail(APIView):
    """
    Retrieve, update or delete a biodigester instance.
    """
    def get_object(self, pk):
        try:
            return Biodigester.objects.get(pk=pk)
        except Biodigester.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        biodigester = self.get_object(pk)
        serializer = BiodigesterSerializer(biodigester)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        biodigester = self.get_object(pk)
        serializer = BiodigesterSerializer(biodigester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        biodigester = self.get_object(pk)
        biodigester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
