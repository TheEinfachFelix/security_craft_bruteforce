# security_craft_brutforce

This Script can be used to bypass the key locks from the [security craft](https://www.curseforge.com/minecraft/mc-mods/security-craft) Minecraft mod.

This should work for all Versions. Tested only for 1.12.2

## How to use:
First install these:

`pip install keyboard`

`pip install pyautogui`

`pip install Pillow --upgrade`


### Minecraft Setup:
Please do not play in fullscreen mode! Window mode only. Press F11 to switch modes. 
Task bar at the bottom please. If the bar is standart or double size does not matter. 

It will automatically scale to your display. As long its in 16:9

### How to run:
First set your range that you want to brute force using the `max_value` var. (it takes ca 2 min per 1000 combinations)
Then you run the script and go into Minecraft, open your target and press `z` to run it. `ESC` quits the script. 

Also the output of the combination might only be in the area of the true combination.
