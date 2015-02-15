"""
Matthew O'Neill/C11354316
AI2 Assignment 1
16/02/15
"""

import csv
import os
import numpy as np
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
        return [line.strip() for line in f.readlines() if line.strip() != '\n']


@check_file_exists
def load_data_set(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        return np.array(list(reader))


def is_numeric(in_string):
    try:
        float(in_string)
        return True
    except:
        return False


def identify_cont_and_cat(data_set):
    cont_cat_dict = dict()
    cont = 'continuous'
    cat = 'categorical'
    full_line_index = -1

    for i in range(len(data_set)):
        for j in range(len(data_set[i])):
            if data_set[i][j].strip() == '?':
                break
        else:
            full_line_index = i
            break

    for i in range(len(data_set[full_line_index])):
        cont_cat_dict[i] = cont if is_numeric(data_set[full_line_index][i].strip()) else cat

    return cont_cat_dict


def output_cont_report():
    outfile = 'c11354316CONT.csv'
    pass #TODO


def output_cat_report():
    outfile = 'c11354316CAT.csv'
    pass #TODO


if __name__ == "__main__":
    data_set_file = './data/DataSet.txt'
    feature_names_file = './data/featurenames.txt'

    data_set = load_data_set(data_set_file)
    feature_names = get_feature_names(feature_names_file)
    no_features = len(feature_names)

    assert len(data_set[0]) == no_features
