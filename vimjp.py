import os
import sys
import time
import webbrowser

import keyboard
#run vim.py now.
#pip install keyboard
os.system("cls")
print("Help ヘルプを表示できます.\nThis is vim 0.0.4.\n著者はancodeb.\nGithub:https://www.github.com/ancodeb.\nChina gov can type cg\ngithub can go to github")
print("happy 中国建国記念日!")
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
    a=a.strip()

    if a=="help":
        print('"cg" あなたは中国政府のウェブサイトに行くことができます.\n"help" ヘルプを表示できます.\n"q"vimを終了できます.\n"ql" 画面をクリアする.\n"creat" 新しいファイルを作成する.\n"github" あなたは行くことができます GitHub')
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
                number=1
                for i in ti:

                    print(str(number)+'    '+i)
                    number=int(number)
                    number+=1
            if keyboard.is_pressed('q'):
                break
            if keyboard.is_pressed('s'):
                name=input('name:')
                Suffixname=input('Suffix name:')
                name=name+Suffixname
                with open(name,'a+',encoding='utf-8')as file:
                    for i in ti:
                        file.write(i+'\n')

    elif a=='happy':
        webbrowser.open('https://www.gov.cn/')
    elif a=='github':
        webbrowser.open('https://www.github.com/ancodeb')
    elif a=='':
        pass



    else:
        print("erro")
