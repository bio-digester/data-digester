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
from sklearn.externals import joblib
from digester.pipeline import create_model

regressor = joblib.load('./modelo.pkl')

class Optimize(APIView):
    def get(self, request, format=None):
        temperature_range = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
        volume_range = [0.3, 0.4, 0.5, 0.6, 0.7]
        pressure_range = [0.5, 0.75, 1.0]
        ph_range = [6.5, 6.0, 7.5]

        all_predictions = []
        for temperature in temperature_range:
            for internal_pressure in pressure_range:
                for ph in ph_range:
                    for volume in volume_range:
                        prediction = regressor.predict([[temperature, internal_pressure, ph, volume]])
                        all_predictions.append({'temperature': temperature,
                                                'internal_pressure': internal_pressure,
                                                'ph': ph,
                                                'volume': volume,
                                                'prediction': prediction[0]
                                                })
        return Response(all_predictions, status=status.HTTP_201_CREATED)

class DataPrepare:
    def prepare(data):
        samples_size = len(data)
        to_predict = []

        for i in range(0, samples_size):
            sample = [
                        data[i]['temperature'],
                        data[i]['internal_pressure'],
                        data[i]['ph'],
                        data[i]['volume']
            ]
            to_predict.append(sample)
        return to_predict

class Predict(APIView):
    def post(self, request, format=None):
        data = request.data
        to_predict = DataPrepare.prepare(data)

        try:
            print(to_predict)
            prediction = regressor.predict(to_predict)
        except:
            print("bad request")
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        prediction_serial = []
        for pred in prediction:
            pred_dict = {'gas_production': pred}
            prediction_serial.append(pred_dict)

        return Response(prediction_serial, status=status.HTTP_201_CREATED)


class BiodigesterList(APIView):
    """
    List all biodigesters, or create a new biodigester.
    """
    def get(self, request, format=None):
        biodigester = Biodigester.objects.all()
        serializer = BiodigesterSerializer(biodigester, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BiodigesterSerializer(data=request.data, many=True)
        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            create_model()
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
