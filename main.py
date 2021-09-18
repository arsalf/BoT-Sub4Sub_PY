import sys
from time import sleep
import pyautogui
import os

NORMALCOLOR = "\33[00m"
INFOCOLOR = "\033[1;33m"
REDCOLOR = "\033[1;31m"
GREENCOLOR = "\033[1;32m"
WHITECOLOR = "\033[1;37m"
DETECTCOLOR = "\033[1;34m"
BANNERCOLOR ="\033[1;33;40m"
ENDBANNERCOLOR="\33[00m"
VIOLETCOLOR = '\33[1;35m'
PASSCOLOR = False

def judul():
    print(VIOLETCOLOR+"""                                                   
                  @(@&(&%@#&#@%@&##&%@#%&&&&&&&&&#  
        ,.        ***@&&&&&&&&/(&&&/@&&&&&&&&&&&@&#  
        #*%#      &@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#  
       @@&#%#(/   *&@@@@@@@@@@@@@@@&#&#@@@@@@@@.&(((##  
%%%%%%%%%*#&(*&&#. (%%%%%%%%%%%%&@@&&&#%%%%%%&@.@&&&&#  
 *%@@@@@@@@@&&&&&&&((           ,%@&&&#      ,% @&&&&#
  ./%@@@@@@@@&@&@&*@&(         ,%@&&&#      ,%#(&&&&&
     ,(&@@#. @,&(@.*. * .%%#%%%%%%@/(#%%%%#%%%&&&&&&
      ,#@@@&&&&&@&&&&&&&&&#@#&@@#&&&&&#&&/@%&/&&%(/    
      ,#@@@&&&&#&@@@@@ @@&&&((@&#.(*&%@@@@@@@@@@#,       
      ,#@@%(&&%#.(&@@@ @@(&@&&&@ ,(/#%&@@@@@@@/.         
      ,#@@@&&%&# *&@@@ @&&&@&&&&&&@@&%         
      ,#@@@&&&&# *&@@@ @@#/* @@&&&&&&#              
      ,#@@,,,,,, *&@@@ @&&#,@@@@@@,,,,         
      ,#@@@@%@#  *&@@@ @##( ,(&@@@#, @         
      .*(#####/  *&@@@ @&@%   ,(#/.
                 *&@@@@@@@%*                        
                  *%@@@@@%*""" + GREENCOLOR + " <---Programming Nusantara--->" + NORMALCOLOR)
    print("==============================================")
    print("      PROGRAM BOT SUB4SUB WATCHING VIDEOS")
    print("==============================================")
    print("1. Only watching")
    print("2. With subscribe")
    print("0. Exit")

def click(source, message="default", confidence=0.78, click=2, interval=1):
    btn = pyautogui.locateCenterOnScreen(source, confidence=confidence)
    temp = btn
    if temp is not None:
        sleep(1)
        pyautogui.moveTo(btn)
        pyautogui.click(btn, clicks=click, interval=interval)
        print("Click "+message)
    else:
        print("Ga ada "+message)

    return temp

def clickBack():
    btn = click("src/back_btn.png", "Back", interval=0.5)
    sleep(2)
    return btn

def clickSkip():
    btn = click("src/skip_btn.png", "Skip") 
    return btn

def watching(seconds=65):
    print("Sedang menonton. . .")
    sleep(seconds)

def clickGoto():
    sleep(3)
    btn = click("src/goto_btn.png", "goto", click=3, interval=2)
    if btn is not None:
        sleep(3)
        clickNotice()

    return btn

def clickDekat():
    btn = click("src/dekat_btn.png", "dekat")
    sleep(2)
    clickRate()
    return btn

def clickNotice():
    click("src/notice_btn.png", "Notif")

def clickHide():
    click("src/hide_btn.png", "hide")

def clickRate():
    rate = click("src/rate_btn.png", "rate")
    if rate is not None:
        clickHide() 

def clickIklan():
    for i in range(1, 11):
        click("src/iklan"+str(i)+"_btn.png", "iklan" + str(i), click=1, confidence=0.75)

def clickBaik():
    baik = click("src/baik_btn.png", "Baik")
    return baik

def clickSubscribe():
    subs = click("src/subs_btn.png", "Subscribe", confidence=0.7)
    return subs

def onlyView():
    jumlah = int(input("Jumlah menonton : "))
    i = 0
    to = 0
    maxTo = 8
    os.system("cls")
    while i < jumlah and to < maxTo:
        print("Percobaan ke :", i+1)
        goto = clickGoto()
        sleep(3)
        if goto is None:
            clickSkip()
            clickBaik()
            clickIklan()
            to += 1
        else:
            watching()
            back = clickBack()
            sleep(3)
            dekat = clickDekat()
            clickBaik()
            if dekat is None:
                sleep(10)
                clickIklan()
                clickSkip()
            
            if back is not None:
                to = 0
                i+=1
            else:
                to+=1
                print("Tonton gagal")
            
        sleep(7)
        os.system("cls")
    
    if to == maxTo:
        print("Program exit time-out")
    print("berhasil :", i)

def clickCoba():
    coba = click("src/coba_btn.png", "Coba")
    return coba

def withSubs():
    jumlah = int(input("Berapa channel yg di subs : "))
    i = 0
    to = 0
    maxTo = 8
    os.system("cls")
    while i < jumlah and to < maxTo:
        print("Percobaan ke :", i+1)
        goto = clickGoto()
        sleep(3)
        if goto is None:
            clickSkip()
            clickBaik()
            clickIklan()
            to += 1
        else:
            watching(seconds=80)
            clickSubscribe()
            back = clickBack()
            sleep(3)
            coba  = clickCoba()
            if coba is not None:
                watching(seconds=6)
                clickSubscribe()
                back = clickBack()
                sleep(2)

            dekat = clickDekat()
            clickBaik()
            if dekat is None:
                sleep(10)
                clickIklan()
            clickSkip()
            if back is not None:
                to = 0
                i+=1
            else:
                to+=1
                print("Tonton gagal")
            
        sleep(7)
        os.system("cls")
    
    if to == maxTo:
        print("Program exit time-out")
    print("berhasil :", i)

def main():
    pilih = -1
    while pilih != 0:
        judul()
        pilih = int(input("Choose menu :"))
        if pilih == 1:
            onlyView()
        elif pilih == 2:
            withSubs()
        elif pilih == 0:
            sys.exit()
        else:
            print("Pilihan salah, ulangi lagi")

if __name__ == "__main__":
    main()
    #clickIklan()