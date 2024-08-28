import tkinter as tk
from tkinter import messagebox
import Data.generalSmallFuncModule as GSFMod

lineOfOP = []
currentOPBuffer = []
currentOPFlag = ""
lastResultBuffer = 0
operations = ["+","-","*","/"]

def singleOP():
    global lastResultBuffer
    lastResultBuffer = 0
    op = lineOfOP.pop(0)
    operation = op.pop(0)
    result = 0
    if operation == '+':
        for x in op:
            result += x
    elif operation == '-':
        result = op.pop(0)
        for x in op:
            result -= x
    elif operation == '*':
        result = op.pop(0)
        for x in op:
            result = result * x
    elif operation == '/':
        result = op.pop(0)
        for x in op:
            result = result/x
    lastResultBuffer += result
    return (operation + " "+ str(result))

#--------------------------PopupGenerator----------------------------------------------------------
def popupLineCalcWindow(root,title,sizex,sizey,textFont,buttonFont):
    def opDefinition(flag):
        global currentOPFlag
        currentOPFlag = flag
        if not currentOPBuffer or currentOPBuffer[0] not in operations:
            currentOPBuffer.insert(0,currentOPFlag)
        elif currentOPBuffer[0] in operations:
            currentOPBuffer.pop(0)
            currentOPBuffer.insert(0,currentOPFlag)
        for button in opButtons:
            button.config(foreground="#00ff64", background="#001002")
        if flag == operations[0]:
            add.config(foreground="#ffffff", background="#640010")
        elif flag == operations[1]:
            sub.config(foreground="#ffffff", background="#640010")
        elif flag == operations[2]:
            mult.config(foreground="#ffffff", background="#640010")
        elif flag == operations[3]:
            div.config(foreground="#ffffff", background="#640010")

    def loadOpeation():
        if currentOPBuffer[0] not in operations:
            messagebox.showerror("Error", "操作欠落")
        else:
            buffer = []
            for x in currentOPBuffer:
                buffer.append(x)
            lineOfOP.append(buffer)
            currentOPBuffer.clear()
            currentOPBuffer.append(currentOPFlag)
            listOfOperands.delete(0, tk.END)
            opLabel.config(text = "業務が一直線\nに並ぶ:" + " " + str(len(lineOfOP)))

    def loadValue(numValue):
        global lastResultBuffer
        if numValue.get() == "" and lastResultBuffer == 0:
            messagebox.showerror("Error", "値を挿入しない")
        else:
            if lastResultBuffer != 0 and numValue == "":
                value = float(lastResultBuffer)
                listOfOperands.insert(0, value)
                currentOPBuffer.append(value)
                lastResultBuffer = 0
            else:
                value = float(numValue.get())
                listOfOperands.insert(0, value)
                currentOPBuffer.append(value)
                numValue.delete(0, tk.END)
    
    def operationStepper(flag):
        if lineOfOP:
            if flag == False:
                result = singleOP()
                listOfResults.insert(0, result)
                opLabel.config(text = "業務が一直線\nに並ぶ:" + " " + str(len(lineOfOP)))
            elif flag == True:
                counter = len(lineOfOP)
                while counter > 0:
                    result = singleOP()
                    listOfResults.insert(0, result)
                    counter -= 1
                opLabel.config(text = "業務が一直線\nに並ぶ:" + " " + str(len(lineOfOP)))
        else:
            messagebox.showerror("Error", "ライン上では何もしない")




    popup = tk.Toplevel(root, bg="#001002")
    popup.title(title)
    popup.geometry(f"{sizex}x{sizey}")
    mainFrame = tk.Frame(popup, pady=10, bg="#001002")
    mainFrame.pack(side=tk.TOP, fill=tk.BOTH)
#---------------------------TopFrame--------------------------------------------
    topFrame = tk.Frame(mainFrame, bg="#001002")
    topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for x in range (0,4):
        topFrame.grid_columnconfigure(x, weight = 1)

#---------------------------BottomFrame-----------------------------------------
    bottomFrame = tk.Frame(mainFrame, bg="#001002")
    bottomFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    bottomFrame.grid_columnconfigure(0, weight = 1)
    bottomFrame.grid_columnconfigure(1, weight = 1)

    bottomFrame1 = tk.Frame(bottomFrame, bg="#001002")
    bottomFrame2 = tk.Frame(bottomFrame, bg="#001002")
    bottomFrame = [bottomFrame1,bottomFrame2]
    posc = 0
    for Frame in bottomFrame:
        Frame.grid(row = 0, column = posc, sticky="n")
        posc += 1
#-------------------------------------------------------------------------------
    add = tk.Button(topFrame, text="足算", foreground="#00ff64", background="#001002", width = 4, height = 1, font = buttonFont, command = lambda: opDefinition("+"))
    sub = tk.Button(topFrame, text="減算", foreground="#00ff64", background="#001002", width = 4, height = 1, font = buttonFont, command = lambda: opDefinition("-"))
    mult = tk.Button(topFrame, text="乗算", foreground="#00ff64", background="#001002", width = 4, height = 1, font = buttonFont, command = lambda: opDefinition("*"))
    div = tk.Button(topFrame, text="割算", foreground="#00ff64", background="#001002", width = 4, height = 1, font = buttonFont, command = lambda: opDefinition("/"))
    opButtons = [add,sub,mult,div]
    posc = 0
    for button in opButtons:
        button.grid(row = 0, column = posc, sticky="n", pady = 3)
        posc += 1
#-------------------------------------------------------------------------------
    listOfOperands = tk.Listbox(bottomFrame1, font = buttonFont, foreground="#00ff64", background="#001002", height=5, width=10)
    listOfResults = tk.Listbox(bottomFrame1, font = buttonFont, foreground="#00ff64", background="#001002", height=5, width=10)
    boxes = [listOfOperands,listOfResults]
    posr = 0
    for box in boxes:
        box.grid(row = posr, column = 0, sticky="w")
        posr += 1
#------------------------------------------------------------------------------
    bottomFrame2.grid_columnconfigure(0, weight=1)
    bottomFrame2.grid_columnconfigure(1, weight=1)
    numEntry = tk.Entry(bottomFrame2, font = textFont, width = 10, foreground="#00ff64", background="#006410")
    loadButton = tk.Button(bottomFrame2, text="数字", font = buttonFont, height = 1, foreground="#00ff64", background="#001002", command=lambda: loadValue(numEntry))
    singleOPButtom = tk.Button(bottomFrame2, text="単独運転", font = buttonFont, height = 1, foreground="#00ff64", background="#001002", command=lambda: operationStepper(False))
    fullOPButton = tk.Button(bottomFrame2, text="全部運転", font = buttonFont, height = 1, foreground="#00ff64", background="#001002", command=lambda: operationStepper(True))
    loadOpButton = tk.Button(bottomFrame2, text="ロード", font = buttonFont, height = 1, foreground="#00ff64", background="#001002", command=lambda: loadOpeation())
    opLabel = tk.Label(bottomFrame2, text = "業務が一直線\nに並ぶ:" + " " + str(len(lineOfOP)), font = buttonFont, foreground="#00ff64", background="#001002",pady = 5)
    upperFrame = [numEntry,loadButton,loadOpButton,singleOPButtom,fullOPButton,opLabel]
    for widget in upperFrame:
        widget.pack()
#------------------------------------------------------------------------------