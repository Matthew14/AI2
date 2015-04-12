'''
Artificial Inteligence 2 Assignment
Matthew O'Neill / C11354316 + Colin Delaney / C11378456
'''

import os
import sys
import numpy as np
import pandas as pd


data_dir = "data"
solutions_dir = "solutions"


#create directories if they don't exist
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


def get_headings():
    headings = ['id','Elevation','Aspect','Slope','Horizontal_Distance_To_Hydrology','Vertical_Distance_To_Hydrology','Horizontal_Distance_To_Roadways','Hillshade_9am','Hillshade_Noon','Hillshade_3pm','Horizontal_Distance_To_Fire_Points','Rawah_Wilderness_Area', 'Neota_Wilderness_Area', 'Comanche_Peak_Wilderness_Area', 'Cache_la_Poudre_Wilderness_Area']

    for i in range (1, 41):
        headings.append("Soil_Type_{}".format(i))

    headings.append('Cover_Type')
    return headings

if __name__ == '__main__':
    headings = get_headings()
    csv =  pd.read_csv(training_set_file_path)
