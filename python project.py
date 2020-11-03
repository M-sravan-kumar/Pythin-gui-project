from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title("Ready to Hang!! If you didn't find the word less than 4 chances")
window.geometry("1000x900")
chances=6;
image_paths=['hang.jpg','hangman02.png','hangman03.png','hangman04.png','hangman05.png'
             ,'hangman06.png','hangman07.png']

img = Image.open(image_paths[chances])
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=0, row=0)

chances=chances-1

answer_arr=[]
def clicked(alphabet):
    global chances
    answer= "OLD";
    if alphabet in answer: #Its checks whether the albpbet is there in the answer
        if alphabet=="O":
            btn01["text"] = alphabet;
        elif alphabet=="L":
            btn02["text"] = alphabet;
        elif alphabet=="D":
            btn03["text"] = alphabet;

    else:
        txt="Chances remaining "+str(chances-1);
        label1.configure(text=txt)
        image = Image.open(image_paths[chances])
        image = image.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        chances = chances - 1;
        if chances<0:
            messagebox.showinfo("Loose to guess","Hanged!!!!!")
            window.destroy()
    if btn01["text"]=="O" and btn02["text"]=="L" and btn03["text"]=="D":
        messagebox.showinfo("congratulations", "Won the Game Great Buddy!!!!")
        window.destroy()
    print(chances)


btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn01.grid(column=11, row=3)
btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn02.grid(column=12, row=3)
btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn03.grid(column=13, row=3)



btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn1.grid(column=8, row=4)
btn2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn2.grid(column=9, row=4)
btn3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn3.grid(column=10, row=4)
btn4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn4.grid(column=11, row=4)
btn5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn5.grid(column=12, row=4)
btn6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
btn6.grid(column=13, row=4)
btn7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
btn7.grid(column=14, row=4)
btn8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
btn8.grid(column=15, row=4)

btn9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn9.grid(column=7, row=5)
btn10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
btn10.grid(column=8, row=5)
btn11= Button(window, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
btn11.grid(column=9, row=5)
btn12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn12.grid(column=10, row=5)
btn13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn13.grid(column=11, row=5)
btn14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn14.grid(column=12, row=5)
btn15= Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn15.grid(column=13, row=5)
btn16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn16.grid(column=14, row=5)
btn17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
btn17.grid(column=15, row=5)
btn18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn18.grid(column=16, row=5)
btn19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn19.grid(column=17, row=5)

btn20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn20.grid(column=9, row=6)
btn19 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn19.grid(column=10, row=6)
btn20 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
btn20.grid(column=11, row=6)
btn19 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn19.grid(column=12, row=6)
btn20 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn20.grid(column=13, row=6)
btn19 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn19.grid(column=14, row=6)
btn20 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn20.grid(column=15, row=6)




label1=Label(window,text="Total Chances are : 5")
label1.grid(row=5,column=0)

pic_path=['old.jpg']

img1 = Image.open(pic_path[0])
img1 = img1.resize((150, 150), Image.ANTIALIAS)
img1= ImageTk.PhotoImage(img1)
panel1 = Label(window, image = img1)
panel1.grid(column=70, row=0)

window.mainloop()

