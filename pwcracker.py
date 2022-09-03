from time import sleep
from datetime import datetime
import keyboard #you have to install this
import pyautogui #this too



toggle_key = 'z'
exit_key = 'Escape'
max_value = 1000
start_time = datetime.now()





def pixel_check():
    img = pyautogui.screenshot() # makes Screenshot. Due to performance it does not get stored
    pix = img.load()
    img_size = img.size # some math to scales coards to your diaplay
    faktor_x = 800/1920
    faktor_y = 511/1080
    exact_x = int(img_size[0]*faktor_x)
    exact_y = int(img_size[1]*faktor_y)
    if (pix[exact_x,exact_y][0]+pix[exact_x,exact_y][1]+pix[exact_x,exact_y][2])/3 == 139: #checks color of pixel is correct
        print("Pin is" + str(i-1))
        print("correct combination found! stopping...")
        print("Runtime: " + str(datetime.now() - start_time))
        exit()


print("Press " + toggle_key + " to start")
while True:
    if keyboard.is_pressed(exit_key): #exit while not running
            print("stopping")
            print("Runtime: " + str(datetime.now() - start_time))
            exit()
    if keyboard.is_pressed(toggle_key):
        print("Running...")
        for i in range(max_value):
            sleep(0.02)
            if keyboard.is_pressed(exit_key): #exit while running
                print("aborting")
                print("Runtime: " + str(datetime.now() - start_time))
                exit()
            keyboard.write(str(i)) #writes the current number
            pixel_check()
            for x  in range(len(str(i)) * 2): #deleting the written and some more 
                keyboard.write('\b')
        print("done")
        print("Runtime: " + str(datetime.now() - start_time))