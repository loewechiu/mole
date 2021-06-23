import pyautogui
import time,sys,os
from pathlib import Path
from PIL import Image
#### Prerequisite:
#### (--index-url https://pypi.douban.com/simple)
####    python -m pip install pyautogui
## pip install--index-url https://pypi.douban.com/simple opencv-python

#Initial Variables
pyautogui.PAUSE = 0.1          # delay x seconds for all the functions
pyautogui.FAILSAFE = False

png_folder = "icons\\"   
out_bait = png_folder + "out_bait.png"
throw_bait = png_folder + "throw_bait.png"
in_water = png_folder + "in_water.png"
green_area = png_folder + "green_area.png"

fish_point = (16, 58, 121)


def ClickPng(png,qty=1):
    try:
        box1 = pyautogui.locateOnScreen(png,grayscale=False,confidence=0.9)
        x,y = pyautogui.center(box1)
        if qty == 2:
            pyautogui.doubleClick(x, y)
        elif qty == 1:
            pyautogui.click(x, y)
        print(png + " clicked.")
        pyautogui.moveTo(0,0)
        return 1
    except:
        print(png + " not found;")
        time.sleep(0.1)
        return 0

def FindPng(png):
    try:
        box1 = pyautogui.locateOnScreen(png,grayscale=False,confidence=0.99)
        return 1
    except:
        print(png + " not found;")
        return 0



####################################################
############# Main Program #########################
try:
    loc1 = pyautogui.locateOnScreen(throw_bait,grayscale=False,confidence=0.9)
    flag = 1
    print("fishing will be started...")
except:
    print("Damm it! Bait not found!")
    flag = 0
    sys.exit()

#ref_loc = (loc1[0]+300,loc1[1]-200,loc1[2],loc1[3])
loc_shot = pyautogui.screenshot(region=loc1)

area = loc1
count = 0


#img = pyautogui.screenshot(region=(615,351,30,30))
#print(img.getpixel((9,8)))
#sys.exit()
while 1:
    if ClickPng(out_bait,1):
        print("Out of bait, fishing stopped.")
        sys.exit()

    if ClickPng(throw_bait,1):
        count = count + 1
        print("Throw bait sequence: " + str(count))
        time.sleep(1)

    if not ClickPng(throw_bait,1) and not FindPng(in_water):
        try:
            area = pyautogui.locateOnScreen(green_area,grayscale=False,confidence=0.9)
        except:
            time.sleep(0.01)
        aa = pyautogui.screenshot(region=area)
        img = Image.open(aa)
        
        for i in range(0,aa[2]):
            for j in range(0,aa[3]):
                if img.getpixel((i,j)) == fish_point:
                    pyautogui.click(loc1[0], loc1[1])
                    time.sleep(0.1)
                    pyautogui.click(loc1[0], loc1[1])
        
    time.sleep(0.05)
