import cv2
import time
from grabscreen import grab_screen


while(True):
    screen = grab_screen(region=(200,250,199+400,249+300))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    cv2.imshow('window', screen)
    time.sleep(0.2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break