import csv
from six.moves import cPickle as pickle
import numpy as np

def main(path_csv, path_pickle):

    x = []
    with open(path_csv,'rb') as f:
        reader = csv.reader(f)
        for line in reader: x.append(line)

    with open(path_pickle,'wb') as f:
        pickle.dump(x, f, pickle.HIGHEST_PROTOCOL)
