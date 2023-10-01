import os
import sys
import time
import webbrowser

import keyboard
#run vim.py now.
#pip install keyboard
os.system("cls")
print("Help can read help.\nThis is vim 0.0.3.\nBy ancodeb.\nGithub:https://www.github.com/ancodeb.\nChina gov can type cg\ngithub can go to github")
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
while True:
    a=input(":")
    if a=="help":
        print("cg can find china gov.\nhelp can read help.\nq can quit vim.\nql can exit help.\ncreat is new file.\nqiuhuvim can close files.")
    elif a=="cg":
        print("china gov is china gov.\nit is https://www.gov.cn")
    elif a=="q":
        os.system("cls")
        sys.exit()
    elif a=="ql":
        os.system("cls")
    elif a=="creat":
        hello=True
        os.system("cls")
        ti=[]
        while hello:
            if keyboard.is_pressed('i'):
                text=input(':')
                ti.append(text)
                os.system("cls")
                for i in ti:
                    print(i)
            if keyboard.is_pressed('q'):
                break
            if keyboard.is_pressed('s'):
                name=input('name:')
                name=name+'.txt'
                with open(name,'a+',encoding='utf-8')as file:
                    for i in ti:
                        file.write(i)

    elif a=='happy':
        webbrowser.open('https://www.gov.cn/')
    elif a=='github':
        webbrowser.open('https://www.github.com/ancodeb')



    else:
        print("erro")
