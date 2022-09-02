from time import sleep
import keyboard

toggle_key = 'z'
max_value = 299

def backspaces(): #this funktion deletes the input, cause i cant use an additional loop there. Yes hardcoding is bad but this is the easiest and i dont want to spend 5h to fix it.(len(str(i)) * 2)
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')
    keyboard.write('\b')

print("Press " + toggle_key + " to start")
while True:
    if keyboard.is_pressed('Escape'):
            print("stopping")
            exit()
    if keyboard.is_pressed(toggle_key):
        print("Running...")
        if True: #Add pixle detektion
            for i in range(max_value):
                if keyboard.is_pressed('Escape'):
                    print("exiting")
                    exit()
                sleep(0.05)
                if keyboard.is_pressed('Escape'):
                    print("exiting")
                    exit()
                keyboard.write(str(i))
                #backspaces()
            print("done")