import pandas
import numpy

def read_labels():
    labels = []
    file = open('../data/features_names.txt', 'r')
    for line in file:
        line = line[:-1]
        labels.append(line)
    return labels

def read_data():
    labels = read_labels()
    biodigester_data = pandas.read_csv('../data/biodigester.csv', sep=",")
    #target = biodigester_data['producao_gas']
    #data = biodigester_data.drop('producao_gas', axis=1)
    return biodigester_data

read_data()
