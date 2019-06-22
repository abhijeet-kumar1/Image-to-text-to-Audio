from tkinter import *
from tkinter import filedialog as fa
import pytesseract
from PIL import Image
from gtts import gTTS
import os


root = Tk()
root.title("Image_Text_Audio")
file=" "
flag = 0
def op():
    global file
    file=fa.askopenfilename(title = "Choose an IMAGE")
    
    print(file)
    global flag 
    flag=1
    
def fi():
    if flag == 0:
        w=Message(root,text="Please select an IMAGE first")
        w.grid(row=0,column=1,padx=25,pady=25)
    else:
        print(file)
        img=Image.open(file.encode("utf-8"),"r")
        
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
        txt=pytesseract.image_to_string(img)
        print(txt)
    
        fo=open('filey.txt','w',encoding="utf-8")
        fo.write(txt)
        print ("File created ")

def au():
    if flag == 0:
        w=Message(root,text="Please select an TEXT FILE first")
        w.grid(row=0,column=1)
    else:
        lan='en'
    
        fo=open('filey.txt','r', encoding="utf-8")
        tx=fo.read()
        my=gTTS(text=tx,lang=lan,slow=False)
        
        my.save('audio.mp3')
        print("Audio converted")
        
def opt():
    os.system("filey.txt")
    
    
def opa():
    os.system("audio.mp3")
    
def opi():
    os.system(file)
    


f=Frame(root,height=500,width=400)
l=Label(root,text="Convert \nImage \nto\n Text\n to\n Audio",padx=25,pady=25,bg='White',fg='blue',width=20,font=('aerial',26))
b=Button(root,text='SELECT AN IMAGE',padx=25,pady=25,command=op)
b1=Button(root,text='CONVERT TO TEXT',padx=25,pady=25,command=fi)
b2=Button(root,text='CONVERT TO AUDIO',padx=25,pady=25,command=au)
b3=Button(root,text='OPEN THE TEXT',padx=25,pady=25,command=opt)
b4=Button(root,text='OPEN THE AUDIO',padx=25,pady=25,command=opa)
b5=Button(root,text='OPEN THE IMAGE',padx=25,pady=25,command=opi)
l.grid(row =0 ,column=0)
b.grid(row =1,column=0,padx=25,pady=25,sticky=W)
b1.grid(row=2,column=0,sticky=W,padx=25,pady=25)
b2.grid(row=3,column=0,sticky=W,padx=25,pady=25)
b3.grid(row=2,column=1,sticky=W,padx=25,pady=25)
b4.grid(row=3,column=1,sticky=W,padx=25,pady=25)
b5.grid(row=1,column=1,sticky=W,padx=25,pady=25)

f.grid()

root.mainloop()