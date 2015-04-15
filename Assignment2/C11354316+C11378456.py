'''
Artificial Inteligence 2 Assignment
Matthew O'Neill / C11354316 + Colin Delaney / C11378456
'''

import os
import sys
import numpy as np
import pandas as pd
import math
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn import cross_validation

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


def get_headings():
    headings = ['id','Elevation','Aspect','Slope','Horizontal_Distance_To_Hydrology','Vertical_Distance_To_Hydrology','Horizontal_Distance_To_Roadways','Hillshade_9am','Hillshade_Noon','Hillshade_3pm','Horizontal_Distance_To_Fire_Points','Rawah_Wilderness_Area', 'Neota_Wilderness_Area', 'Comanche_Peak_Wilderness_Area', 'Cache_la_Poudre_Wilderness_Area']

    headings.extend(["Soil_Type_{}".format(i) for i in range(1, 41)])
    headings.append('Cover_Type')

    return headings


if __name__ == '__main__':
    setup_files()

    #numeric are all headings up to Horizontal_Distance_To_Fire_Points
    headings = get_headings()
    numeric_headings = headings[:headings.index('Horizontal_Distance_To_Fire_Points') + 1]
    numeric_headings.pop(0)

    training_df =  pd.read_csv(training_set_file_path, names=headings)
    queries_df = pd.read_csv(queries_file_path, names=headings)
    numeric_cols = training_df[numeric_headings]
    cat_df = training_df.drop(numeric_cols, axis=1)

    # Merge Categorical and Numeric Descriptive Features
    # train_dfs = np.hstack((numeric_dfs.as_matri

    decTreeModel = tree.DecisionTreeClassifier(criterion='entropy')

    decTreeModel.fit(training_df, training_df['Cover_Type'])

    predictions = decTreeModel.predict([query[0],query[1]])
