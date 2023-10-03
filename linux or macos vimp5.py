import os
import sys
import time
import webbrowser
import vimerror5
import keyboard
#run vim.py now.
#pip install keyboard
def frist():
    os.system("clear")
    print("Help can read help.\nThis is vim 0.0.7.\nBy ancodeb.\nGithub:https://www.github.com/ancodeb.\nChina gov can type cg\ngithub can go to github.\n")
    print("happy china's day!")
    print("""
  _     _   _                   ____                                 _ _   _           _                             __                       _      _     
 | |   | | | |            _    / / /                                (_) | | |         | |                           / /                      | |    | |    
 | |__ | |_| |_ _ __  ___(_)  / / /_      ____      ____      ____ _ _| |_| |__  _   _| |__   ___ ___  _ __ ___    / /_ _ _ __   ___ ___   __| | ___| |__  
 | '_ \| __| __| '_ \/ __|   / / /\ \ /\ / /\ \ /\ / /\ \ /\ / / _` | | __| '_ \| | | | '_ \ / __/ _ \| '_ ` _ \  / / _` | '_ \ / __/ _ \ / _` |/ _ \ '_ \ 
 | | | | |_| |_| |_) \__ \_ / / /  \ V  V /  \ V  V /  \ V  V / (_| | | |_| | | | |_| | |_) | (_| (_) | | | | | |/ / (_| | | | | (_| (_) | (_| |  __/ |_) |
 |_| |_|\__|\__| .__/|___(_)_/_/    \_/\_/    \_/\_/    \_/\_(_)__, |_|\__|_| |_|\__,_|_.__(_)___\___/|_| |_| |_/_/ \__,_|_| |_|\___\___/ \__,_|\___|_.__/ 
               | |                                              __/ |                                                                                      
               |_|                                             |___/                                                                                       
    """)
    print(time.asctime())
def save(textlist,filename,line):
    del textlist[line]
    os.system('clear')
    number = 1
    with open(filename, 'w+', encoding='utf-8') as file:
        for i in textlist:
            file.write(i)
            print(str(number) + '    ' + i)
            number = int(number)
            number += 1
frist()
while True:

    a = input(":")
    a = a.strip()

    if a == "help":
        with open('help.txt', 'r', encoding='utf-8') as file:
            filetext = file.read()
            print(filetext)
    elif a == "cg":
        print("china gov is china gov.\nit is https://www.gov.cn")
    elif a == "q":
        os.system("clear")
        sys.exit()
    elif a == "ql":
        os.system("clear")
    elif a == "creat":
        hello = True
        os.system("cls")
        ti = []
        while hello:
            if keyboard.is_pressed('i'):
                text = input(':')
                ti.append(text)
                os.system("clear")
                number = 1
                for i in ti:
                    print(str(number) + '    ' + i)
                    number = int(number)
                    number += 1
            if keyboard.is_pressed('q'):
                break
            if keyboard.is_pressed('s'):
                name = input('name:')
                Suffixname = input('Suffix name:')
                name = name + Suffixname
                with open(name, 'a+', encoding='utf-8') as file:
                    for i in ti:
                        file.write(i + '\n')
            if keyboard.is_pressed('d'):
                line = input('line:')
                if line == '':
                    pass
                line = int(line)
                line = line - 1
                if line < 0 or line > len(ti):
                    print(vimerror5.error[1]+'\n'+vimerror5.errors[1])
                else:
                    del ti[line]
                    os.system('clear')
                    number = 1
                    for i in ti:
                        print(str(number) + '    ' + i)
                        number = int(number)
                        number += 1

    elif a == 'happy':
        webbrowser.open('https://www.gov.cn/')
    elif a == 'github':
        webbrowser.open('https://www.github.com/ancodeb')
    elif a == '':
        pass

    elif a == 'write':
        os.system('clear')
        filename = input('filename:')
        with open(filename, 'r+', encoding='utf-8') as c:
            texts = c.readlines()
            textlist = []
        for text in texts:
            textlist.append(text)
            number = 1
        for i in textlist:
            print(str(number) + '    ' + i)
            number = int(number)
            number += 1
        while True:
            if keyboard.is_pressed('d'):
                line = input('line:')
                if line == '':
                    pass
                line = int(line)
                line = line - 1
                if line < 0 or line > len(textlist):
                    print(vimerror5.error[1]+'\n'+vimerror5.errors[1])
                else:
                    save(textlist,filename,line)

            if keyboard.is_pressed('i'):
                text = input(':')
                textlist.append(text)
                os.system("clear")
                number = 1
                for i in textlist:
                    print(str(number) + '    ' + i)
                    number = int(number)
                    number += 1

            if keyboard.is_pressed('q'):
                print('Is it saved? If it is not saved, you can enter "s", and if saved, please enter "q".')
                text=input(':')
                if text=='s':
                    save(textlist,filename,line)
                else:
                    break





    else:
        print(vimerror5.error[0]+'\n'+f'no found command "{a}"')
        time.sleep(0.5)
        frist()

