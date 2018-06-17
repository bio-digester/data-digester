import os
import pandas
import numpy

DUMP_FILE_PATH = '../data/bio-data.json'
DUMP_CSV_PATH = '../data/bio-data.csv'
FEATURES_NAMES = [
                    'water_flow',
                    'temperature',
                    'internal_pressure',
                    'ph',
                    'gas_production',
                    'volume'
                ]
os.system('python3 ../manage.py dumpdata api > '+DUMP_FILE_PATH)

dump_dataframe = pandas.read_json(path_or_buf = DUMP_FILE_PATH)
fields_dataframe = dump_dataframe.fields

# print(fields_dataframe[0])
# print(fields_dataframe[0]['created'])

all_samples = []
for i in range(0, len(fields_dataframe)):
    sample = [
                fields_dataframe[i]['water_flow'],
                fields_dataframe[i]['temperature'],
                fields_dataframe[i]['internal_pressure'],
                fields_dataframe[i]['ph'],
                fields_dataframe[i]['gas_production'],
                fields_dataframe[i]['volume']
            ]
    all_samples.append(sample)

print(all_samples)

all_samples_dataframe = pandas.DataFrame(data=all_samples, columns=FEATURES_NAMES)
all_samples_dataframe.to_csv(path_or_buf = DUMP_CSV_PATH, index=False)
print(all_samples_dataframe)
