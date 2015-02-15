"""
Matthew O'Neill/C11354316
AI2 Assignment 1
16/02/15
"""

import csv
import os
import numpy as np
from functools import wraps
from collections import OrderedDict

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
        return [line.strip() for line in f.readlines() if line.strip() != '']


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
    cont_and_cats = dict()
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
        cont_and_cats[i] = cont if is_numeric(data_set[full_line_index][i].strip()) else cat

    conts = [k for k in cont_and_cats.keys() if cont_and_cats[k] == 'continuous']
    cats = [k for k in cont_and_cats.keys() if cont_and_cats[k] == 'categorical']

    return conts, cats


def output_report(feature_dict, outfile):

    with open(outfile, 'w') as f:
        writer = csv.writer(f)
        headings = ['FEATURENAME']
        headings.extend(list(feature_dict[list(feature_dict.keys())[0]].keys()))

        writer.writerow(headings)

        for k, v in feature_dict.items():
            fn = k
            vals = v.values()
            row = [k]
            row.extend(list(vals))
            writer.writerow(row)


def create_and_output_cont_report(data_set, conts, feature_names):
    outfile = './data/c11354316CONT.csv'

    data_set_len = len(data_set)
    feature_dict = OrderedDict()

    for feature in conts:
        feature_name = feature_names[feature]

        feature_dict[feature_name] = OrderedDict()
        feature_dict[feature_name]['missing_vals'] = 0

        #convert from string type to floats for this numeric col
        col = np.array(data_set[:, feature], dtype='float')
        non_zero_col = col[np.nonzero(col)] #remove 0 (missing)

        for i in range (len(col)):
            if col[i] == 0:
                feature_dict[feature_name]['missing_vals'] += 1

        feature_dict[feature_name]['min'] = np.min(non_zero_col)
        feature_dict[feature_name]['max'] = np.max(non_zero_col)
        feature_dict[feature_name]['mean'] = np.mean(non_zero_col)
        feature_dict[feature_name]['median'] = np.median(non_zero_col)
        feature_dict[feature_name]['std'] = np.std(non_zero_col)
        feature_dict[feature_name]['first_quartile'] = np.percentile(non_zero_col, 25)
        feature_dict[feature_name]['third_quartile'] = np.percentile(non_zero_col, 75)
        feature_dict[feature_name]['no_distinct'] = len(np.unique(non_zero_col))
        feature_dict[feature_name]['percent_missing'] = (feature_dict[feature_name]['missing_vals'] * 100) / len(col)

    output_report(feature_dict, outfile)


def create_and_output_cat_report(data_set, cats, feature_names):
    outfile = './data/c11354316CAT.csv'

    for feature in cats:
        feature_name = feature_names[feature]



if __name__ == "__main__":
    data_set_file = './data/DataSet.txt'
    feature_names_file = './data/featurenames.txt'

    data_set = load_data_set(data_set_file)
    feature_names = get_feature_names(feature_names_file)
    no_features = len(feature_names)

    assert len(data_set[0]) == no_features

    conts, cats = identify_cont_and_cat(data_set)

    create_and_output_cont_report(data_set, conts, feature_names)
    create_and_output_cat_report(data_set, cats, feature_names)
