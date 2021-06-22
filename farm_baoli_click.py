import pyautogui
import time,sys,os
from pathlib import Path
from PIL import Image
#### Prerequisite:
#### (--index-url https://pypi.douban.com/simple)
####    python -m pip install PyAutoGUI
####    python -m pip install Pillow
####    python -m pip install pywin32 [win32gui is a part of it]


#Initial Variables
pyautogui.PAUSE = 1           # delay x seconds for all the functions
pyautogui.FAILSAFE = False


#png_folder = str(screenWidth) + "X" + str(screenHeight) + "\\"           #choose the screen pixels folder
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

tmp_scrshot = png_folder + 'tmp.png'

def ClickPng(png,qty=1):
    try:
        x, y = pyautogui.locateCenterOnScreen(png)
        if qty == 2:
            pyautogui.doubleClick(x, y)
        elif qty == 1:
            pyautogui.click(x, y)
        print(png + " clicked.")
        #break
        return 1
    except:
        print(png + " not found;")
        time.sleep(0.5)             #sleep 1.5s 
        return 0

def Screenshot(x, y):
    area = (x, y, x + 20, y + 20)
    img = Image.open(tmp_scrshot)
    img2 = img.crop(area)
    img2.save(tmp_scrshot)
    print("new screenshot saved with " + str(area))

#pyautogui.screenshot


####################################################
############# Main Program #########################

a1 = (859,523)
a2 = (902,517)
a3 = (933,509)


i = 0
while i < 10000:
    i = i + 1
    pyautogui.doubleClick(1234, 452, 2)
    time.sleep(0.05)

#pyautogui.typewrite(str(tmppage), interval=0.1)
#pyautogui.press('enter')
#os.remove("tmp\\"+"a.png")
#pyautogui.hotkey('alt', 'f4')

