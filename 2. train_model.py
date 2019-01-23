import numpy as np
from grabscreen import grab_screen
import cv2
import time
import os
import pandas as pd
from tqdm import tqdm
from collections import deque
from models import alexnet3 as alexnet
from models import inception_v3 as googlenet
from random import shuffle
import tensorflow as tf


FILE_I_END = 7

WIDTH = 400
HEIGHT = 300
LR = 1e-3
EPOCHS = 30

# MODEL_NAME = 'testv4.1-{}-{}.model'.format(LR, EPOCHS)
# PREV_MODEL = 'testv4.1-{}-{}.model'.format(LR, EPOCHS)

# MODEL_SAVE_LOC = os.path.join('m-inception_v3', MODEL_NAME)
# MODEL_SAVE_LOC = os.path.join(os.getcwd(), MODEL_SAVE_LOC)

# PREVM_SAVE_LOC = os.path.join('m-inception_v3', MODEL_NAME)
# PREVM_SAVE_LOC = os.path.join(os.getcwd(), MODEL_SAVE_LOC)

MODEL_NAME = 'm-alexnetv4-{}-{}'.format(LR, EPOCHS)
PREV_MODEL = 'm-alexnetv4-{}-{}'.format(LR, EPOCHS)

MODEL_SAVE_LOC = os.path.join('m-alexnetv4-1050ti-11520', MODEL_NAME)
MODEL_SAVE_LOC = os.path.join(os.getcwd(), MODEL_SAVE_LOC)

PREVM_SAVE_LOC = os.path.join('m-alexnetv4-1050ti', MODEL_NAME)
PREVM_SAVE_LOC = os.path.join(os.getcwd(), MODEL_SAVE_LOC)

# Specially for alexnet
# MODEL_NAME = 'model_alexnet-46782'
# MODEL_SAVE_LOC = 'model_alexnet-46782'
# PREVM_SAVE_LOC = 'model_alexnet-46782'

print(MODEL_SAVE_LOC)
print(PREVM_SAVE_LOC)

LOAD_MODEL = False

wl = 0
sl = 0
al = 0
dl = 0

wal = 0
wdl = 0
sal = 0
sdl = 0
nkl = 0

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

# model = alexnet3(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)
model = alexnet(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)

if LOAD_MODEL:
    model.load(PREVM_SAVE_LOC)
    print('We have loaded a previous model!!!!')
    # print('Loading model from the checkpoint...')
    # checkpoint = tf.train.latest_checkpoint('checkpoint')
    # saver.restore(sess, checkpoint)
    

# iterates through the training files


for e in range(EPOCHS):
    #data_order = [i for i in range(1,FILE_I_END+1)]
    print('EPOCH: ', e)
    data_order = [i for i in range(1,FILE_I_END+1)]
    shuffle(data_order)
    for count,i in enumerate(data_order):
        
        try:
            file_name = 'D:/Github/pygta5/training/training8/training8_complete-{}v1.npy'.format(i)
            # full file info
            train_data = np.load(file_name)
            print('Training', file_name, len(train_data))

##            # [   [    [FRAMES], CHOICE   ]    ] 
##            train_data = []
##            current_frames = deque(maxlen=HM_FRAMES)
##            
##            for ds in data:
##                screen, choice = ds
##                gray_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
##
##
##                current_frames.append(gray_screen)
##                if len(current_frames) == HM_FRAMES:
##                    train_data.append([list(current_frames),choice])


            # #
            # always validating unique data: 
            split_data = round(len(train_data)/10)

            shuffle(train_data)
            train = train_data[:-split_data]
            test = train_data[-split_data:]

            X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,3)
            Y = [i[1] for i in train]

            gpu_options = tf.GPUOptions(allow_growth=True)

            test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,3)
            test_y = [i[1] for i in test]

            # model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            #     snapshot_step=2500, show_metric=True, run_id=MODEL_NAME, batch_size=4)
            model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
                snapshot_step=2500, show_metric=True, run_id=MODEL_NAME, batch_size=4)


            # if count%100 == 0:
            #     print('SAVING MODEL!')
            #     model.save(MODEL_NAME)

            os.system('copy m-alexnetv4-1050ti m-alexnetv4-1050ti-backup')
            print('Backup done')

            print('SAVING MODEL at', MODEL_SAVE_LOC)
            model.save(MODEL_SAVE_LOC)
            print('MODEL SAVED')
                    
        except Exception as e:
            print(str(e))
            
    








#

#tensorboard --logdir=foo:C:/Github/pygta5

