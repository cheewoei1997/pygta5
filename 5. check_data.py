import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os
import time

path = 'training8'

# Get address of current working directory
folder =  os.path.join(os.getcwd(), 'training', path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

# ================================================================================

# train_data = np.load(os.path.join(folder, 'training7_data-13v1.npy'))
# # shuffle(train_data)
# print(train_data.shape)

# for data in train_data:
#         img = data[0]
#         choice = data[1]
#         cv2.imshow('test', img)
#         print(choice)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#                 break

# ================================================================================

count = 1

for filename in filenames:
        try:
                train_data = np.load(os.path.join(folder, 'training8_complete-{}v1.npy'.format(count)))
        except:
                print('Something went wrong at', count)
                break

        
        print('='*80)
        print(' '*80)
        print('training8_data-{}v1.npy'.format(count))
        print(train_data.shape)
        print(' '*80)
        print('='*80)
        time.sleep(3)
        # shuffle(train_data)

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
