import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

WIDTH = 400
HEIGHT = 300

GAME_WIDTH = 400
GAME_HEIGHT = 300

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

starting_value = 1
train_no = 'training18'
training_type = 'raw'

# ================================================================================

curr_dir = os.path.join(os.getcwd(), 'training', train_no)
if os.path.isdir(curr_dir):
    print('{} exists, saving here.'.format(train_no))

else:
    os.system('mkdir {}'.format(curr_dir))
    print('Created {} folder.'.format(train_no))

while True:
    file_name = os.path.join(os.getcwd(), 'training', '{}/{}_{}-{}.npy'.format(train_no, train_no, training_type, starting_value))

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        
        break


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = grab_screen(region=(200, 250, 199+GAME_WIDTH,249+GAME_HEIGHT))
            last_time = time.time()
            # resize to something a bit more acceptable for a CNN
            # screen = cv2.resize(screen, (WIDTH, HEIGHT))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

            # Show what is captured
            # cv2.imshow('window', screen)
            # time.sleep(0.2)
            # if cv2.waitKey(25) & 0xFF == ord('q'):
            #     cv2.destroyAllWindows()
            #     break
            
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])

            # Show training data array
            # print(training_data)

            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
##            cv2.imshow('window',cv2.resize(screen,(640,360)))
##            if cv2.waitKey(25) & 0xFF == ord('q'):
##                cv2.destroyAllWindows()
##                break

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 500:
                    np.save(file_name,training_data)
                    file_name = os.path.join(os.getcwd(), 'training', '{}/{}_{}-{}.npy'.format(train_no, train_no, training_type, starting_value))
                    print('=' * 80)
                    print('SAVED', file_name)
                    print('=' * 80)
                    training_data = []
                    starting_value += 1

                    
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main(file_name, starting_value)
