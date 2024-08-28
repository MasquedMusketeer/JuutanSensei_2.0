import tkinter as tk
import keyboard as kb
import pyperclip as ppc
import Data.BankModule as bkm
from tkinter import messagebox
from Data.autochkModule import Update
import Data.InterfaceTextModule as GUIText
import Data.generalSmallFuncModule as GSFMod
from Data.autochkModule import listVerify as scoutBot


listOfEntries = []          # Entries currently loaded
flagValue = ["\u25BA NoBank \u25C4","#ff0010"]         #Bank ID of current list
entriesCache = []           #List of any entry that went to ListOfEntries during an app session. Resets on soft/hard startup
loadFlag = False            #flag to determine if current list was loaded from bank or inputed by user
loginFlag = True            #flag to determine permission for sensitive operations
functionReturn = ""
bankLoadFlag = False
#___________________ Credential verification function_________________
def updateLogin(flag):
    if flag == True:
        global loginFlag
        loginFlag = True

def clearList():
    global loadFlag
    global bankLoadFlag
    listOfEntries.clear()
    flagValue.clear()
    Update(listOfEntries)
    flagValue.append("\u25BA NoBank \u25C4")
    flagValue.append("#ff0010")
    loadFlag = False
    bankLoadFlag = False
#___________________ Save function_________________
def saveToBank(topFrame,bottomFrame,textFont,buttonFont,popup,root):
    global loginFlag
    global functionReturn
    def closeTab():
        global functionReturn
        functionReturn = ""
        popup.destroy()
    def save(entry):
        global functionReturn
        flag = entry.get()
        listOfFlags = bkm.data_bank.loadFlags()
        if flag in listOfFlags:
            if functionReturn == "":
                overwriteBankEntry(textFont,buttonFont,flag,root)
            if functionReturn == True:
                flagValue.clear()
                flagValue.append("\u25BA " + str(flag) + " \u25C4")
                flagValue.append("#00ff64")
                bkm.data_bank.save_list(flag, listOfEntries)
                Update(listOfEntries)
                closeTab()
            elif functionReturn == False:
                messagebox.showwarning("DataBank","変更は行われなかった")
                closeTab()
        else:
            flagValue.clear()
            flagValue.append("\u25BA " + str(flag) + " \u25C4")
            flagValue.append("#00ff64")
            bkm.data_bank.save_list(flag, listOfEntries)
            Update(listOfEntries)

    if loginFlag == False:
      messagebox.showwarning("Unauthorized",GSFMod.guestMessage(loginFlag))
    else:
        global loadFlag
        loadFlag = True
        text = tk.Label(topFrame, text = "DBから読み込みますか?", font = textFont, foreground="#00ff64", background="#001002")
        text.pack(pady = 10)
        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_columnconfigure(1, weight=1)
        listID = tk.Entry(bottomFrame, font = textFont, width = 10, foreground="#00ff64", background="#006410")
        saveButton = tk.Button(bottomFrame, text="セーブ", font = buttonFont, foreground="#00ff64", background="#001002", command=lambda: save(listID))
        lowerFrame = [listID,saveButton]
        posc = 0
        for widget in lowerFrame:
            widget.grid(row = 0, column = posc, sticky="n", pady = 1, padx = 2)
            posc += 1

   
    #___________________ Overwite function_________________
    def overwriteBankEntry(textFont,buttonFont,flag,root):
        global functionReturn
        popup2 = tk.Toplevel(root, bg="#001002")
        popup2.title('確認')
        popup2.geometry("250x100")
        mainFrame = tk.Frame(popup2, pady=10, bg="#001002")
        mainFrame.pack(side=tk.TOP, fill=tk.BOTH)
        #---------------------------TopFrame--------------------------------------------
        topFrame = tk.Frame(mainFrame, bg="#001002")
        topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #---------------------------BottomFrame-----------------------------------------
        bottomFrame = tk.Frame(mainFrame, bg="#001002")
        bottomFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #-------------------------------------------------------------------------------

        def choice(choice):
            global functionReturn
            if choice == 0:
                bkm.data_bank.delete_list(flag)
                functionReturn = True
                popup2.destroy()
            elif choice == 1:
                functionReturn = False
                popup2.destroy()
                
        
        text = tk.Label(topFrame, text = "すでにエントリがあります.", font = textFont, foreground="#00ff64", background="#001002")
        text2 = tk.Label(topFrame, text = "上書きしますか?", font = textFont, foreground="#00ff64", background="#001002")
        textLines = [text, text2]
        for text in textLines:
            text.pack(pady = 1)
        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_columnconfigure(1, weight=1)
        haiButton = tk.Button(bottomFrame, text="はい", font = buttonFont, foreground="#00ff64", background="#001002", command=lambda: choice(0))
        iieButton = tk.Button(bottomFrame, text="いいえ", font = buttonFont, foreground="#00ff64", background="#001002", command=lambda: choice(1))
        lowerFrame = [haiButton,iieButton]
        posc = 0
        for widget in lowerFrame:
            widget.grid(row = 0, column = posc, sticky="n", pady = 1, padx = 2)
            posc += 1
