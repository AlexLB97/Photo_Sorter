#sorterGui.py

import tkinter
from tkinter.filedialog import askdirectory
from os import *
from sorter import *

startFolder = ""
destFolder = ""
startSet = False
destSet = False
startString = ""
destString = ""

def getStart():
    global startFolder
    startFolder = askdirectory()
    startString = startFolder
    startLabel.configure(text = startString, width = len(startString) + 10)
    if startFolder != "":
        startSet = True
    if startSet and destSet:
        sortButton.configure(state = "normal")
    
def getDest():
    global destFolder
    destFolder = askdirectory()
    destString = destFolder
    destLabel.configure(text = destString, width = len(destString) + 10)
    if destString != 0:
        destSet = True
    if destSet:
        sortButton.configure(state = "normal")

    
def checked():
    if checkNames.get() == 1:
        print("Not renaming")
    else:
        print("Renaming")


root = tkinter.Tk()
root.title('Image Sorter')

checkNames = tkinter.IntVar()

root.geometry('700x500')

label = tkinter.Label(root, text = 'Select folders and then click sort!')
nameCheckLabel = tkinter.Label(root, text = "Check this box if the photos are already named uniquely. \n If not check, photos will be renamed to avoid overwriting.")
nameCheckBox = tkinter.Checkbutton(root, variable = checkNames, onvalue = 1, offvalue = 0, text = "Photo names are unique")
currentFolder = tkinter.Button(root, text = 'Choose the folder containing the unsorted folders:', command = getStart)
startLabel = tkinter.Label(root, text = startString, bg = "white", height = 1, width = 40)
destLabel = tkinter.Label(root, text = destString, bg = "white", height = 1, width = 40)
destFolder = tkinter.Button(root, text = 'Choose the top level directory to contain the sorted folders:', command = getDest)
sortButton = tkinter.Button(root, text = 'Sort', width = 25, height = 2, font = (None, 15), bg = "green", state = "disabled", command = lambda: sortPhotos(startFolder, destFolder, checkNames.get()))


label.pack(pady = 8)
currentFolder.pack(pady = 8)
startLabel.pack(pady=8)
destFolder.pack(pady = 8)
destLabel.pack(pady = 8)
nameCheckLabel.pack(pady = 8)
nameCheckBox.pack(pady = 8)
sortButton.pack(pady = 8)

root.mainloop()
