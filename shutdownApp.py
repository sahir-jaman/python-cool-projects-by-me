from tkinter import *
from tkinter import ttk
import os

class ShutDownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ShutdownApp")
        self.root.geometry("300x300+0+0")

        # shutdown command
        def shutdown():
            return os.system("shutdown /s /t 1")

        def restart():
            return os.system("shutdown /r /t 1")

        def logout():
            return os.system("shutdown -l")

        labelFrame = Frame(root, bd=1, relief=RIDGE)
        labelFrame.place(x=105,y=90)

        ttk.Button(labelFrame, text="shutdown", command=shutdown).grid(row=0)
        ttk.Button(labelFrame, text="restart", command=restart).grid(row=1)
        ttk.Button(labelFrame, text="Logout", command=logout).grid(row=2)



if __name__ == "__main__":
    root = Tk()
    obj = ShutDownApp(root)
    root.mainloop()