#___________________ Load function_________________
def loadFromBank(topFrame,bottomFrame,textFont,buttonFont,popup):
    def load(entry):
        flag = entry.get()
        data = bkm.data_bank.load_list(flag)
        if data != False:
            flagValue.clear()
            flagValue.append("\u25BA " + str(flag) + " \u25C4")
            flagValue.append("#00ff64")
            listOfEntries.clear()
            for x in data:
                listOfEntries.append(x)
                entriesCache.append(x)
            Update(listOfEntries)
        
        else:
            messagebox.showwarning("Failed load","リストが見つかりません")
        popup.destroy()
    if loginFlag == False:
      messagebox.showwarning("Unauthorized",GSFMod.guestMessage(loginFlag))
    else:
        global loadFlag
        loadFlag = True
        text = tk.Label(topFrame, text = "DBから読み込みますか?", font = textFont, foreground="#00ff64", background="#001002")
        text.pack(pady = 10)
        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_columnconfigure(1, weight=1)
        listID = tk.Entry(bottomFrame, font = textFont, width = 10, foreground="#00ff64", background="#006410")
        loadButton = tk.Button(bottomFrame, text="ロード", font = buttonFont, foreground="#00ff64", background="#001002", command=lambda: load(listID))
        lowerFrame = [listID,loadButton]
        posc = 0
        for widget in lowerFrame:
            widget.grid(row = 0, column = posc, sticky="n", pady = 1, padx = 2)
            posc += 1         
#___________________ Delete function_________________
def deleteFromBank(topFrame,bottomFrame,textFont,buttonFont,popup):
    def delete(entry):
        global loadFlag
        flag = entry.get()
        data = bkm.data_bank.load_list(flag)
        if data != False:
            flagValue.clear()
            flagValue.append("\u25BA NoBank \u25C4")
            flagValue.append("#ff0010")
            bkm.data_bank.delete_list(flag)
            listOfEntries.clear()
            loadFlag = False  
            messagebox.showwarning("Success","リストを削除しました!")          
        else:
            messagebox.showwarning("Failed operation","リストが見つかりません")
        popup.destroy()

    global loadFlag
    if loginFlag == False:
      messagebox.showwarning("Unauthorized",GSFMod.guestMessage(loginFlag))
    else:
        loadFlag = True
        text = tk.Label(topFrame, text = "DBから削除しますか?", font = textFont, foreground="#00ff64", background="#001002")
        text.pack(pady = 10)
        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_columnconfigure(1, weight=1)
        listID = tk.Entry(bottomFrame, font = textFont, width = 10, foreground="#00ff64", background="#006410")
        deleteButton = tk.Button(bottomFrame, text="削除", font = buttonFont, foreground="#00ff64", background="#001002", command=lambda: delete(listID))
        lowerFrame = [listID,deleteButton]
        posc = 0
        for widget in lowerFrame:
            widget.grid(row = 0, column = posc, sticky="n", pady = 1, padx = 2)
            posc += 1
#--------------------------PopupGenerator----------------------------------------------------------
def popupMainWindow(root,title,sizex,sizey,OPFlag,textFont,buttonFont):
    popup = tk.Toplevel(root, bg="#001002")
    popup.title(title)
    popup.geometry(f"{sizex}x{sizey}")
    mainFrame = tk.Frame(popup, pady=10, bg="#001002")
    mainFrame.pack(side=tk.TOP, fill=tk.BOTH)
#---------------------------TopFrame--------------------------------------------
    topFrame = tk.Frame(mainFrame, bg="#001002")
    topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#---------------------------BottomFrame-----------------------------------------
    bottomFrame = tk.Frame(mainFrame, bg="#001002")
    bottomFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#-------------------------------------------------------------------------------
    if OPFlag == 0:
        loadFromBank(topFrame,bottomFrame,textFont,buttonFont,popup)
    elif OPFlag == 1:
        saveToBank(topFrame,bottomFrame,textFont,buttonFont,popup,root)
    elif OPFlag == 2:
        deleteFromBank(topFrame,bottomFrame,textFont,buttonFont,popup)
    elif OPFlag == 3:
        loadEntry(topFrame,bottomFrame,textFont,buttonFont)
    elif OPFlag == 4:
        showEntry(topFrame,bottomFrame,buttonFont,popup)
