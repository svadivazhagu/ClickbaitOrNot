import pandas as pd
import sys
from tkinter import *
import requests
from io import BytesIO


from PIL import Image, ImageTk


def getImage(datarow):
    response = requests.get(
        'https://img.youtube.com/vi/' + datarow['video_id']+'/0.jpg')
    img = Image.open(BytesIO(response.content))
    return img


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
        self.master.bind('<KeyPress>', self.handleKeyPress)
        self.pack()
        self.create_widgets()

        self.buttonFrame = Frame(self)

        self.isCB = Button(self.buttonFrame, text="Click Bait", height=10, width=10,
                           fg="red", command=self.handleClickBait)
        self.notCB = Button(self.buttonFrame, text='Not CB', height=10, width=10,
                            command=self.handleNotClickBait)

        self.remove = Button(self.buttonFrame, text='Remove',
                             height=10, width=10, command=self.neither)

        self.isCB.pack(side='left')
        self.notCB.pack(side='right')

        self.buttonFrame.pack(side='top')

    def create_widgets(self):
        global i
        self.innerFrame = Frame(self)
        try:
            self.title = Label(self.innerFrame, text=data.iloc[i].title)
            img = getImage(data.iloc[i])
        except:
            i += 1
            self.create_widgets()
            return

        self.img = ImageLabel(self.innerFrame, img)

        self.title.pack(side="top")
        self.innerFrame.pack(side='top')

    def handleKeyPress(self, event):
        if event.char == 'f':
            self.handleClickBait()
        elif (event.char == 'j'):
            self.handleNotClickBait()
        else:
            self.neither()

    def handleClickBait(self):
        data.at[i, 'isCB'] = 1
        self.getNextVideo()

    def handleNotClickBait(self):
        data.at[i, 'isCB'] = 0
        self.getNextVideo()

    def neither(self):
        global i
        data.at[i, 'isCB'] = 2
        self.innerFrame.destroy()
        del self.img
        del self.title
        i += 1
        self.create_widgets()

    def getNextVideo(self):
        global i
        self.innerFrame.destroy()
        del self.img
        del self.title
        print(data.iloc[i].title, data.iloc[i].isCB)

        with open('tracker.txt', 'w') as _out:
            _out.write(str(i))
        with open('output.csv', 'a') as _out:
            _out.write(
                str(i) + ',"' + data.iloc[i].title + '",' + str(data.iloc[i]['isCB']) + '\n')
        i += 1

        self.create_widgets()


data = pd.read_csv('./youtube-new/USvideos.csv', header=[0])
print(data.shape)
data.drop_duplicates(subset='video_id', inplace=True)
print(data.shape)

data['isCB'] = 0
with open('tracker.txt', 'r') as _in:

    i = int(_in.read())

root = Tk()
app = Application(master=root)
app.mainloop()
