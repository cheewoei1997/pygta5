import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os

path = 'training4'

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)


train_data = np.load(os.path.join(folder, 'training_data-1v2.npy'))
print(train_data.shape)

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test', img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break