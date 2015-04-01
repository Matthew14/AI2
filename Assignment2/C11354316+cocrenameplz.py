'''
Artificial Inteligence 2 Assignment
Matthew O'Neill / C11354316 + Colin Delaney / numberhere
'''

import os
import sys
import numpy


data_dir = "data"
queries_file_path = os.path.join(data_dir, 'queries.txt')
training_set_file_path = os.path.join(data_dir, 'trainingset.txt')

if not os.path.isfile(queries_file_path) or not os.path.isfile(training_set_file_path):
    print "data file(s) not found..."
    sys.exit(1)


if __name__ == '__main__':
    pass
