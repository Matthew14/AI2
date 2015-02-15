"""
AI2 Assignment 1
Matthew O'Neill/C11354316
16/02/15
"""

import csv
import os
import numpy


data_set_file = './data/DataSet.txt'
feature_names_file = './data/featurenames.txt'


def get_feature_names(file_path):
    if not os.path.isfile(file_path):
        raise IOError('file doesn\'t exist')

    with open(file_path, 'r') as f:
        return [l.rstrip() for l in f.readlines() if l != '\n']

