"""
Matthew O'Neill/C11354316
AI2 Assignment 1
16/02/15
"""

import csv
import os
import numpy


def get_feature_names(file_path):
    if not os.path.isfile(file_path):
        raise IOError('file doesn\'t exist')

    with open(file_path, 'r') as f:
        return [l.rstrip() for l in f.readlines() if l != '\n']


def load_data_set(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        return numpy.array(list(reader))


def output_cont_report():
    outfile = 'c11354316CONT.csv'
    pass #TODO


def output_cat_report():
    outfile = 'c11354316CAT.csv'
    pass #TODO


if __name__ == "__main__":
    data_set_file = './data/DataSet.txt'
    feature_names_file = './data/featurenames.txt'

    ds = load_data_set(data_set_file)
