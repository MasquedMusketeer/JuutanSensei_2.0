import os
import importlib
import subprocess
import generalSmallFuncModule as GSFMod

list_of_modules = ["datetime","pyperclip","keyboard","getpixelcolor","mouse","tkinter","win10toast"]
pass_list = []
installscript = os.path.join(os.path.dirname(__file__), "scripts", "install_dependencies.bat")

def check_module(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

for x in list_of_modules:
    flag = check_module(x)
    pass_list.append(flag)
if False in pass_list:
    GSFMod.formating(5)
    GSFMod.formating(6)
    print("\u25BA Some dependencies were not found \u25C4")
    print("\u25BA Do you wish to install them? y/n \u25C4")
    GSFMod.formating(5)
    GSFMod.formating(6)
    usr_inpt = str(input("\u27a2  "))
    if usr_inpt == "y":
        GSFMod.formating(5)
        GSFMod.formating(6)
        print("\u25BA Installing required dependencies \u25C4")
        GSFMod.formating(5)
        GSFMod.formating(6)
        subprocess.call(installscript)


    else:
        print('\u25BA     Shutting Down...    \u25C4')