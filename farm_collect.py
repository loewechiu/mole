import pyautogui
import time,sys,os
from pathlib import Path
from PIL import Image
#### Prerequisite:
#### (--index-url https://pypi.douban.com/simple)
####    python -m pip install pyautogui

#Initial Variables
pyautogui.PAUSE = 0.1          # delay x seconds for all the functions
pyautogui.FAILSAFE = False

png_folder = "icons\\"   
sickle_sel = png_folder + "sickle_sel.png"
axe_sel = png_folder + "axe_sel.png"
hammer_sel = png_folder + "hammer_sel.png"
sickle_press = png_folder + "sickle_press.png"
axe_press = png_folder + "axe_press.png"
hammer_press = png_folder + "hammer_press.png"
weapon = {hammer_sel:hammer_press,
            sickle_sel:sickle_press,
            axe_sel:axe_press}

def ClickPng(png,qty=1):
    try:
        box1 = pyautogui.locateCenterOnScreen(png)
        x,y = pyautogui.center(box1)
        if qty == 2:
            pyautogui.doubleClick(x, y)
        elif qty == 1:
            pyautogui.click(x, y)
        print(png + " clicked.")
        return 1
    except:
        print(png + " not found;")
        time.sleep(0.5)
        pyautogui.moveTo(0,0)
        return 0

def Press_key(key,seconds):
    start = time.time()
    while time.time() - start < seconds:
        pyautogui.press(key)

def JudgeScreenMove(ref_loc_shot,ref_loc):
    try:
        box1 = pyautogui.locateCenterOnScreen(ref_loc_shot)
        #x,y = pyautogui.center(box1)
        print(box1[0],box1[1])
        if box1[0] == ref_loc[0] and box1[1] == ref_loc[1]:
            return 0
        else:
            print("Screen moved.")
            return 1
    except:
        #time.sleep(0.5)             #sleep 1.5s
        print("Screen moved.")
        return 1

####################################################
############# Main Program #########################

try:
    loc1 = pyautogui.locateCenterOnScreen(sickle_sel)
    flag = 1
    ref_loc = (loc1[0],loc1[1]-200,loc1[2],loc1[3])
    ref_loc_shot = pyautogui.screenshot(region=ref_loc)
except:
    flag = 0

if flag == 0:
    print("Damm it! No farm icon found!")
    sys.exit()

print("located " + sickle_sel )


Press_key('d',1)

i = 0
ref_locked = 0
while i < 1000:
    i = i + 1
    
    if ref_locked > 5:
        Press_key('d',1)
        ref_locked = 0
        ref_loc_shot = pyautogui.screenshot(region=ref_loc)

    for j in (sickle_sel,axe_sel,hammer_sel):
        ClickPng(j,1)
        #time.sleep(0.1)

        while JudgeScreenMove(ref_loc_shot,ref_loc):
            ref_locked = 0
            ClickPng(weapon[j],2)
            #pyautogui.doubleClick(1234, 452, 2)
            time.sleep(0.3)
        
        ref_locked = ref_locked + 1