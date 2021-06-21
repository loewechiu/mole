import pyautogui
import time,sys,os
import win32gui
import configparser
from pathlib import Path
#### Prerequisite:
#### (--index-url https://pypi.douban.com/simple)
####    python -m pip install PyAutoGUI
####    python -m pip install Pillow
####    python -m pip install pywin32 [win32gui is a part of it]


#Initial Variables
pyautogui.PAUSE = 1           # delay x seconds for all the functions
pyautogui.FAILSAFE = False

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

#png_folder = str(screenWidth) + "X" + str(screenHeight) + "\\"           #choose the screen pixels folder
png_folder = "icons\\"   
liandao_sel = png_folder + "liandao_sel.png"


def ClickPng(png,qty=1):
    tcount = 0
    while tcount < 50:
        try:
            x, y = pyautogui.locateCenterOnScreen(png)
            if qty == 2:
                pyautogui.doubleClick(x, y)
            elif qty == 1:
                pyautogui.click(x, y)
            #break
            return
        except:
            time.sleep(0.1)
            tcount = tcount + 1
            print("Scanning " + png + " ... " + str(tcount), end= "\r")
    
    print("button " + png + " not found")
    sys.exit()


    pyautogui.hotkey('alt', 'f4')

    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'f4')


def getFileName(filedir):
    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    return file_list if file_list else []

def removeFile():

####################################################
############# Main Program #########################


    pyautogui.typewrite(str(tmppage), interval=0.1)
    pyautogui.press('enter')


os.remove("tmp\\"+"a.png")


if is_repoll == "Yes":
    for i in range(start,end+1,1):
        tmp_file = Path(dir_book + "\\"+ str(i)+'.pdf')
        if tmp_file.is_file():
            continue
        else:
            #print(str(i) + " not exist.")
            relist.append(i)
else:                        # new poll
    for i in range(start,end+1,1):
        ClickPng(nextpage)
        Poll_page(i)

## Re-print the blank pages

for parent,dirnames,filenames in os.walk(dir_book):
    for filename in filenames:
        tmppage = int(filename[:-4])
        fullfile = dir_book + "\\" + filename
        Size=os.path.getsize(fullfile)
        if Size < 1024 and tmppage > 2:
            relist.append(tmppage)
            #print("Size of " + filename + ":\t" + str(Size))
            os.remove(fullfile)


for parent,dirnames,filenames in os.walk(dir_book):
    for filename in filenames:
        tmppage = int(filename[:-4])
        fullfile = dir_book + "\\" + filename
        Size=os.path.getsize(fullfile)

