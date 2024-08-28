import time
import mouse
import keyboard
import tkinter as tk
import datetime as dt
import getpixelcolor as gp 
from Data.lnkBank import linkBank as lB
import Data.InterfaceTextModule as GUIText
import Data.generalSmallFuncModule as GSFMod

comp, caixa, dem, log, NoFi, vale = lB.linkBank()

def hourDetermine():
    t = time.localtime()
    hour = int(time.strftime("%H", t))
    return hour

def dateDetermine():
    monthLength = [[2],[4,6,9,11],[1,3,5,7,8,10,12]]
    monthDay = [[28,29],30,31]
    month, year, weekday, today = GSFMod.calendarDateColector(True, "null")
    currentDate = dt.datetime(year, month, today)
    currentWeekDay = currentDate.weekday() + 2
    
    def monthDayProcessor(dateMonth):
        yearBigFeb = [2024,2028,2032,2036,2040]
        monthindex = 0
        for group, month in monthLength:
            if month == dateMonth:
                    monthindex = group
                    break
        returnDay = monthDay[monthindex]
        if year in yearBigFeb and returnDay == [28,29]:
            returnDay = monthDay[monthindex,1]
        else:
            returnDay = monthDay[monthindex,0]
        return returnDay

    def dateProcessor(flagValue,stringFlag):
        day = today - flagValue
        dateMonth = month
        if day <= 0:
            dateMonth = month - 1
            days = monthDayProcessor(dateMonth)
            actualDay = days + day
        else:
            actualDay = day

        if actualDay < 10:
            actualDay = "0" + str(actualDay)

        date = (str(actualDay) + stringFlag + str(dateMonth))
        fulldate = (str(actualDay) + stringFlag + str(dateMonth) + "." + str(year))
        return (date,fulldate)

    if month <10:
        if int(currentWeekDay) - 1 == 1:
            return dateProcessor(3,".0")
        else:
            return dateProcessor(1,".0")
    else:
        if int(currentWeekDay) - 1 == 1:
            return dateProcessor(3,".")
        else:
            return dateProcessor(1,".")

positions = [(118, 192),(902, 301),(910, 343),(908, 407),(905, 451),
             (867, 356),(874, 402),(1049, 349),(1160, 402),
             (955, 296),(985, 346),(1096, 301),(1120, 358)
             ]

def writeMail(flag,pos):
    keyboard.write(GSFMod.mailStrings(flag))
    time.sleep(0.7)
    posx,posy = positions[pos]
    mouse.move(posx, posy, absolute=True, duration=0.3)
    time.sleep(0.7)
    mouse.click('left')
    time.sleep(0.4)
    if GSFMod.mailStrings(flag) == 'comercial.aluguel@bykamy.com.br':
        pix1 = (253, 253, 253)
        pix2 = (53, 53, 53)
        pix3 = (73, 94, 102)
        if gp.pixel(1085, 409) == pix1 and gp.pixel(1071, 411) == pix2 and gp.pixel(1095, 419) == pix3:
            time.sleep(0.7)
            mouse.click('left')

def moveMouse(pos):
    posx,posy = positions[pos]
    mouse.move(posx, posy, absolute=True, duration=0.3)
    time.sleep(0.7)
    mouse.click('left')

def caixaMail():
    hour = hourDetermine()
    date, fulldate = dateDetermine()
    moveMouse(0)
    moveMouse(1)
#------------- Writing and selecting the mail -------------
    writeMail(6,5)
#----------------------------------------------------------
    moveMouse(2)
#------------- Writing and selecting the mail -------------
    writeMail(9,6)
    moveMouse(7)
    writeMail(10,8)
#-----------------------------------------------------------
    posx,posy = positions[3]
    mouse.move(posx, posy, absolute=True, duration=0.3)
    time.sleep(0.2)
    mouse.click('left')
    keyboard.write(GSFMod.mailStrings(12) + " " + date)
    posx,posy = positions[4]
    mouse.move(posx, posy, absolute=True, duration=0.3)
    time.sleep(0.4)
    mouse.click('left')
    time.sleep(0.4)
    mouse.click('left')
    if hour < 12:
        keyboard.write(GSFMod.mailStrings(1))
    elif hour > 12:
        keyboard.write(GSFMod.mailStrings(2))
    keyboard.press('enter')
    keyboard.release('enter')
    keyboard.write(GSFMod.mailStrings(4) + " " + fulldate +";")
    keyboard.press('enter')
    keyboard.release('enter')
    keyboard.write(GSFMod.mailStrings(5))
    time.sleep(0.3)
    GSFMod.loadLink(caixa)

def orçamentoMail(flag):
    hour = hourDetermine()
    moveMouse(0)
    moveMouse(1)
