import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os
import time

path = 'training18'
train_type = 'raw'

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
                train_data = np.load(os.path.join(folder, '{}_{}-{}.npy'.format(path, train_type, count)))
        except:
                print('Something went wrong at', count)
                break

        
        print('='*80)
        print(' '*80)
        print('{}_{}-{}.npy'.format(path, train_type, count), train_data.shape)
        # df = pd.DataFrame(train_data)
        # print(df.head())
        # print(Counter(df[1].apply(str)))
        print(train_data.shape)
        print(' '*80)
        print('='*80)
        time.sleep(3)

        # for data in train_data:
        #         img = data[0]
        #         print(img.shape)
        #         choice = data[1]
        #         cv2.imshow('test', img)
        #         print(choice)
        #         if cv2.waitKey(25) & 0xFF == ord('q'):
        #                 cv2.destroyAllWindows()
        #                 break
        
        count += 1

# ================================================================================
