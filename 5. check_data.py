import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os
import time

train_no = 'training14'
train_type = 'raw'

# Get address of current working directory
folder =  os.path.join(os.getcwd(), 'training', train_no)
# Gets all contents of the address of folder
filenames = os.listdir(folder)
# Start at which training file
count = 1

for filename in filenames:
        try:
                train_data = np.load(os.path.join(folder, '{}_{}-{}.npy'.format(train_no, train_type, count)))
        except:
                print('Something went wrong at', count)
                break

        
        print('='*80)
        print(' '*80)
        print('{}_{}-{}.npy'.format(train_no, train_type, count))
        print(train_data.shape)
        print(' '*80)
        print('='*80)
        # time.sleep(3)
        # shuffle(train_data)

        # Check images in the array individually
        # for data in train_data:
        #         img = data[0]
        #         choice = data[1]
        #         cv2.imshow('test', img)
        #         print(choice)
        #         if cv2.waitKey(25) & 0xFF == ord('q'):
        #                 cv2.destroyAllWindows()
        #                 break
        
        count += 1

# ================================================================================
