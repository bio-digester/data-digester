import pandas
import numpy
from read_data import read_labels

NUMBER_SAMPLES = 100
NUMBER_FEATURES = 4

def create_mock_data():

    samples = numpy.around(10 * numpy.random.rand(NUMBER_SAMPLES, NUMBER_FEATURES), decimals=3)
    labels = read_labels()

    data = pandas.DataFrame(data=samples, columns=labels)
    data.to_csv('../data/biodigester.csv', index=False, encoding='utf-8')

create_mock_data()
