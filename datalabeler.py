import pandas as pd
import sys
from tkinter import *

from PIL import Image, ImageTk


def getImage(datarow):
    return Image.open('test_img.png')


class ImageLabel():
    def __init__(self, frame, imageObj):
        self.imageObj = imageObj
        self.tkImg = ImageTk.PhotoImage(self.imageObj)

        self.label = Label(frame, image=self.tkImg)

        self.label.pack()


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.buttonFrame = Frame(self)

        self.isCB = Button(self.buttonFrame, text="Click Bait",
                           fg="red", command=self.handleClickBait)
        self.notCB = Button(self.buttonFrame, text='Not CB',
                            command=self.handleNotClickBait)

        self.isCB.pack(side='left')
        self.notCB.pack(side='right')

        self.buttonFrame.pack()

    def create_widgets(self):
        global i
        self.innerFrame = Frame(self)
        self.title = Label(self.innerFrame, text=data.iloc[i].title)
        self.img = ImageLabel(self.innerFrame, getImage(data.iloc[i]))

        self.title.pack(side="top")
        self.innerFrame.pack(side='top')

        


    def handleClickBait(self):
        data.at[i, 'isCB'] = True
        self.getNextVideo()

    def handleNotClickBait(self):
        data.loc[i, 'isCB'] = False
        self.getNextVideo()

    def getNextVideo(self):
        global i
        i += 1
        self.create_widgets()
        self.innerFrame.destroy()
        print(data.iloc[i].title, data.iloc[i].isCB)

        with open('tracker.txt', 'w') as _out:
            _out.write(str(i))
        with open('output.csv', 'a') as _out:
            _out.write(str(i), data.iloc[i]['isCB'])
                

data = pd.read_csv('./youtube-new/USvideos.csv', header=[0])
data['isCB'] = False
with open('tracker.txt', 'r') as _in:

    i = int(_in.read())

root = Tk()
app = Application(master=root)
app.mainloop()
