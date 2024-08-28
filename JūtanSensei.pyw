import os
import subprocess
import tkinter as tk
from datetime import datetime
from tkinter.font import Font
import Data.calendarModule as cal
import Data.InterfaceTextModule as GUIText
import Data.generalSmallFuncModule as GSFMod
from win10toast import ToastNotifier as note
from Data.mailWriterModule import mailWindow as mail
from Data.logoScreen import loginProcedure as acsess
from Data.bankAssistModule import childConteiner as DB
from Data.functionModule import foldersWindow as folder
from Data.functionModule import userLoginWindow as login
from Data.LineCalculatorModule import popupLineCalcWindow as calc

Overlay = os.path.join(os.path.dirname(__file__), "Data", "scripts", "Overlay.ps1")
iconPath = os.path.join(os.path.dirname(__file__), "Data", "icons", "JuutanSenseiTitleBar.ico")

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", Overlay], startupinfo=startupinfo)

mainScreenFlag = True
notify = note()

root = tk.Tk()
root.geometry("315x540")
root.resizable(False, False)
root.title("JutanSensei")
root.configure(background="#001002")
root.iconbitmap(iconPath)
uiFont = Font(family = "Mincho", size = 13)
calendarFont = Font(family = "Mincho", size = 12)
textFont = Font(family = "Mincho", size = 14)
killDBFont = Font(family = "Arial", size = 6)
buttonFont = Font(family = "Mincho", size = 10)
#--------------MainFrame----------------------
mainFrame = tk.Frame(root, bg="#001002")
mainFrame.pack(side=tk.TOP, fill=tk.BOTH)

def successfulLogin(argument):
        for widget in mainFrame.winfo_children():
            widget.destroy()
            argument()

