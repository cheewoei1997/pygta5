# import numpy as np
# import cv2
# import os

# train_data = np.load('training3test/new_training_data-4.npy')
# print(train_data.shape)
# print(train_data[0])
# cv2.imshow('test', train_data[1])

# some_list = [0,1,2,3,4,5,6,7,8,9]

# print(some_list[:4])
# print(some_list[4:])
# print(some_list[:-4])
# print(some_list[-4:])

# os.system('copy folder1 folder2')

# --------------------------------------------------------------------------------
# balanceData.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os


path = 'training8'

# Get address of current working directory
folder =  'C:/GitHub/pygta5/training/training8'
# Gets all contents of the address of folder
# filenames = os.listdir(folder)
filenames = ['training8_balanced-1v1.npy', 'training8_balanced-2v1.npy',
                'training8_balanced-3v1.npy', 'training8_balanced-4v1.npy',
                'training8_balanced-5v1.npy', 'training8_balanced-6v1.npy',
                'training8_balanced-7v1.npy', 'training8_balanced-8v1.npy',
                'training8_balanced-9v1.npy', 'training8_balanced-10v1.npy']

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

checkLen = 0
count = 1
count2 = 1

balanced = []
even_data = []

def main():
    for filename in filenames:
        train_data = np.load(os.path.join(folder, filename))
        print(filename, train_data.shape)

        # df = pd.DataFrame(train_data)
        # print(df.head())
        # print(Counter(df[1].apply(str)))

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

        shuffle(train_data)

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

        wl = wl[:len(al)][:len(dl)][:len(wal)][:len(wdl)][:len(nkl)]
        al = al[:len(wl)][:len(dl)][:len(wal)][:len(wdl)][:len(nkl)]
        dl = wl[:len(wl)][:len(al)][:len(wal)][:len(wdl)][:len(nkl)]
        wal = wal[:len(wl)][:len(al)][:len(dl)][:len(wdl)][:len(nkl)]
        wdl = wdl[:len(wl)][:len(al)][:len(dl)][:len(wal)][:len(nkl)]
        nkl = nkl[:len(wl)][:len(al)][:len(dl)][:len(wal)][:len(wdl)]

        # wl = wl[:len(al)][:len(dl)][:len(wdl)][:len(wal)][:len(nkl)]
        # wal = wal[:len(al)][:len(dl)][:len(wdl)][:len(wl)][:len(nkl)]
        # wdl = wdl[:len(al)][:len(dl)][:len(wl)][:len(wal)][:len(nkl)]
        # nkl = nkl[:len(al)][:len(dl)][:len(wdl)][:len(wal)][:len(wl)]

        print('nk: ', len(nkl))
        print('w: ', len(wl))
        print('a: ', len(al))
        print('s: ', len(sl))
        print('d: ', len(dl))
        print('wa: ', len(wal))
        print('wd: ', len(wdl))
        print('sa: ', len(sal))
        print('sd: ', len(sdl))

        # final_data = wl + al + sl + dl + wal + wdl + sal + sdl + nkl
        final_data = []
        final_data.extend(wl)
        final_data.extend(al)
        final_data.extend(sl)
        final_data.extend(dl)
        final_data.extend(wal)
        final_data.extend(wdl)
        final_data.extend(sal)
        final_data.extend(sdl)
        final_data.extend(nkl)
        shuffle(final_data)
        # print(final_data.shape)

        even_data.extend(final_data)
        print('Current length:', len(even_data))
        
        # balanced.extend(final_data)
        # # print(final_data)

        # # checkLen += int(len(final_data))
        # # print(checkLen)

        # # np.save(os.path.join(folder, 'training_balanced{}v1.npy'.format(count)), final_data)

        # if (count % 10 == 0):
        #     print('Data shape:', len(balanced))
        #     np.save(os.path.join(folder, 'training5_balanced{}v1.npy'.format(count2)), balanced)
        #     count2 += 1
        #     balanced = []

        # count += 1

    print('Final length:', len(even_data))
    # print(even_data)
    # np.save(os.path.join(folder, 'training_data-all.npy'), even_data)

    new_data = []
    count3 = 1
    count4 = 1
    print('Didn\'t skip this')
    for data in even_data:
        new_data.append(data)

        if count3 % 500 == 0:
            np.save('C:/GitHub/pygta5/training/training8/training8_complete-{}v1.npy'.format(count4), new_data)
            count4 += 1
            new_data = []

        count3 += 1


main()