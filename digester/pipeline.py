import os
import pandas
import numpy
import pickle
import json
from sklearn import linear_model
from sklearn.externals import joblib
from api.models import Biodigester
from django.core import serializers
from sklearn import neighbors

DUMP_JSON_PATH = '../data/bio_data.json'
DUMP_CSV_PATH = '../data/bio_data.csv'
FEATURES_NAMES = [
                    'temperature',
                    'internal_pressure',
                    'ph',
                    'gas_production',
                    'volume'
                ]

def dump_to_dataframe():
    #dump database to json
    print("dumping database to json")

    biodigesters = serializers.serialize('json', Biodigester.objects.all())
    biodigesters_json = json.loads(biodigesters)
    dump_dataframe = pandas.DataFrame.from_dict(biodigesters_json)
    fields_dataframe = dump_dataframe.fields

    #tran
    all_samples = []
    for i in range(0, len(fields_dataframe)):
        sample = [
                    fields_dataframe[i]['temperature'],
                    fields_dataframe[i]['internal_pressure'],
                    fields_dataframe[i]['ph'],
                    fields_dataframe[i]['gas_production'],
                    fields_dataframe[i]['volume']
                ]
        all_samples.append(sample)
    print(all_samples)

    all_samples_dataframe = pandas.DataFrame(data=all_samples, columns=FEATURES_NAMES)

    return all_samples_dataframe

def create_model():
    print("creating machine learning model")
    bio_dataframe = dump_to_dataframe()
    target = bio_dataframe['gas_production']
    data = bio_dataframe.drop(['gas_production'], axis=1)

    # particionar dados em treino e teste
    # .1 10% dos dados para teste
    # data_train, data_test, target_train, target_test = \
    #     train_test_split(data, target, test_size = .1)

    #print(data_test)
    print(data)

    regressor = neighbors.KNeighborsRegressor(n_neighbors = 1)
    regressor.fit(data, target)

    #joblib.dump(regressor, 'modelo.pkl')
    joblib.dump(regressor, '../modelo.pkl')

    return regressor
