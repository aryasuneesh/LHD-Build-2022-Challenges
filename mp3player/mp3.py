from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
def addsongs():
    tSong=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for s in tSong:
        s=s.replace("C:/Users/Arya Suneesh/Desktop/Programming/python/LHD-Build-Challenges/mp3player","")
    sList.insert(END,s)
     
def deletesong():
    cSong=sList.curselection()
    sList.delete(cSong[0])
    
def Play():
    song=sList.get(ACTIVE)
    sList.selection_set(0)
    song=f'C:/Users/Arya Suneesh/Desktop/Programming/python/LHD-Build-Challenges/mp3player/{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    sList.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()

def Next():
    next_one=sList.curselection()
    try:
        next_one=next_one[0]+1
    except:
        sList.selection_set(0)
        next_one=sList.activate(0)
    temp=sList.get(next_one)
    if temp=='':
        temp=f'C:/Users/Arya Suneesh/Desktop/Programming/python/LHD-Build-Challenges/mp3player/{sList.get(0)}'
        sList.selection_clear(0,END)
        sList.activate(0)
        sList.selection_set(0)
        mixer.music.load(temp)
        mixer.music.play()
    else:
        temp=f'C:/Users/Arya Suneesh/Desktop/Programming/python/LHD-Build-Challenges/mp3player/{temp}'
        sList.selection_clear(0,END)
        sList.activate(next_one)
        sList.selection_set(next_one)
        mixer.music.load(temp)
        mixer.music.play()

def Previous():
    previous_one=sList.curselection()
    try:
        previous_one=previous_one[0]-1
    except:
        sList.selection_set(0)
        previous_one=sList.activate(0)
    temp2=sList.get(previous_one)
    if temp2=='':
        temp2=f'C:/Users/Arya Suneesh/Desktop/Programming/python/LHD-Build-Challenges/mp3player/{sList.get(END)}'
        sList.selection_clear(0,END)
        sList.activate(END)
        sList.selection_set(END)
        mixer.music.load(temp2)
        mixer.music.play()
    else:
        temp2=f'C:/Users/Arya Suneesh/Desktop/Programming/python/LHD-Build-Challenges/mp3player/{temp2}'
        sList.selection_clear(0,END)
        sList.activate(previous_one)
        sList.selection_set(previous_one)
        mixer.music.load(temp2)
        mixer.music.play()


root=Tk()
root.title('MP3 Player')

mixer.init()

sList=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('Helvetica',15),height=12,width=47,selectbackground="gray",selectforeground="black")
sList.grid(columnspan=9)

defined_font = font.Font(family='')

play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=3)

Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=2)

previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)


mainMenu=Menu(root)
root.config(menu=mainMenu)
sMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Menu",menu=sMenu)
sMenu.add_command(label="Add songs",command=addsongs)
sMenu.add_command(label="Delete song",command=deletesong)
mainloop()