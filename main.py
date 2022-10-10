#!/usr/bin/env python
# -*- coding: utf-8 -

from multiprocessing import Value
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os
from change_md5 import change_md5

# 选择路径
def select_path():
    path_ = askdirectory()
    path.set(path_)

# 开始修改md5
def start_change():
  real_path = path.get()
  log_el = Text(window, font='arial 14')
  if not real_path:
    messagebox.showwarning('提示', '请选择路径')
  elif not os.path.exists(real_path):
    messagebox.showerror('提示', '路径无效')
  else:
    change_md5(real_path, log_el)
    log_el.grid(row=1, rowspan=2, column=0, columnspan=4, )
    messagebox.showinfo('提示', '✅修改完成')
    


window = Tk()
window.title('修改文件md5')
path = StringVar()
log = StringVar()

Label(window, text="目标路径:").grid(row=0, column=0)
Entry(window, textvariable=path).grid(row=0, column=1)
ttk.Button(window, text="路径选择", width=10,command=select_path).grid(row=0, column=2)
ttk.Button(window, text="开始修改", width=10,
       command=start_change).grid(row=0, column=3)

window.mainloop()
