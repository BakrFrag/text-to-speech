from Tkinter import *;
#from mtTkinter import *;
from gtts import gTTS;
import playsound;
import os;
root=Tk();
v1=StringVar();
v2=StringVar();
root.title("Speech To Reader");
root.geometry("350x300+50+50");
root.resizable(1,1);
v1=StringVar();
v2=StringVar();
frame1=Frame(root);
frame2=Frame(root);
Label(frame1,text="1.read from text file",font="arial 70 bold",fg="blue",justify="left").grid(row=0,column=0);
Label(frame1,text="2.read entered statements",font="arial 70 bold",fg="blue",justify="left").grid(row=1,column=0);
entry1=Entry(frame1,text="enter choice",textvariable=v1,width=200,justify="left");
entry2=Entry(frame1,width=200,textvariable=v2);
Label(frame1,text="Enter file path or statements",font="arial 70 bold",fg="blue").grid(row=3,column=0)
entry2.grid(row=4,column=0);
entry1.grid(row=2,column=0);
v1.set("the choice");
global textfile;
textfile=" ";
def speechreader():
    global textfile;
    textfile =" ";
    if str(v1.get())=="1":
        filet = open(v2.get(), "r")
        for line in filet.readlines():
            textfile += line;
        tts = gTTS(text=textfile, lang="en");
        tts.save("abobakrvoice.mp3");
        playsound.playsound("abobakrvoice.mp3", True);
        #os.startfile("abobakrvoice.mp3");
        filet.close();
        os.remove("abobakrvoice.mp3")
        #print "removed well!";
    else:
        textfile += v2.get();
        #print textfile;
        tts = gTTS(text=textfile, lang="en");
        tts.save("abobakrvoice.mp3");
        playsound.playsound("abobakrvoice.mp3", True);
        #os.startfile("abobakrvoice.mp3")
        os.remove("abobakrvoice.mp3");
        #print "removed well!";
btn1=Button(frame2,width=50,text="Speaker",font="arial 40 bold",fg="blue",bg="yellow",pady=10);
btn1.config(command=speechreader);
btn1.pack(side=TOP,fill=X);
btn2=Button(frame2,width=50,text="Quit",font="arial 40 bold",fg="blue",bg="yellow");
btn2.config(command=root.destroy);
btn2.pack(side=TOP,fill=X);
frame1.pack(side=TOP);
frame2.pack(side=BOTTOM);
root.mainloop();
