import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import Data.InterfaceTextModule as GUIText

mainLoginFlag = False

def openLoginWindow(mainFrame,textFont,callBack,argument):
    global loginWindow, entry_username, entry_password
    loginWindow = tk.Toplevel(mainFrame)
    loginWindow.title("Login")
    loginFrame = tk.Frame(loginWindow, padx=10, pady=10, bg="#001002")
    loginFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Username
    label_username = tk.Label(loginFrame, text="ユーザー名:" , font = textFont, foreground="#00ff64", background="#001002")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(loginFrame, foreground="#00ff64", background="#001002")
    entry_username.grid(row=0, column=1)

    # Password
    label_password = tk.Label(loginFrame, text="パスワード:" , font = textFont, foreground="#00ff64", background="#001002")
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(loginFrame, show="*", foreground="#00ff64", background="#001002")
    entry_password.grid(row=1, column=1)

    # Login Button
    button_login = tk.Button(loginFrame, text="ログイン", font = textFont, command =  lambda : login(callBack,argument), foreground="#00ff64", background="#001002")
    button_login.grid(row = 2, column = 1, pady = 8)

    rootStyle = ttk.Style()
    rootStyle.configure("Term.Body", background="#001002")
    rootStyle.configure("Term.Font", foreground="#00ff64", background="#001002")
def login(callBack,argument):
    global entry_username, entry_password, mainLoginFlag
    username = entry_username.get()
    password = entry_password.get()
    if username == "adm" and password == "password":
        mainLoginFlag = True
    else:
        messagebox.showerror("Login", "Invalid username or password")
    if mainLoginFlag == True:
        loginWindow.destroy()
        callBack(argument)

def loginProcedure(mainFrame,callBack,argument):
    logoScreen1 = GUIText.iniInterface(2)
    logoScreen2 = GUIText.iniInterface(0)
    logoScreen3 = GUIText.iniInterface(1)

    uiFont = Font(size = 10, weight = "bold")
    textFont = Font(family = "Mincho", size = 12)
    imageFont = Font(family = "Mincho", size = 7)
    screenTimings = [1,2,3]
    screenTimer = 0

    #---------------------------------Upper Screen--------------------------
    logoFrame = tk.Frame(mainFrame, padx=10, pady=10, bg="#001002")
    logoFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    for x in logoScreen1:
        if screenTimer in screenTimings:
            label = tk.Label(logoFrame, text= x, font = textFont, foreground="#00ff64", background="#001002")
            label.pack()
        else:
            label = tk.Label(logoFrame, text= x, font = uiFont, foreground="#00ff64", background="#001002")
            label.pack()
        screenTimer += 1
    for x in logoScreen2:
        label = tk.Label(logoFrame, text= x, font = imageFont, foreground="#00ff64", background="#001002")
        label.pack()
    for x in logoScreen3:
        label = tk.Label(logoFrame, text= x, font = textFont, foreground="#00ff64", background="#001002")
        label.pack()

    login_button = tk.Button(logoFrame, text="ログイン", command = lambda: openLoginWindow(mainFrame,textFont,callBack,argument), foreground="#00ff64", background="#001002")
    login_button.pack(pady=20)
