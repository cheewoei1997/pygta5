# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os


path = 'training3'

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

# for filename in filenames:
#     print(os.path.join(folder, filename))

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

count = 1

for filename in filenames:
    train_data = np.load(os.path.join(folder, filename))

    df = pd.DataFrame(train_data)
    print(df.head())
    print(Counter(df[1].apply(str)))

    lefts = []
    rights = []
    forwards = []

    wl = []
    sl = []
    al = []
    dl = []
    wal = []
    wdl = []
    sal = []
    sdl = []
    nkl = []

    ##shuffle(train_data)
    print(train_data.shape)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == w:
            wl.append([img,w])
        elif choice == s:
            sl.append([img,s])
        elif choice == a:
            al.append([img,a])
        elif choice == d:
            dl.append([img,d])
        elif choice == wa:
            wal.append([img,wa])
        elif choice == wd:
            wdl.append([img,wd])
        elif choice == sa:
            sal.append([img,sa])
        elif choice == sd:
            sdl.append([img,sd])
        elif choice == nk:
            nkl.append([img,nk])
        else:
            print('no matches')

    wl = wl[:len(wal)][:len(wdl)]
    al = al[:len(wl)]
    dl = dl[:len(wl)]
    sl = sl[:len(wl)]
    wal = wal[:len(wl)]
    wdl = wdl[:len(wl)]
    nkl = nkl[:len(wl)]

    print('nk: ', len(nkl))
    print('w: ', len(wl))
    print('a: ', len(al))
    print('d: ', len(dl))
    print('wa: ', len(wal))
    print('wd: ', len(wdl))

    final_data = wl + al + sl + dl + wal + wdl + sal + sdl + nkl
    shuffle(final_data)
    # print(final_data)

    np.save(os.path.join(folder, 'training_balanced{}v1.npy'.format(count)), final_data)
    count += 1

    ##forwards = forwards[:len(lefts)][:len(rights)]
    ##lefts = lefts[:len(forwards)]
    ##rights = rights[:len(forwards)]
    ##
    ##final_data = forwards + lefts + rights
    ##shuffle(final_data)
    ##
    ##np.save('training_data.npy', final_data)