#------------- Writing and selecting the mail -------------
    if flag == 0:
        writeMail(6,5)
        moveMouse(9)
        writeMail(7,10)
        moveMouse(11)
        writeMail(8,12)
    elif flag == 1:
        writeMail(6,5)
        moveMouse(9)
        writeMail(7,10)
    elif flag == 2:
        moveMouse(11)
        writeMail(8,5)
#-----------------------------------------------------------
    moveMouse(2)
#------------- Writing and selecting the mail -------------
    writeMail(9,6)
    moveMouse(7)
    writeMail(10,8)
#-----------------------------------------------------------
    posx,posy = positions[4]
    mouse.move(posx, posy, absolute=True, duration=0.3)
    time.sleep(0.4)
    mouse.click('left')
    time.sleep(0.4)
    mouse.click('left')
    time.sleep(0.7)
    if hour < 12:
        keyboard.write(GSFMod.mailStrings(1))
    elif hour > 12:
        keyboard.write(GSFMod.mailStrings(2))
    keyboard.press('enter')
    keyboard.release('enter')
    keyboard.write(GSFMod.mailStrings(3))
    keyboard.press('enter')
    keyboard.release('enter')
    keyboard.write(GSFMod.mailStrings(5))
    time.sleep(0.3)
    GSFMod.loadLink(NoFi)


def mailWindow(container,uiFont,textFont,buttonFont):
#--------------------------------TextFrame------------------------------------------------
    textFrame = tk.Frame(container, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    contentCounter = 0
    for string in GUIText.mainMenuInterface():
        contentCounter += 1
        if contentCounter == 1 or contentCounter == 2:
            line = tk.Label(textFrame, text = string, font = uiFont, foreground="#00ff64", background="#001002")
            line.pack()
    line = tk.Label(textFrame, text ="郵便屋さん、お役に立ちます!!" , font = textFont, foreground="#00ff64", background="#001002")
    line.pack()
#---------------------------------ButtonFrame-----------------------------------------------
    mailFrame = tk.Frame(container, pady=10, bg="#001002")
    mailFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
    mailFrame.grid_rowconfigure(0, weight=1)
    mailFrame.grid_rowconfigure(2, weight=1)
    mailFrame.grid_columnconfigure(0, weight=1)
    mailFrame.grid_columnconfigure(1, weight=1)
    caixaButton = tk.Button(mailFrame, text="レジメール", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: caixaMail())
    orcamentoButton = tk.Button(mailFrame, text="予算", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: nfQuestion(True))
    buttons = [caixaButton,orcamentoButton]
    posc = 0
    for button in buttons:
        button.grid(row = 0, column = posc, sticky="n", pady = 6, padx = 2)
        posc += 1
#--------------------------------------HiddenFrame-------------------------------------------
#--------------------------------------HiddenFrameText>>
    nfTextFrame = tk.Frame(container, pady=10, bg="#001002")
    for string in GUIText.mainMenuInterface():
        contentCounter += 1
        if contentCounter == 1 or contentCounter == 2:
            line = tk.Label(nfTextFrame, text = string, font = uiFont, foreground="#00ff64", background="#001002")
            line.pack()
    line = tk.Label(nfTextFrame, text ="請求書は必要ですか?" , font = textFont, foreground="#00ff64", background="#001002")
    line.pack()
#------------------------------------HiddenFrameButton>>
    nfButtonFrame = tk.Frame(container, pady=10, bg="#001002")
    nfButtonFrame.grid_rowconfigure(0, weight=1)
    nfButtonFrame.grid_rowconfigure(2, weight=1)
    nfButtonFrame.grid_columnconfigure(0, weight=1)
    nfButtonFrame.grid_columnconfigure(1, weight=1)
    fullButton = tk.Button(nfButtonFrame, text="全体電子", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: backToMain(0))
    noNFButton = tk.Button(nfButtonFrame, text="請求書なし", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: backToMain(1))
    justNFButton = tk.Button(nfButtonFrame, text="請求書のみ", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: backToMain(2))
    buttons = [fullButton,noNFButton,justNFButton]
    posc = 0
    for button in buttons:
        button.grid(row = 0, column = posc, sticky="n", pady = 6, padx = 2)
        posc += 1
#-----------------------------------CallHiddenFrames------------------------------------------
    def nfQuestion(flag):
        if flag == True:
            textFrame.pack_forget()
            mailFrame.pack_forget()
            nfTextFrame.pack(side=tk.TOP, fill=tk.BOTH)
            nfButtonFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        elif flag == False:
            nfTextFrame.pack_forget()
            nfButtonFrame.pack_forget()
            textFrame.pack(side=tk.TOP, fill=tk.BOTH)
            mailFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
    def backToMain(flag):
        nfQuestion(False)
        orçamentoMail(flag)