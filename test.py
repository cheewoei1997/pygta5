import numpy as np
import cv2

train_data = np.load('training3test/new_training_data-4.npy')
print(train_data.shape)
print(train_data[0])
# cv2.imshow('test', train_data[1])

# some_list = [0,1,2,3,4,5,6,7,8,9]

# print(some_list[:4])
# print(some_list[4:])
# print(some_list[:-4])
# print(some_list[-4:])