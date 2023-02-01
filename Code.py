import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# folder path
dir_path =os.getcwd()

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

# Checking if folder exist and creating folder
path_labor = dir_path + "\\Labor"
if not os.path.exists(path_labor):
     os.mkdir(path_labor)

# loop for file segregation
for i in range(len(res)):
  if res[i][-3:] == "pdf":
      PO = res[i][0 : 12]
      path = path_labor + "\\" + PO
      if not os.path.exists(path):
        os.mkdir(path)
      TY = res[i][13 : 23]
      path = path + "\\" + TY
      if not os.path.exists(path):
        os.mkdir(path)
      original = dir_path + "\\" + res[i]
      target = path + "\\" + res[i]
      shutil.copyfile(original, target)

# Ending messagebox
messagebox.showinfo(title="Message", message="Files have been copied")