buttonList = []
def mainScreenLoop():

    #--------------TextFrame----------------------
    textFrame = tk.Frame(mainFrame, padx=10, bg="#001002", height = 50)
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    #--------------ButtonFrame--------------------
    buttonFrame = tk.Frame(mainFrame, padx=10, pady=10, bg="#001002", width = 340, height = 70)
    buttonFrame.pack(side=tk.TOP, fill=tk.BOTH)

    def exitApp():
        popup = tk.Toplevel(root, bg="#001002")
        popup.title("じゃね！")
        popup.geometry("300x50")
        label = tk.Label(popup, text="毎度ありがとうございます!!", font = textFont, foreground="#00ff64", background="#001002")
        label.pack(pady=10)
        root.after(3000, root.destroy)

    def info ():
        screenTimings = [1,2,3]
        screenTimer = 0
        logoScreen1 = GUIText.iniInterface(2)
        popup = tk.Toplevel(root, bg="#001002")
        popup.title("Info")
        popup.geometry(f"{340}x{150}")
        mainFrame = tk.Frame(popup, pady=10, bg="#001002")
        mainFrame.pack(side=tk.TOP, fill=tk.BOTH)

        for x in logoScreen1:
            if screenTimer in screenTimings:
                label = tk.Label(mainFrame, text= x, font = textFont, foreground="#00ff64", background="#001002")
                label.pack()
            else:
                label = tk.Label(mainFrame, text= x, font = uiFont, foreground="#00ff64", background="#001002")
                label.pack()
            screenTimer += 1

    def clearContainer():
        global mainScreenFlag
        mainScreenFlag = False
        for widget in containerFrame.winfo_children():
            widget.destroy()

    def changeScreens(flag):
        if flag == "f":
            clearContainer()
            folder(containerFrame,uiFont,textFont,buttonFont,root)
        elif flag == "l":
            clearContainer()
            login(containerFrame,uiFont,textFont,buttonFont,root)
        elif flag == "db":
            clearContainer()
            DB(containerFrame,uiFont,textFont,buttonFont,root,killDBFont)
        elif flag == "ml":
            clearContainer()
            mail(containerFrame,uiFont,textFont,buttonFont)

    def returnMainScreen(flag):
        global mainScreenFlag
        for button in buttonList:
            button.config(foreground="#00ff64", background="#001002")
        if flag == False:
            clearContainer()
            calendarFrame(containerFrame)
            mainScreenFlag = True
        if flag == True:
            exitApp()
        
    def calendarFrame(containerFrame):
        month, year, weekday, today = GSFMod.calendarDateColector(True, "null")
        colorCounter = 0
        posc = 0
        posr = 0
        upperFrame = tk.Frame(containerFrame, padx=10, bg="#001002",  width = 340, height = 20)
        upperFrame.pack(side=tk.TOP, fill=tk.BOTH)
        lowerFrame = tk.Frame(containerFrame, padx=10, bg="#001002",  width = 340)
        lowerFrame.pack(side=tk.TOP, fill=tk.BOTH)
        for x in range(0,7):
            lowerFrame.grid_columnconfigure(x, weight = 1)
        header =  cal.calendarFull(GSFMod.calendarDateColector(True, "null"), "h")
        label = tk.Label(upperFrame, text= header, font = textFont, foreground="#ff0010", background="#001032",relief = "sunken")
        label.pack()
        for item in cal.calendarFull(GSFMod.calendarDateColector(True, "null"), "b"):
            if colorCounter < 7:
                spot = tk.Label(lowerFrame, text= (item), font = textFont, foreground="#ff0010", background="#001032",relief = "sunken")
                spot.grid(row = posr, column = posc, sticky="nsew")
            elif colorCounter >= 7:
                if str(item) == str(today) or str(item) == ("0" + str(today)):
                    spot = tk.Label(lowerFrame, text= (item), font = textFont, foreground="#ff0010", background="#001002",relief = "sunken")
                    spot.grid(row = posr, column = posc, sticky="nsew")
                else:
                    spot = tk.Label(lowerFrame, text= (item), font = textFont, foreground="#00ff64", background="#001002",relief = "sunken")
                    spot.grid(row = posr, column = posc, sticky="nsew")
            posc += 1
            if posc == 7:
                posc = 0
                posr += 1
            colorCounter += 1



    def mainAppwindow():

        def buttonSelectionColor(flag):
            for button in buttonList:
                button.config(foreground="#00ff64", background="#001002")
            if flag == "1":
                folderButton.config(foreground="#ffffff", background="#640010")
                changeScreens("f")
            elif flag == "2":
                loginsButton.config(foreground="#ffffff", background="#640010")
                changeScreens("l")
            elif flag == "3":
                monthButton.config(foreground="#ffffff", background="#640010")
                cal.popUpGeneration(root,"月チェック",340,300,textFont,buttonFont,uiFont)
            elif flag == "4":
                bankButton.config(foreground="#ffffff", background="#640010")
                changeScreens("db")
            elif flag == "5":
                bulkCalcButton.config(foreground="#ffffff", background="#640010")
                calc(root,"電卓",200,200,textFont,buttonFont)
            elif flag == "6":
                mailButton.config(foreground="#ffffff", background="#640010")
                changeScreens("ml")

        def updateTime(timeLabel):
            currentTime = datetime.now().strftime("%H:%M:%S")
            timeLabel.config(text=currentTime)
            if datetime.now().strftime("%H:%M:%S") == "17:20:00":
                notify.show_toast(
                    "時が来た",
                    "帰ることの時だ",
                    threaded = True,
                    icon_path = None,
                    duration = 5
                )
            elif datetime.now().strftime("%H:%M:%S") == "10:00:00":
                 notify.show_toast(
                    "時が来た",
                    "JUGGERNAUT MK.IV はオンになっています",
                    threaded = True,
                    icon_path = None,
                    duration = 5
                 )
            root.after(1000, lambda: updateTime(timeLabel))
    #--------------Welcome Message--------------------------------------------------------------------------------------------------
        line1 = tk.Label(textFrame, text = GUIText.mainMenuInterface()[0], font = uiFont, foreground="#00ff64", background="#001002")
        line1.pack()
        line1 = tk.Button(textFrame, text = GUIText.mainMenuInterface()[2], font = textFont, foreground="#00ff64", background="#001002", command = lambda : info ())
        line1.pack()
        line1 = tk.Label(textFrame, text = GUIText.mainMenuInterface()[1], font = uiFont, foreground="#00ff64", background="#001002")
        line1.pack()
        contentCounter = 0
        for string in GUIText.mainMenuInterface():
            contentCounter += 1
            if contentCounter > 3:
                line = tk.Label(textFrame, text = string, font = textFont, foreground="#00ff64", background="#001002")
                line.pack()
        timeLabel = tk.Label(textFrame, font = textFont, foreground="#00ff64", background="#001064", relief = "sunken")
        timeLabel.pack()
        updateTime(timeLabel)
        #----------------------Buttons--------------------------------------------------------------------------------------------------------------
        buttonFrame.grid_rowconfigure(0, weight=1)
        buttonFrame.grid_rowconfigure(3, weight=1)
        buttonFrame.grid_columnconfigure(0, weight = 1)
        buttonFrame.grid_columnconfigure(2, weight = 1)
        folderButton =      tk.Button(buttonFrame, text="フォルダ", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: buttonSelectionColor("1"))
        loginsButton =      tk.Button(buttonFrame, text="ログイン", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: buttonSelectionColor("2"))
        monthButton =     tk.Button(buttonFrame, text="月チェック", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: buttonSelectionColor("3"))
        bankButton =     tk.Button(buttonFrame, text="データバンク", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: buttonSelectionColor("4"))
        bulkCalcButton =   tk.Button(buttonFrame, text="一括計算機", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: buttonSelectionColor("5"))
        mailButton =     tk.Button(buttonFrame, text="郵便局", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: buttonSelectionColor("6"))

        global buttonList
        buttonList = [folderButton,loginsButton,monthButton,bankButton,bulkCalcButton,mailButton]
        posr = 0
        posc = 0
        posCounter = 0
        for button in buttonList:
            posCounter += 1
            button.grid(row = posr, column = posc, sticky="n", pady = 3)
            posc += 1
            if posCounter == 6:
                posr = 2
                posc = 1
            else:
                if posc == 3:
                    posc = 0
                    posr += 1
                if posr == 4:
                    posr = 0

        calendarFrame(containerFrame)
    #--------------Conteiner----------------------
    containerFrame = tk.Frame(mainFrame, padx=10, bg="#001002",  width = 340, height = 20, relief = "sunken")
    containerFrame.pack(side=tk.TOP, fill=tk.BOTH)
    #----------------------------------CloseButton----------------------------------------------------------------------------------------------
    buttonFrame2 = tk.Frame(mainFrame, padx=10, pady=10, bg="#001002", width = 340, height = 70)
    buttonFrame2.pack(side=tk.TOP, fill=tk.BOTH)
    closeButton =  tk.Button(buttonFrame2, text="閉じる", foreground="#ffffff", background="#640010", width=11, height = 1, font = buttonFont, command = lambda: returnMainScreen(mainScreenFlag))
    closeButton.pack()
#---------------------------------------------------------------------------------------------------------------------------------------------
    mainAppwindow()

acsess(mainFrame,successfulLogin,mainScreenLoop)
root.mainloop()