#___________________ Delete Bank function_________________
def killDB(root,textFont,uiFont,killDBFont,buttonFont):
    popup = tk.Toplevel(root, bg="#001002")
    popup.title("データ")
    popup.geometry("340x430")
#--------------------------------TextFrame------------------------------------------------
    textFrame = tk.Frame(popup, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    uiLine1 = tk.Label(textFrame, text = GUIText.mainMenuInterface()[0], font = uiFont, foreground="#00ff64", background="#001002")
    textLine = tk.Label(textFrame, text = 'DBを強制終了しますか?', font = textFont, foreground="#00ff64", background="#001002")
    uiLine2 = tk.Label(textFrame, text = GUIText.mainMenuInterface()[1], font = uiFont, foreground="#00ff64", background="#001002")
    textElements = [uiLine1,textLine,uiLine2]
    for string in textElements:
        string.pack()
    for strings in GUIText.deathDBInterface():
        textLine = tk.Label(textFrame, text = strings, font = killDBFont, foreground="#00ff64", background="#001002")
        textLine.pack()
#---------------------------------ButtonFrame-----------------------------------------------
    buttonFrame = tk.Frame(popup, pady=10, bg="#001002")
    buttonFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
    buttonFrame.grid_rowconfigure(0, weight=1)
    buttonFrame.grid_rowconfigure(2, weight=1)
    buttonFrame.grid_columnconfigure(0, weight=1)
    buttonFrame.grid_columnconfigure(1, weight=1)
    confirmButton = tk.Button(buttonFrame, text="はい", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: killDBProcedure())
    denyButton = tk.Button(buttonFrame, text="いいえ", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: popup.destroy())
    buttons = [confirmButton,denyButton]
    posc = 0
    for button in buttons:
        button.grid(row = 0, column = posc, sticky="n", pady = 6, padx = 2)
        posc += 1

    def killDBProcedure():
        global loadFlag
        flagValue.clear()
        flagValue.append("NoBank")
        flagValue.append("#ff0010")
        bkm.data_bank.delete_data_bank()
        loadFlag = False
#___________________Function that displays all lists on the Bank_________________        
def showDB(root,textFont,uiFont):
    popup = tk.Toplevel(root, bg="#001002")
    popup.title("データ")
    popup.geometry("340x300")
#--------------------------------TextFrame------------------------------------------------
    textFrame = tk.Frame(popup, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    uiLine1 = tk.Label(textFrame, text = GUIText.mainMenuInterface()[0], font = uiFont, foreground="#00ff64", background="#001002")
    textLine = tk.Label(textFrame, text = 'DBに保存されたリスト', font = textFont, foreground="#00ff64", background="#001002")
    uiLine2 = tk.Label(textFrame, text = GUIText.mainMenuInterface()[1], font = uiFont, foreground="#00ff64", background="#001002")
    textElements = [uiLine1,textLine,uiLine2]
    for string in textElements:
        string.pack()
#---------------------------------ContentsFrame-----------------------------------------------
    popupDataFrame = tk.Frame(popup, bg="#001002")
    popupDataFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
    for col in range(4):
        popupDataFrame.grid_columnconfigure(col, weight=1)

    for row in range(len(bkm.data_bank.loadFlags()) // 4 + 1):
        popupDataFrame.grid_rowconfigure(row, weight=1)
    listOfFlags = bkm.data_bank.loadFlags()
    posc = 0
    posr = 0
    for flag in listOfFlags:
        label = tk.Label(popupDataFrame, text = "\u25BA "+flag, font = textFont, foreground="#00ff64", background="#001002")
        label.grid(row = posr, column = posc, sticky="n", pady = 3, padx = 3)
        posc += 1
        if posc == 4:
            posc = 0
            posr += 1

def loadEntry(topFrame,bottomFrame,textFont,buttonFont):
    statusString = ""
    possibleStatus = ["登録済み","有効でない","削除された","重複"]
    def updateStatusStrings(flag):
        if flag == 0:
            statusLabel.config(text = possibleStatus[0], font = buttonFont, foreground="#00ff64")
        elif flag == 1:
            statusLabel.config(text = possibleStatus[1], font = buttonFont, foreground="#ff0010")
        elif flag == 2:
            statusLabel.config(text = possibleStatus[2], font = buttonFont, foreground="#00ff64")
        elif flag == 3:
            statusLabel.config(text = possibleStatus[3], font = buttonFont, foreground="#ffa000")
        bottomFrame.after(1750, resetStatusLabel)

    def resetStatusLabel():
        statusLabel.config(text="")

    def load(numEntry,dell):
        global bankLoadFlag
        global statusString
        inputText = numEntry.get()
        if dell == 'del':
            listOfEntries.pop(-1)
            listBox.delete(0,None)
            updateStatusStrings(2)
            numEntry.delete(0, tk.END)
        elif inputText in listOfEntries and dell == "null":
            updateStatusStrings(3)
            numEntry.delete(0, tk.END)
        elif len(inputText) != 6 and dell == "null":
            updateStatusStrings(1)
            numEntry.delete(0, tk.END)
        elif len(inputText) == 6 and dell == "null":
            listBox.insert(0, inputText)
            listOfEntries.append(inputText)
            updateStatusStrings(0)
            numEntry.delete(0, tk.END)
        if bankLoadFlag == False:
            flagValue.clear()
            flagValue.append("\u25BA Unknown \u25C4")
            flagValue.append("#ffa000")
            bankLoadFlag = True

    topFrame.grid_columnconfigure(0, weight=1)
    topFrame.grid_columnconfigure(1, weight=1)
    numEntry = tk.Entry(topFrame, font = textFont, width = 10, foreground="#00ff64", background="#006410")
    loadButton = tk.Button(topFrame, text="削除", font = buttonFont, foreground="#00ff64", background="#001002", command=lambda: load(numEntry,'del'))
    upperFrame = [numEntry,loadButton]
    posc = 0
    for widget in upperFrame:
        widget.grid(row = 0, column = posc, sticky="n", pady = 1, padx = 2)
        posc += 1
    
    bottomFrame.grid_columnconfigure(0, weight=1)
    bottomFrame.grid_columnconfigure(1, weight=1)
    bottomFrame.grid_rowconfigure(0, weight=1)
    bottomFrame.grid_rowconfigure(1, weight=1)
    listBox = tk.Listbox(bottomFrame, font = buttonFont, foreground="#00ff64", background="#001002")
    statusLabel = tk.Label(bottomFrame, text = statusString, font = textFont, foreground="#00ff64", background="#001002")
    lowerFrame = [listBox,statusLabel]
    posc = 0
    for widget in lowerFrame:
        widget.grid(row = 0, column = posc, sticky="w", pady = 1, padx = 2)
        posc += 1
        def on_enter_key(event):
            load(numEntry,"null")
        numEntry.bind('<Return>', on_enter_key)
loadCounter = 0
def showEntry(handlerFrame,buttonFont):
    global loadCounter
    loadCounter = 0
    for widget in handlerFrame.winfo_children():
        widget.destroy()
    entryCounter = len(listOfEntries)
    def show():
        global loadCounter
        if entryCounter != 0:
            if loadCounter == entryCounter:
                textLabel2.config(text = "リストの終わり")
                loadCounter = 0
            else:
                textLabel2.config(text = listOfEntries[loadCounter])
                ppc.copy(listOfEntries[loadCounter])
                loadCounter += 1
        else:
            textLabel2.config(text = "??????")

    textLabel1 = tk.Label(handlerFrame, text = "現在選択されて\nいるエントリ:", font = buttonFont, foreground="#00ff64", background="#001002")
    textLabel2 = tk.Label(handlerFrame, font = buttonFont, foreground="#00ff64", background="#001002")
    loadButton = tk.Button(handlerFrame, text="次へ", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: show())

    upperFrame = [textLabel1,textLabel2,loadButton]
    for widget in upperFrame:
        widget.pack(pady = 5)


def clearContainer(buttonFrame):
    for widget in buttonFrame.winfo_children():
        widget.destroy()

def childConteiner(container,uiFont,textFont,buttonFont,root,killDBFont):
    childFrame = tk.Frame(container, pady=10, bg="#001002")
    childFrame.pack(side=tk.TOP, fill=tk.BOTH)
#--------------------------------TextFrame------------------------------------------------
    textFrame = tk.Frame(childFrame, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    contentCounter = 0
    for string in GUIText.mainMenuInterface():
        contentCounter += 1
        if contentCounter == 1 or contentCounter == 2:
            line = tk.Label(textFrame, text = string, font = uiFont, foreground="#00ff64", background="#001002")
            line.pack()
    for string in GUIText.dbMenuInterface():
        line = tk.Label(textFrame, text = string , font = textFont, foreground="#00ff64", background="#001002")
        line.pack()
#---------------------------------ButtonFrame-----------------------------------------------
    buttonFrame = tk.Frame(childFrame, bg="#001002")
    buttonFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
#---------------------------------HandlerMenuScreen-------------------------------------------------------------------------  
    def recieveInputMenu(buttonFrame,uiFont,textFont,buttonFont,root):
        handlerFrame = tk.Frame(buttonFrame, bg="#001002")
        handlerFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        loadButton = tk.Button(handlerFrame, text="ロード番号", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: popupMainWindow(root,"負荷員",250,200,3,textFont,buttonFont))
        sequenceButton = tk.Button(handlerFrame, text="順序", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: showEntry(handlerFrame,buttonFont))
        mainMenuButton = tk.Button(handlerFrame, text="開始", foreground="#ffffff", background="#640010", width=11, height = 1, font = buttonFont, command = lambda: updateScreen(0))
        widgets = [loadButton,sequenceButton,mainMenuButton]
        for item in widgets:
            item.pack(pady = 2)

#---------------------------------DBMenuScreen-------------------------------------------------------------------------  
    def DBMenu(buttonFrame,uiFont,textFont,buttonFont,root):
#---------------------------------ButtonFrame-----------------------------------------------
        bankFrame = tk.Frame(buttonFrame, bg="#001002")
        bankFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        saveButton = tk.Button(bankFrame, text="ロード", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: popupMainWindow(root,"ロード",250,100,0,textFont,buttonFont))
        loadButton = tk.Button(bankFrame, text="セーブ", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: popupMainWindow(root,"セーブ",250,100,1,textFont,buttonFont))
        deleteButton = tk.Button(bankFrame, text="削除", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: popupMainWindow(root,"削除",250,100,2,textFont,buttonFont))
        wipeButton = tk.Button(bankFrame, text="DB消滅", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: killDB(root,textFont,uiFont,killDBFont,buttonFont))
        mainMenuButton = tk.Button(bankFrame, text="開始", foreground="#ffffff", background="#640010", width=11, height = 1, font = buttonFont, command = lambda: updateScreen(0))
        widgets = [saveButton,loadButton,deleteButton,wipeButton,mainMenuButton]
        for item in widgets:
            item.pack(pady = 2)

#---------------------------------MainScreen-------------------------------------------------------------------------  
    def bankMenuWindow(buttonFrame,uiFont,textFont,buttonFont,root,killDBFont):
        def updateBank():
            bankFlag.config(text = flagValue[0], foreground = flagValue[1])
            bankFrame.after(1000, updateBank)
        def updateautoCheckModule():
            Update(listOfEntries)
            bankFrame.after(1000, updateautoCheckModule)
#---------------------------------ButtonFrame-----------------------------------------------
        bankFrame = tk.Frame(buttonFrame, bg="#001002")
        bankFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        bankFrame.grid_rowconfigure(0, weight=1)
        bankFrame.grid_rowconfigure(2, weight=1)
        bankFrame.grid_columnconfigure(0, weight=1)
        bankFrame.grid_columnconfigure(1, weight=1)
        dataBank = tk.Button(bankFrame, text="データベース", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: updateScreen(1))
        bankFlag = tk.Label(bankFrame, text = flagValue[0], font = textFont, foreground = flagValue[1], background="#001064",relief = "sunken")
        dataChecker = tk.Button(bankFrame, text="データ確認", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: scoutBot())
        clearButton = tk.Button(bankFrame, text="引き払う", foreground="#ffffff", background="#640010", width=11, height = 1, font = buttonFont, command = lambda: clearList())
        displayBank = tk.Button(bankFrame, text="ベース見せる", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: showDB(root,textFont,uiFont))
        entryHandler = tk.Button(bankFrame, text="数値累算器", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: updateScreen(2))
        widgets = [dataBank,bankFlag,dataChecker,clearButton,displayBank,entryHandler]
        posr = 0
        posc = 0
        posCounter = 0
        posFlag = False
        for item in widgets:
            item.grid(row = posr, column = posc, sticky="n", pady = 1, padx = 2)
            if posFlag == False:
                posc += 1
                posCounter += 1
                if posc == 2:
                    posc = 0
                    posr += 1
                    if posCounter == 4:
                        posFlag = True
            elif posFlag == True:
                posr += 1
        updateBank()
        updateautoCheckModule()
    def updateScreen(screenFlag):
        if screenFlag == 0:
            clearContainer(buttonFrame)
            bankMenuWindow(buttonFrame,uiFont,textFont,buttonFont,root,killDBFont)
        elif screenFlag == 1:
            clearContainer(buttonFrame)
            DBMenu(buttonFrame,uiFont,textFont,buttonFont,root)
        elif screenFlag == 2:
            clearContainer(buttonFrame)
            recieveInputMenu(buttonFrame,uiFont,textFont,buttonFont,root)
    updateScreen(0)