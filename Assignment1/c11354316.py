"""
Matthew O'Neill/C11354316
AI2 Assignment 1
16/02/15
"""

import csv
import os
import numpy
from functools import wraps


#function wrapper to check first parameter of a func is a file that exists
def check_file_exists(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if len(args) < 1 or not os.path.isfile(args[0]):
            raise IOError('file doesn\'t exist')
        return f(*args, **kwargs)
    return decorated_function


@check_file_exists
def get_feature_names(file_path):
    with open(file_path, 'r') as f:
        return [l.rstrip() for l in f.readlines() if l != '\n']


@check_file_exists
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

    # ds = load_data_set(data_set_file)

    get_feature_names(feature_names_file)

