'''
Artificial Inteligence 2 Assignment
Matthew O'Neill / C11354316 + Colin Delaney / C11378456
'''

import os
import sys
import numpy as np
from sklearn import tree


#globals
data_dir ="data"
solutions_dir = "solutions"
queries_file_path = os.path.join(data_dir, 'queries.txt')
training_set_file_path = os.path.join(data_dir, 'trainingset.txt')
solutions_file_path = os.path.join(solutions_dir, 'C11354316+C11378456.txt')


def setup_files():
    #create directories if they don't exist
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    if not os.path.isdir(solutions_dir):
        os.mkdir(solutions_dir)

    #we don't want to continue if the files aren't there
    if not os.path.isfile(queries_file_path) or not os.path.isfile(training_set_file_path):
        print ("data file(s) not found...")
        sys.exit(1)


def load_csv(fp, cols, dtype=np.float32):
    return np.genfromtxt(fp, delimiter=',', usecols=cols, dtype=dtype)


if __name__ == '__main__':
    setup_files()

    #the training data minus id and type:
    t_num_data = load_csv(training_set_file_path, range(1, 55))
    #the training type column
    t_type_col = load_csv(training_set_file_path, 55, dtype=np.dtype((str, 5)))
    #the query data minus id and type:
    q_data = load_csv(queries_file_path, range(1, 55))
    #the query id column
    q_id = load_csv(queries_file_path, 0, dtype=np.dtype((str, 10)))


    #fit data above to DTC and predict it
    model = tree.DecisionTreeClassifier(criterion='entropy')
    model.fit(t_num_data, t_type_col)
    predictions = model.predict(q_data)


    #output the predictions:
    with open(solutions_file_path, 'w') as f:
        for i in range(len(predictions)):
            f.write("{},{}\n".format(q_id[i], predictions[i]))
