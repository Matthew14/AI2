'''
Artificial Inteligence 2 Assignment
Matthew O'Neill / C11354316 + Colin Delaney / C11378456
'''

import os
import sys
import numpy


data_dir = "data"
solutions_dir = "solutions"

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)
if not os.path.isdir(solutions_dir):
    os.mkdir(solutions_dir)

queries_file_path = os.path.join(data_dir, 'queries.txt')
training_set_file_path = os.path.join(data_dir, 'trainingset.txt')
solutions_file_path = os.path.join(solutions_dir, 'C11354316+C11378456.txt')

if not os.path.isfile(queries_file_path) or not os.path.isfile(training_set_file_path):
    print ("data file(s) not found...")
    sys.exit(1)


if __name__ == '__main__':
    pass

