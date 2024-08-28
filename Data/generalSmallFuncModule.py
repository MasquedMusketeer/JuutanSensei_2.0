import time
import subprocess
import datetime as dt

def formating(x):
    if x == 1:
        return ""
    elif x == 2:
        return ("❀❀❀❀❀")
    elif x == 5:
        return (" ╔══════════════════════════════╗ ")
    elif x == 6:
        return (" ╚══════════════════════════════╝ ")
    elif x == 3:
        return ('>>    No available operation    <<')

def version():
    version = 'ver 2.0.7f'
                    # a - Alpha
                    # b - Beta
                    # f - Final
                    # x - Experimental
    return version

def printFunction(string):
    for y in string:
        print(y, end='', flush=True)
        time.sleep(0.003)
    print('\r')

def loadLink(lnk):
    subprocess.Popen(lnk, shell=True)

def bankKillScreen():
    print('     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀  ⠀  ⠀⠀⠀⠀⣠⣔⡿⠛⠒⠒⡕⢄⠀⠀⠀⠀⠀⠀')
    print('⠀⠀  ⠀  ⠀⣀⣴⣳⠃⠀⠀⠀⠀⠘⢎⡦⣄⠀⠀⠀⠀')
    print('⠀    ⠀⠀⣜⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣳⠀⠀⠀')
    print('⠀    ⠀⢸⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡆⠀⠀')
    print('⠀    ⠀⠘⡏⢀⢴⠶⣤⢄⢲⣲⠦⣦⣤⡤⡀⡇⠇⠀⠀')
    print('⠀    ⠀⠀⣧⠀⣾⢀⣸⡸⠘⢸⠀⣿⠀⣸⡏⣧⠀⠀⠀')
    print('⠀    ⠀⠀⢹⠀⣿⠿⡯⡀⢀⣼⢀⣿⠛⠉⠀⢻⠀⠀⠀')
    print('⠀    ⠀⠀⣿⠐⠛⠂⠘⠛⠒⠛⠊⠛⠂⠀⢸⢸⠀⠀⠀')
    print('⠀    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡼⠀⠀⠀')
    print('⠀    ⠀⠀⢻ ⠀Data Bank⢸⡆⠀⠀⠀')
    print('⠀⠀    ⢀⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡀⠀⠀')
    print('  ⠀  ⣠⠃⠘⠊⠉⠛⠛⠋⠩⠩⠭⠍⠛⠛⠛⠃⠐⡄⠀')
    print('    ⠀⣯⡉⠉⢉⡉⠉⠉⠉⠉⠉⠉⣉⣉⣉⣉⣉⣉⣹⠀')

def calendarDateColector(flag,ursMonth):
    month = dt.datetime.now().month
    year = dt.datetime.now().year
    today = dt.datetime.now().day
    if flag == True:
        date = dt.datetime(year, month, 1)
    else:
        date = dt.datetime(year, ursMonth, 1)
    weekday = date.isoweekday() + 1
    if flag == True:
        return month, year, weekday, today
    else:
        return ursMonth, year, weekday, today

def secretLogin():
    usr_input = input('\u27a2 ')
    if usr_input == "Afp04599":
        return True
    else:
        return False

def guestMessage(flag):
    if flag == False:
        string = "Unauthorized access to feature"
        return string


def mailStrings(selection):
    strings = [
        ['Bom dia a todos,','Boa tarde a todos,'],
        ['segue em anexo a solicitação;','segue em anexo o caixa do dia'],
        'obrigado.',
        ['123@abc.com.br','123@abc.com.br','123@abc.com.br'],
        ['123@abc.com.br','123@abc.com.br'],
        ['Caixa dia']
    ]
    if selection == 1:
        return strings[0][0]
    elif selection == 2:
        return strings[0][1]
    elif selection == 3:
        return strings[1][0]
    elif selection == 4:
        return strings[1][1]
    elif selection == 5:
        return strings[2]
    elif selection == 6: 
        return strings[3][0]
    elif selection == 7: 
        return strings[3][1]
    elif selection == 8: 
        return strings[3][2]
    elif selection == 9: 
        return strings[4][0]
    elif selection == 10:
        return strings[4][1]
    elif selection == 11:
        return strings[4][2]
    elif selection == 12:
        return strings[5][0]

#---------------Develop a letter descrambler-------------
#def simpleLetterScrambler(descrablePlz):

# ARROWS 
# '\u27a2  '  general input
# '\u25BA'L '\u25C4'R   return messages
# '\u27B9'    list pointers