import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os
import time

# training9, training10, training11, training12
# raw, balanced, complete
path = 'training9'
dataType = 'data'
count = 13

# Get address of current working directory
folder =  os.path.join(os.getcwd(), 'training', path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

try:
    train_data = np.load(os.path.join(folder, '{}_{}-{}v1.npy'.format(path, dataType, count)))
except:
    print('Something went wrong at', count)


print('='*80)
print(' '*80)
print('{}_{}-{}v1.npy'.format(path, dataType, count), train_data.shape)
print(' '*80)
print('='*80)
time.sleep(3)

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('Image', img)
    print(choice)
    cv2.imwrite('{}_{}-{}.jpeg'.format(path, dataType, count), img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
