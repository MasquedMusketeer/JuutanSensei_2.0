import tkinter as tk
import Data.autoLoginModule as al
from Data.lnkBank import linkBank as lB
import Data.InterfaceTextModule as GUIText
import Data.generalSmallFuncModule as GSFMod

comp, caixa, dem, log, NoFi, vale = lB.linkBank()

#---------------------------------FolderScreen-------------------------------------------------------------------------  
def foldersWindow(container,uiFont,textFont,buttonFont,root):
#--------------------------------TextFrame------------------------------------------------
    textFrame = tk.Frame(container, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    contentCounter = 0
    for string in GUIText.mainMenuInterface():
        contentCounter += 1
        if contentCounter == 1 or contentCounter == 2:
            line = tk.Label(textFrame, text = string, font = uiFont, foreground="#00ff64", background="#001002")
            line.pack()
    for string in GUIText.folderMenuInterface():
        line = tk.Label(textFrame, text = string , font = textFont, foreground="#00ff64", background="#001002")
        line.pack()
#---------------------------------ButtonFrame-----------------------------------------------
    mailFrame = tk.Frame(container, bg="#001002")
    mailFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
    mailFrame.grid_rowconfigure(0, weight=1)
    mailFrame.grid_rowconfigure(3, weight=1)
    mailFrame.grid_columnconfigure(0, weight=1)
    mailFrame.grid_columnconfigure(2, weight=1)
    compButton = tk.Button(mailFrame, text="共有", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: GSFMod.loadLink(comp))
    NoFiButton = tk.Button(mailFrame, text="請求書", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: GSFMod.loadLink(NoFi))
    demButton = tk.Button(mailFrame, text="実演", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: GSFMod.loadLink(dem))
    valeButton = tk.Button(mailFrame, text="レンタル券", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: GSFMod.loadLink(vale))
    logButton = tk.Button(mailFrame, text="物流", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: GSFMod.loadLink(log))
    caixaButton = tk.Button(mailFrame, text="レジ", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: GSFMod.loadLink(caixa))
    buttons = [compButton,NoFiButton,demButton,valeButton,logButton,caixaButton]
    posr = 0
    posc = 0
    posCounter = 0
    for button in buttons:
        posCounter += 1
        button.grid(row = posr, column = posc, sticky="n", pady = 6, padx = 2)
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
#---------------------------------------------------------------------------------------------
#----------------------------------------LoginScreen------------------------------------------    
loginCredList = [
    'USER >> 123@abc.com.br','PASSWORD >> abc123',
    'USER >> 123@abc.com.br','PASSWORD >> abc123'
]

def loginPopup(root,flag,textFont):
    popup = tk.Toplevel(root, bg="#001002")
    popup.title("ログイン認証情報")
    popup.geometry("300x70")
    textFrame = tk.Frame(popup, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    stringLineCounter = 0
    if flag == 'SU':
        for string in loginCredList:
            stringLineCounter += 1
            if stringLineCounter == 1 or stringLineCounter == 2:
                line = tk.Label(textFrame, text = string, font = textFont, foreground="#00ff64", background="#001002")
                line.pack()
    elif flag == "CRM":
        for string in loginCredList:
            stringLineCounter += 1
            if stringLineCounter == 3 or stringLineCounter == 4:
                line = tk.Label(textFrame, text = string, font = textFont, foreground="#00ff64", background="#001002")
                line.pack()
#--------------------------------TextFrame------------------------------------------------
def userLoginWindow(container,uiFont,textFont,buttonFont,root):
    textFrame = tk.Frame(container, pady=10, bg="#001002")
    textFrame.pack(side=tk.TOP, fill=tk.BOTH)
    contentCounter = 0
    for string in GUIText.mainMenuInterface():
        contentCounter += 1
        if contentCounter == 1 or contentCounter == 2:
            line = tk.Label(textFrame, text = string, font = uiFont, foreground="#00ff64", background="#001002")
            line.pack()
    for string in GUIText.loginMenuInterface():
        line = tk.Label(textFrame, text = string , font = textFont, foreground="#00ff64", background="#001002")
        line.pack()
#---------------------------------ButtonFrame-----------------------------------------------
    mailFrame = tk.Frame(container, bg="#001002")
    mailFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
    blButton = tk.Button(mailFrame, text="BL ログイン", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: al.BLlogin())
    siteButton = tk.Button(mailFrame, text="サイトの店長", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: loginPopup(root,"SU",textFont))
    crmButton = tk.Button(mailFrame, text="CRM ログイン", foreground="#00ff64", background="#001002", width=11, height = 1, font = buttonFont, command = lambda: loginPopup(root,"CRM",textFont))
    buttons = [blButton,siteButton,crmButton]
    for button in buttons:
        button.pack(pady = 5.5)