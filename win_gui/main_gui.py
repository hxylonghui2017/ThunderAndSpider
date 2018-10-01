from tkinter import *

class MainGUI:
    def __init__(self):
        self.root=Tk()
        self.root.title("电影下载")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self._set_gui()

    def open_gui(self):
        self.root.mainloop()

    def _set_gui(self):
        Label(self.root, text="资源来源：").grid(row=0, column=0)
        self.entry_01 = Entry(self.root)
        self.entry_01.grid(row=0,column=1,sticky=W)
        Label(self.root, text="资源种子：").grid(row=1, column=0)
        self.text_01 = Text(self.root)
        self.text_01.grid(row=1,column=1, sticky=W)
        Label(self.root, text="当前电影：").grid(row=2, column=0)
        self.entry_02 = Entry(self.root, width=300)
        self.entry_02.grid(row=2,column=1,sticky=W)
        self.frm = Frame(self.root)
        self.frm.grid(row=3, column=1, sticky=W)
        self.btn_01 = Button(self.frm, text="上一部")
        self.btn_01.grid(row=0, column=1)
        self.btn_02 = Button(self.frm, text="下一部")
        self.btn_02.grid(row=0, column=2)
        self.btn_03 = Button(self.frm, text="下载当前部")
        self.btn_03.grid(row=0, column=3)
