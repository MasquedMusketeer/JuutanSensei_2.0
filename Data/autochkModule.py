import time
import mouse
import keyboard
import getpixelcolor as gp 
from tkinter import messagebox
import Data.generalSmallFuncModule as GSFMod

listOfItems = []
listOfItemsNotPass = []
returnFlag = False

def Update(x):
    if x == []:
        listOfItems.clear()
    else:
        for y in x:
            if y not in listOfItems:
                listOfItems.append(y)
chkpix = 0
def verifyStep(x,y):
    global chkpix
    chkMousPosPix = gp.pixel(949, 610)
    if chkMousPosPix != (0, 0, 82) and gp.pixel(890, 572) == (253, 231, 233):
        mouse.move(962, 624, absolute=True, duration=0.3)
    elif chkMousPosPix != (0, 0, 82):
        mouse.move(949, 660, absolute=True, duration=0.3)
    else:
        mouse.move(949, 610, absolute=True, duration=0.3)
    mouse.click("left")
    time.sleep(0.7)
    chkpix = gp.pixel(881, 571)
    if chkpix != (253, 231, 233):
        listOfItemsNotPass.append(x + " \u25BA  " + y)

def scoutBot():
    global returnFlag
    for x in listOfItems:
        mouse.move(1404, 212, absolute=True, duration=0.3)
        mouse.click("left")
        mouse.move(1416, 287, absolute=True, duration=0.3)
        mouse.click("left")
        time.sleep(0.3)
        keyboard.write(x)
        time.sleep(0.3)
        verifyStep(x,"Avarias 1")
        mouse.move(239, 859, absolute=True, duration=0.3)
        mouse.click("left")
        verifyStep(x,"Lavados")
        mouse.move(382, 860, absolute=True, duration=0.3)
        mouse.click("left")
        verifyStep(x,"Restauro")
        mouse.move(597, 858, absolute=True, duration=0.3)
        mouse.click("left")
        verifyStep(x,"Avarias 2")
        mouse.move(128, 862, absolute=True, duration=0.3)
        mouse.click("left")
        mouse.move(1016, 343, absolute=True, duration=0.3)
        mouse.click("left")
    if listOfItemsNotPass == []:
        messagebox.showerror("絨毯先生", "エントリが見つかりません")
    else:
        stringbuffer = ""
        
        for x in listOfItemsNotPass:
            stringbuffer = stringbuffer + (str(x) + "\n")
        messagebox.showwarning("絨毯先生","エントリが見つかりました: \n \n" + stringbuffer)
    returnFlag = True

def listVerify():
    global returnFlag
    if not listOfItems:
        messagebox.showerror("Error", "エントリのリストが空です")
    else:
        scoutBot()
        if returnFlag == True:
            listOfItems.clear()
            listOfItemsNotPass.clear()
            returnFlag = False
