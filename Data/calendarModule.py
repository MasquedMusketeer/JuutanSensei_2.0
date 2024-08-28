# type: ignore
import Data.generalSmallFuncModule as GSFMod
import tkinter as tk

month, year, weekday, today = GSFMod.calendarDateColector(True, "null")
calendar = ""

def calendarFull(data,flag):
    x, y, z, td = data
    if z <= 6:
        weekday = z
    elif z >= 7:
        weekday = z - 7
    year = y
    month1 = []
    spaces = [' ','  ']
    monthList = ['01','02','03','04','05','06','07','08','09','10','11','12']
    yearBigFeb = [2024,2028,2032,2036,2040]
    weektracker = ['日','月','火','水','木','金','士']
    monthDays28 = [2]
    monthDays29 = [2]
    monthDays30 = [4,6,9,11]
    monthDays31 = [1,3,5,7,8,10,12]
    startMonth = [x,weektracker[weekday-1]]
    infoBuffer = []
    month = monthList[startMonth[0]-1]

    def gapInput(x,y):
        counterBef = x
        counterAft = y
        while counterBef > 0:
            month1.append(spaces[1])
            counterBef -= 1
        while counterAft > 0:
            month1.append(spaces[1])
            counterAft -= 1
        
    def dayDet(wd):
        gapCalculator = wd
        gapNum = 0
        if gapCalculator == '日':
            gapNum = 0
        elif gapCalculator == '月':
            gapNum = 1
        elif gapCalculator == '火':
            gapNum = 2
        elif gapCalculator == '水':
            gapNum = 3
        elif gapCalculator == '木':
            gapNum = 4
        elif gapCalculator == '金':
            gapNum = 5
        elif gapCalculator == '士':
            gapNum = 6
        infoBuffer.append(gapNum)

    def dayListInput(x):
        lastDayToCalculate = x
        if lastDayToCalculate in monthDays31:
            for x in range(1,32):
                if x < 10:
                    month1.append("0"+str(x))
                else:
                    month1.append(str(x))
            infoBuffer.append(11)
        elif lastDayToCalculate in monthDays30:
            for x in range(1,31):
                if x < 10:
                    month1.append("0"+str(x))
                else:
                    month1.append(str(x))
            infoBuffer.append(12)
        elif lastDayToCalculate in monthDays29 and year in yearBigFeb:
            for x in range(1,30):
                if x < 10:
                    month1.append("0"+str(x))
                else:
                    month1.append(str(x))
            infoBuffer.append(13)
        elif lastDayToCalculate in monthDays28 and year not in yearBigFeb:
            for x in range(1,29):
                if x < 10:
                    month1.append("0"+str(x))
                else:
                    month1.append(str(x))
            infoBuffer.append(14)

    dayDet(startMonth[1])
    gapInput(infoBuffer[0],0)
    dayListInput(startMonth[0])
    gapInput(0,infoBuffer[-1])


    def printCalendar():
        global calendar
        global header
        header = GSFMod.formating(2) + str(year)+" "+str(month) + GSFMod.formating(2)
        calendar = [
        '日','月','火','水','木','金','士',
        month1[0],month1[1],month1[2],month1[3],month1[4],month1[5],month1[6],
        month1[7],month1[8],month1[9],month1[10],month1[11],month1[12],month1[13],
        month1[14],month1[15],month1[16],month1[17],month1[18],month1[19],month1[20],
        month1[21],month1[22],month1[23],month1[24],month1[25],month1[26],month1[27],
        month1[28],month1[29],month1[30],month1[31],month1[32],month1[33],month1[34],
        month1[35],month1[36],month1[37],month1[38],month1[39],month1[40],month1[41],
        ]
    printCalendar()
    if flag == "h":
        return header
    elif flag == 'b':
        return calendar

def popUpGeneration(root,title,sizex,sizey,textFont,buttonFont,uiFont):
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
    textLable = tk.Label(topFrame, text = "確認する月:", font = textFont, foreground="#00ff64", background="#001002")
    monthBox = tk.Entry(topFrame, font = textFont, width = 10, foreground="#00ff64", background="#006410")
    checkButton = tk.Button(topFrame, text="チェック", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: calCheckFunction())
    topFrameWidget = [textLable,monthBox,checkButton]
    posc = 0
    for widget in topFrameWidget:
        widget.grid(row = 0, column = posc, sticky="n", pady = 6, padx = 2)
        posc += 1
    def calCheckFunction():
        for widget in bottomFrame.winfo_children():
            widget.destroy()
        usrInput = int(monthBox.get())
        colorCounter = 0
        posc = 0
        posr = 0
        upperFrame = tk.Frame(bottomFrame, padx=10, bg="#001002",  width = 315, height = 20)
        upperFrame.pack(side=tk.TOP, fill=tk.BOTH)
        lowerFrame = tk.Frame(bottomFrame, padx=32, bg="#001002",  width = 315,)
        lowerFrame.pack(side=tk.TOP, fill=tk.BOTH)
        for x in range(0,7):
            lowerFrame.grid_columnconfigure(x, weight = 1)
        header =  calendarFull(GSFMod.calendarDateColector(False, usrInput), "h")
        label = tk.Label(upperFrame, text= header, font = textFont, foreground="#ff0010", background="#001032",relief = "sunken")
        label.pack()
        for item in calendarFull(GSFMod.calendarDateColector(False, usrInput), "b"):
            if colorCounter < 7:
                spot = tk.Label(lowerFrame, text= (item), font = textFont, foreground="#ff0010", background="#001032",relief = "sunken")
                spot.grid(row = posr, column = posc, sticky="nsew")
            elif colorCounter >= 7:
                spot = tk.Label(lowerFrame, text= (item), font = textFont, foreground="#00ff64", background="#001002",relief = "sunken")
                spot.grid(row = posr, column = posc, sticky="nsew")
            posc += 1
            if posc == 7:
                posc = 0
                posr += 1
            colorCounter += 1