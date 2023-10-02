import os
import sys
import time
import webbrowser
import vimerror5
import keyboard
#run vim.py now.
#pip install keyboard
def fist():
    os.system("cls")
    print("Help can read help.\nThis is vim 0.0.6.\nBy ancodeb.\nGithub:https://www.github.com/ancodeb.\nChina gov can type cg\ngithub can go to github.\n")
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
def li():
    while True:
        a = input(":")
        a = a.strip()

        if a == "help":
            with open('help.txt','r',encoding='utf-8')as file:
                filetext=file.read()
                print(filetext)
        elif a == "cg":
            print("china gov is china gov.\nit is https://www.gov.cn")
        elif a == "q":
            os.system("cls")
            sys.exit()
        elif a == "ql":
            os.system("cls")
        elif a == "creat":
            hello = True
            os.system("cls")
            ti = []
            while hello:
                if keyboard.is_pressed('i'):
                    text = input(':')
                    ti.append(text)
                    os.system("cls")
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
                    line=input('line:')
                    if line=='':
                        pass
                    line=int(line)
                    line=line-1
                    if line<0 or line>len(ti):
                        print(vimerror5.error[1])
                    else:
                        del ti[line]
                        os.system('cls')
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
        elif a == 'see':
            os.system('cls')
            filename=input(':')
            with open(filename,'r',encoding='utf-8')as c:
                co=c.read()
                print(co)



        else:
            print(vimerror5.error[0])

fist()
li()