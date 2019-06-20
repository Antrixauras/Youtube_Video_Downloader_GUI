from tkinter import *
import os
import youtube_dl
from tkinter import filedialog

root = Tk()

root.title("Youtube Video Downloader")
root.configure(background = 'azure')
root.state('zoomed')
width, height = root.winfo_screenwidth(), root.winfo_screenheight()     ##to set width and height of screen
root.geometry('%dx%d+0+0'%(width,height))


def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        # cv2.destroyAllWindows()
root.protocol("WM_DELETE_WINDOW", on_closing)


def clear():
    text1.delete(first=0, last=70)

def browse_button():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def download():
    try:
        URL = text1.get()
        PATH = text2.get()
        ydl_opts = {}
        os.chdir(PATH)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            root.title('Downloading... ' + URL)
            ydl.download([URL])
        print(ydl_opts)
        noty='Your video Downloaded'
        root.title(noty)
        Notification.configure(text=noty,fg='black', bg="white", width=50, font=('times', 17, 'bold','italic'))
        Notification.place(x=350, y=500)
    except Exception as e:
        print(e)

folder_path = StringVar()

from PIL import Image,ImageTk

img = ImageTk.PhotoImage(Image.open('background_youtube.jpg'))
panel = Label(root, image = img)
panel.pack(side = "bottom" , fill = "both", expand = "yes")

tag = Label(root,text = 'Youtube Video Downloader',bg = 'black',fg = 'white',width = '30',height = '3',font = ('algerian',30,'bold'))
tag.place(x = 300,y = 10)

url = Label(root,text = 'Enter URL',bg = 'black',fg = 'white',width = '10',height = '1',font = ('times new roman',25,'bold'))
url.place(x = 170,y = 210)

Notification = Label(root, text="Video downloaded from kanishka gupta", bg="white", fg="black", width=35,height=3, font=('times', 17, 'bold'))

path = Label(root,text = 'Enter Path',bg = 'black',fg = 'white',width = '10',height = '1',font = ('times new roman',25,'bold'))
path.place(x = 170,y = 300)

clear = Button(root,text = 'Clear',command = clear,bg = 'black',fg = 'white',width = '10',height = '1',activebackground = 'azure',font = ('times',25))
clear.place(x = 1100,y = 210)

browse = Button(root,text = 'Browse',bg = 'black',fg = 'white',width = '10',height = '1',command = browse_button,activebackground = 'azure',font = ('times',25))
browse.place(x = 1100,y = 300)

text1 = Entry(root,bg = 'white',width = '34',insertwidth = '3',font = ('times',25,'italic'))
text1.place(x = 400,y = 210)

text2 = Entry(root,bg = 'white',width = '34',textvariable = folder_path,font = ('times',25,'italic'))
text2.place(x = 400,y = 300)

down = Button(root,text = 'Download',command = download,width = '10',height = '1',fg = 'white',bg = 'black',activebackground = 'azure',font = ('times',25,'bold'))
down.place(x = 600,y = 450)

develop = Label(root,text = '@ Developed by Kanishka Gupta',justify = 'center',width = '70',height = '1',bg = 'black',fg = 'white',font = ('times',25,'bold'))
develop.place(x = 0,y = 650)

root.mainloop()