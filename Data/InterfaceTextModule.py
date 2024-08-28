import Data.generalSmallFuncModule as GSFMod

def iniInterface(selection):
    listOfCharacters1 = '╔══════════════════════════════╗'
    listOfCharacters2 = '絨毯先生 '+ GSFMod.version()
    listOfCharacters3 = 'Mendoukusai ByteLabs'
    listOfCharacters4 = '© 2024 All rights reserved'
    listOfCharacters5 = '╚══════════════════════════════╝'
    listOfCharacters6 = '           ⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
    listOfCharacters7 = ' ⢀⣤⣤⣤⣤⣀⣀⣤⣶⣿⣿⣿⡿⡋⠅⠈⠉⠒⠢⢀⡤⠤⠤⠤⢤⣀⠀⠀'
    listOfCharacters8 = ' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢎⠁⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀'
    listOfCharacters9 = ' ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⣀⣁⠀⠀⢀⣀⠀⠀⠀⢳⡀⠠⡇⠀⠀'
    listOfCharacters10= ' ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠧⢥⣀⠀⠀⠉⠲⢤⣳⣸⠁⠀⠀'
    listOfCharacters11= ' ⢹⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠀⠀⠀⢸⣿⣿⠹⣶⣤⡀⠈⡇⠀⡰⠆'
    listOfCharacters12= ' ⢸⣿⣿⣿⣿⣿⡟⠁⠀⠀⠂⠄⠀⠀⡀⡩⡿⠒⣿⣿⣿⣦⣿⠀⠆⢛'
    listOfCharacters13= ' ⢸⣿⣿⣿⣿⡟⠀⣠⡤⠤⣄⣀⠀⠀⡏⡼⢁⣀⣹⡇⣿⣿⡟⠀⠙⠉'
    listOfCharacters14= ' ⣾⣿⣿⣿⣹⠁⢻⠁⢰⡞⣶⠙⠀⣰⠞⠁⢿⢿⡿⠙⣿⣿⡇⠀⠀⠀'
    listOfCharacters15= ' ⣿⣿⠫⢈⢹⠀⠀⡑⡤⠑⠊⠀⠀⠀⠀⠀⠸⠙⠁⠈⣿⡟⢱⠀⠀⠀'
    listOfCharacters16= ' ⢿⣿⡀⠢⢆⢡⠀⠀⠁⠑⠑⠀⠀⠀⠘⠀⠀⠱⢀⠁⣿⡇⢸⠀⠀⠀'
    listOfCharacters17= ' ⣸⣿⣿⣶⣤⣬⠁⠀⠀⠀⠀⢄⣀⠤⢄⡠⠂⠀⠀⢰⣿⡇⢸⡄⠀⠀'
    listOfCharacters18= ' ⢀⣿⢿⣿⣿⣿⡇⠑⢄⡀⠀⠀⠈⡄⠀⠠⠁⠀⢀⣴⡛⢹⣡⣸⡇⠀⠀'
    listOfCharacters19= ' ⣼⡷⠚⠛⠴⢏⣓⡠⠄⣙⡶⣄⡀⠈⠀⠁⣀⣴⣿⣿⠇⢸⣿⣿⡇⠀⠀'
    listOfCharacters20= ' ⣰⣿⢉⣧⠀⠀⠀⠀⠀⠈⠁⠪⡫⡙⢅⠒⣺⡿⠿⠏⠹⠂⣾⣿⣿⡇⠀⠀'
    listOfCharacters21= ' ⣿⣿⡾⠋⠑⢦⣀⠀⠀⠀⠀⠀⠘⠔⢌⢔⡵⠃⠀⠀⣀⣤⢏⣿⡟⡇⠀⠀'

    logo = [listOfCharacters1,listOfCharacters2,
            listOfCharacters3,listOfCharacters4,
            listOfCharacters5]

    listOfCharacters = [listOfCharacters6,listOfCharacters7,listOfCharacters8,
                        listOfCharacters9,listOfCharacters10,listOfCharacters11,listOfCharacters12,
                        listOfCharacters13,listOfCharacters14,listOfCharacters15,listOfCharacters16,
                        listOfCharacters17,listOfCharacters18,listOfCharacters19,listOfCharacters20,
                        listOfCharacters21]
    phrase = ["",
            "あなたが望む未来は",
            "あなたの手の届くところにあります。",
            "あきらめないでください!"]
    if selection == 0:
        return listOfCharacters
    if selection == 1:
        return phrase
    if selection == 2:
        return logo
    
def mainMenuInterface():
    upperStringsContent = [(GSFMod.formating(5)),(GSFMod.formating(6)),("        絨毯先生 "+ GSFMod.version()) + "      ",
                       " 絨毯先生にようこそ!",'  選択肢はこちら:',""]
    return upperStringsContent
def loginMenuInterface():
    upperStringsContent = ["ハッカー先生です!!",'選択肢はこちら:']
    return upperStringsContent
def folderMenuInterface():
    upperStringsContent = ["フォルダー係です!!",'選択肢はこちら:']
    return upperStringsContent
def dbMenuInterface():
    upperStringsContent = ["図書館員です!!",'選択肢はこちら:']
    return upperStringsContent

def deathDBInterface():
    stringList = [
        '███████▀▀▀░░░░░░░▀▀▀███████',
        '████▀░░░░░░░░░░░░░░░░░▀████',
        '███│░░░░░░░░░░░░░░░░░░░│███',
        '██▌│░░░░░░░░░░░░░░░░░░░│▐██',
        '██░└┐░░░░░░░░░░░░░░░░░┌┘░██',
        '██░░└┐░░░░░░░░░░░░░░░┌┘░░██',
        '██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██',
        '██▌░│██████▌░░░▐██████│░▐██',
        '███░│▐███▀▀░░▄░░▀▀███▌│░███',
        '██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██',
        '██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██',
        '████▄─┘██▌░░░░░░░▐██└─▄████',
        '█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████',
        '████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████',
        '█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████',
        '███████▄░░░░░░░░░░░▄███████',
        '██████████▄▄▄▄▄▄▄██████████',
        ]
    return stringList