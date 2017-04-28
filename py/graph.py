import os
from pandas import read_csv
from matplotlib import pyplot as plt
import numpy as np


os.chdir("..\\CSV\\data")

file = os.listdir()
data = read_csv(file[3])
array = np.array(data)
print()
