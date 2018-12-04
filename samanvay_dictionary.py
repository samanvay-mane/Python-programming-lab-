#importing all the modules
from PyDictionary import PyDictionary
from Tkinter import *
import tkMessageBox
import os
import pyttsx3
#defining functions into variables
dictionary=PyDictionary()
mGui=Tk()

#considering a random variable
ment=StringVar()
# defining the geometry of the gui window
mGui.geometry('509x300+0+0')
#text for the title bar
mGui.title("Digital Lexicon")
#creating a frame for the gui interface
mFrame=Frame(mGui,width=509,height=300,relief=SUNKEN)
mFrame.pack()
#creating a label
mLabel=Label(mGui,font=("GungsuhChe",25,"bold"),text="Digital Lexicon",bd=10,anchor="w")
mLabel.place(x=130,y=0)
#functions defined for the buttons


def TextToSpeech():         #pronounces the given text in the entry box
    mtext = ment.get()
    
    engine = pyttsx3.init()
    engine.say(mtext)
    engine.runAndWait()

def Meaning():              #gives meaning to the provided text
    mtext=ment.get()
    mOutput.delete(0.0,END)
    Word =(dictionary.meaning(mtext))
    mOutput.insert(END,Word)

def Synonym():              #gives synonym to the provided text
    mtext=ment.get()
    mOutput.delete(0.0,END)
    Word =(dictionary.synonym(mtext))
    mOutput.insert(END,Word)

def Antonym():              #gives antonym to the provided text
    mtext=ment.get()
    mOutput.delete(0.0,END)
    Word =(dictionary.antonym(mtext))
    mOutput.insert(END,Word)

def Translate():      #translates the given text to different languages
    mtext=ment.get()
    Language="hi"
    mOutput.delete(0.0,END)
    Word =(dictionary.translate(mtext,Language))
    mOutput.insert(END,Word)

def mHistory():             #displays search history
    root1=Tk()
    root1.title("Search History")
    root1.geometry('520x200+0+0')
    def exit_():
        root1.destroy()
        return
    def clear():
        os.remove(creds)
    f=open(creds, 'a') 
    f.write(mEntry.get())
    f.write('\n')
    f.close()
    if creds==True:
        a=open(creds) 
        a.close()
    d=open('tempfile.txt')    
    stri=str(d.read())
    
    history=Text(root1,width=63,height=7,wrap=WORD,background="white")

    history.delete(0.0,END)

    history.place(x=5,y=10)

    history.insert(END,stri)
    
    ok=Button(root1,text="Ok",justify="center",command=exit_)
    ok.place(x=400,y=140)
    
    clear = Button(root1, text='Clear History', fg='red', command=clear)
    clear.place(x=430,y=140)
    
    Scrollbar1=Scrollbar(root1)
    Scrollbar1.place(x=495,y=10)
    history.configure(yscrollcommand=Scrollbar1.set)
    Scrollbar1.configure(command=history.yview)
def mExit():                #exits the application
    mQuit=tkMessageBox.askokcancel(title="Exit",message="Are You Sure?")
    if mQuit>0:
        mGui.destroy()
        return
    
creds = 'tempfile.txt'
if creds==False:
    a=open(creds,'w')  
    a.close()

#configures the menu bar
menubar=Menu(mGui)
#filemenu
filemenu=Menu(menubar,tearoff=0)
#configures the the exit and search history functions into the file menu
filemenu.add_command(label="Search History",command=mHistory)
filemenu.add_command(label="Exit",command=mExit)
#configures the file menu into the menu bar
menubar.add_cascade(label="File",menu=filemenu)


mGui.config(menu=menubar)       #configures menu bar into the gui

#creates a entry box
mEntry=Entry(mFrame,font=("arial",20),bg="powder blue",bd=10,textvariable=ment,insertwidth=2,justify="center")
mEntry.place(x=85,y=60)
#creates a button for text to speech function
mbutton0=Button(mGui,font=("GungsuhChe",12),text="[(O)]",bd=10,justify="center",command=TextToSpeech,bg="powder blue").place(x=410,y=60)
#creates a button for meaning function
mbutton1=Button(mGui,font=("GungsuhChe",16),text="Meaning",bd=10,justify="center",command=Meaning,bg="powder blue").place(x=0,y=120)
#creates a button for synonym function
mbutton2=Button(mGui,font=("GungsuhChe",16),text="Synonym",bd=10,justify="center",command=Synonym,bg="powder blue").place(x=121,y=120)
#creates a button for antonym function
mbutton3=Button(mGui,font=("GungsuhChe",16),text="Antonym",bd=10,justify="center",command=Antonym,bg="powder blue").place(x=251,y=120)
#creates a button for translate function
mbutton4=Button(mGui,font=("GungsuhChe",16),text="Translate",bd=10,justify="center",command=Translate,bg="powder blue").place(x=378,y=120)

#creates a text box to display the output 
mOutput=Text(mGui,width=63,height=7,wrap=WORD,background="white")
mOutput.place(y=180)

#scrollbar
mScrollbar=Scrollbar(mGui)
mScrollbar.place(x=491,y=180)
#configures scrollbar for the text box into the gui
mOutput.configure(yscrollcommand=mScrollbar.set)
mScrollbar.configure(command=mOutput.yview)

mGui.mainloop()

#End
