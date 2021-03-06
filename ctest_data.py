import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from models import inception_v3 as googlenet
from models import alexnet3 as alexnet
from getkeys import key_check
from collections import deque, Counter
import random
from statistics import mode,mean
import numpy as np
from motion import motion_detection
import os

GAME_WIDTH = 400
GAME_HEIGHT = 300

how_far_remove = 800
rs = (20,15)
log_len = 25

motion_req = 800
motion_log = deque(maxlen=log_len)

WIDTH = 400
HEIGHT = 300
LR = 1e-3
EPOCHS = 30

sleep_duration = 0

trained_model = 'm-inceptionv3v15'
# weights = np.array([3.0, 1.0, 50, 50,  1.5,   1.5, 1.0, 1.0, 1.0])
# weights = np.array([0.5, 1.0, 0.5, 1.3, 1.0, 1.0, 1.0, 1.0, 0.6])
# weights = np.array([0.3, 1.0, 1.0, 15.0, 1.0, 1.0, 1.0, 1.0, 0.8])

weights = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
# weights = np.array([0.5, 1.0, 0.3, 1.3, 1.0, 1.0, 1.0, 1.0, 0.6])

# model = alexnet(WIDTH, HEIGHT, 3, LR, output=9)
model = googlenet(WIDTH, HEIGHT, 3, LR, output=9)
MODEL_NAME = os.path.join('models', '{}-1050ti'.format(trained_model), trained_model)
model.load(MODEL_NAME)
print('Model {}'.format(MODEL_NAME), ' loaded')

choices = deque([], maxlen=5)
hl_hist = 250
choice_hist = deque([], maxlen=hl_hist)

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

t_time = 0.25

def sleep():
    time.sleep(sleep_duration)

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)
    sleep()

def left():
    if random.randrange(0,3) == 1:
        PressKey(W)
    else:
        ReleaseKey(W)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)
    #ReleaseKey(S)
    sleep()

def right():
    if random.randrange(0,3) == 1:
        PressKey(W)
    else:
        ReleaseKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)
    sleep()
    
def reverse():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    sleep()


def forward_left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)
    sleep()
    
    
def forward_right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)
    sleep()

    
def reverse_left():
    PressKey(S)
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    sleep()

    
def reverse_right():
    PressKey(S)
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)
    sleep()

def no_keys():

    if random.randrange(0,3) == 1:
        PressKey(W)
        sleep()
    else:
        ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    mode_choice = 0

    screen = grab_screen(region=(0,40,GAME_WIDTH,GAME_HEIGHT+30))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    prev = cv2.resize(screen, (WIDTH,HEIGHT))

    t_minus = prev
    t_now = prev
    t_plus = prev

    while(True):
        
        if not paused:
            screen = grab_screen(region=(200,250,200+GAME_WIDTH,250+GAME_HEIGHT))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

            # cv2.imshow('window', screen)
            # if cv2.waitKey(25) & 0xFF == ord('q'):
            #     cv2.destroyAllWindows()
            #     break

            last_time = time.time()
            screen = cv2.resize(screen, (WIDTH,HEIGHT))
            # print(last_time)

            # delta_count_last = motion_detection(t_minus, t_now, t_plus)

            # t_minus = t_now
            # t_now = t_plus
            # t_plus = screen
            # t_plus = cv2.blur(t_plus,(4,4))

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,3)])[0]
            # print("%.5f" % (prediction))
            # prediction = np.array(prediction) * np.array([4.5, 0.1, 0.1, 0.1,  1.8,   1.8, 0.5, 0.5, 0.2])
            # prediction = np.array(prediction) * np.array([1.0, 0.1, 0.1, 0.1,  1.0,   1.0, 0.5, 0.5, 1.0])
            prediction = np.array(prediction) * weights

            # Print confidence level for each output
            print("w: %.5f" % (prediction[0]))
            print("s: %.5f" % (prediction[1]))
            print("a: %.5f" % (prediction[2]))
            print("d: %.5f" % (prediction[3]))
            print("wa: %.5f" % (prediction[4]))
            print("wd: %.5f" % (prediction[5]))
            print("sa: %.5f" % (prediction[6]))
            print("sd: %.5f" % (prediction[7]))
            print("nk: %.5f" % (prediction[8]))
            # print('prediction: {}'.format(prediction[1]))

            mode_choice = np.argmax(prediction)
            # print(mode_choice)

            if mode_choice == 0:
                straight()
                choice_picked = 'straight'
                
            elif mode_choice == 1:
                reverse()
                choice_picked = 'reverse'
                
            elif mode_choice == 2:
                left()
                choice_picked = 'left'
            elif mode_choice == 3:
                right()
                choice_picked = 'right'
            elif mode_choice == 4:
                forward_left()
                choice_picked = 'forward+left'
            elif mode_choice == 5:
                forward_right()
                choice_picked = 'forward+right'
            elif mode_choice == 6:
                reverse_left()
                choice_picked = 'reverse+left'
            elif mode_choice == 7:
                reverse_right()
                choice_picked = 'reverse+right'
            elif mode_choice == 8:
                no_keys()
                choice_picked = 'nokeys'

            # motion_log.append(delta_count)
            # motion_avg = round(mean(motion_log),3)
            # print('loop took {} seconds. Motion: {}. Choice: {}'.format( round(time.time()-last_time, 3) , motion_avg, choice_picked))
            print('loop took {} seconds. Choice: {}'.format( round(time.time()-last_time, 3) , choice_picked))

            # if motion_avg < motion_req and len(motion_log) >= log_len:
            #     print('WERE PROBABLY STUCK FFS, initiating some evasive maneuvers.')

            #     # 0 = reverse straight, turn left out
            #     # 1 = reverse straight, turn right out
            #     # 2 = reverse left, turn right out
            #     # 3 = reverse right, turn left out

            #     quick_choice = random.randrange(0,4)
                
            #     if quick_choice == 0:
            #         reverse()
            #         time.sleep(random.uniform(1,2))
            #         forward_left()
            #         time.sleep(random.uniform(1,2))

            #     elif quick_choice == 1:
            #         reverse()
            #         time.sleep(random.uniform(1,2))
            #         forward_right()
            #         time.sleep(random.uniform(1,2))

            #     elif quick_choice == 2:
            #         reverse_left()
            #         time.sleep(random.uniform(1,2))
            #         forward_right()
            #         time.sleep(random.uniform(1,2))

            #     elif quick_choice == 3:
            #         reverse_right()
            #         time.sleep(random.uniform(1,2))
            #         forward_left()
            #         time.sleep(random.uniform(1,2))

            #     for i in range(log_len-2):
            #         del motion_log[0]
    
        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                print('Paused')
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()       
