#
#

'read mnist CSV'

__author__ = 'hjkruclion'

import csv
import numpy as np
train_label = []
train_data = []
with open("mnist_test.csv", "r") as csvFile:
    reader = csv.reader(csvFile)

    for item in reader:
        x = np.zeros([10], np.float32)
        x[int(item[0])] = 1.0
        train_label.append(x)
        train_data.append(list(map(float, item[1:])))
print(train_label[0], train_data[0],  len(train_data[0]))