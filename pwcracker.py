from time import sleep
import keyboard

toggle_key = 'z'
exit_key = 'Escape'
max_value = 299

print("Press " + toggle_key + " to start")
while True:
    if keyboard.is_pressed(exit_key):
            print("stopping")
            exit()
    if keyboard.is_pressed(toggle_key):
        print("Running...")
        if True: #Add pixle detektion
            for i in range(max_value):
                sleep(0.05)
                if keyboard.is_pressed(exit_key):
                    print("aborting")
                    exit()
                keyboard.write(str(i)) #writes the current number
                for x  in range(len(str(i)) * 2): #deleting the written and some more 
                    keyboard.write('\b')
            print("done")