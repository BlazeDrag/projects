
from tkinter import *
import os
os.system('cls')
from numpy import double
def r1():
    global  fr1
    dee()
    fr1=Frame(root)
    fr1.grid(row=1,column=0,columnspan=4)
    def bmi():
        global ca
        global ex
        global dol
        ca.destroy()
        ex.destroy()
        dol.destroy()

        global  variable
        for wid1 in fr1.winfo_children():
            wid1.destroy()
        fr3 = Frame(root)
        fr3.grid(row=1, column=0, columnspan=4)
        def weight():
            global variable
            variable=1
        Button(fr3,text="Press Here to Enter the Weight in kg",font=("Courier", 10),command=weight).grid(row=0,columnspan=2,column=0)
        l3=Entry(fr3,width=30,borderwidth=5)
        l3.grid(row=0,column=2)
        l4 = Entry(fr3, width=30, borderwidth=5)
        l4.grid(row=1, column=2)
        variable=0

        def height():
            global variable
            variable=2
        def Go():
            global l6
            l6.destroy()
            bmi1=(double(l3.get()))/(double(l4.get())**2)
            if (bmi1<18.5):
                l6=Label(fr3,text=str(bmi1)+" "+"Underweight",font=("Courier", 30),background="#20B2AA")
                l6.grid(row=2,column=0,columnspan=3)
            elif (bmi1>=18.5 and bmi1 <25):
                l6=Label(fr3,text=str(bmi1)+" "+"Normal",font=("Courier", 30),background="green")
                l6.grid(row=2,column=0,columnspan=3)
            elif (bmi1>=25 and bmi1 <30):
                l6=Label(fr3,text=str(bmi1)+" "+"Overweight",font=("Courier", 30),background="yellow")
                l6.grid(row=2,column=0,columnspan=3)
            elif (bmi1>=30 and bmi1 <35):
               l6= Label(fr3,text=str(bmi1)+" "+"Obesity  Class 1",font=("Courier", 30),background="#EE6A50")
               l6.grid(row=2,column=0,columnspan=3)
            elif (bmi1 >= 35 and bmi1 <40):
               l6= Label(fr3, text=str(bmi1) + " " + "Obesity  Class 2", font=("Courier", 30), background="#FF4040")
               l6.grid(row=2, column=0, columnspan=3)
            elif (bmi1 >= 40 ):
                l6=Label(fr3, text=str(bmi1) + " " + "Obesity  Class 3", font=("Courier", 30), background="#EE0000")
                l6.grid(row=2, column=0, columnspan=3)


        def num(yh):
            global variable
            if(variable==1):
                curren = l3.get()
                l3.delete(0, END)
                l3.insert(0, str(curren) + str(yh))
            elif(variable==2):
                curre = l4.get()
                l4.delete(0, END)
                l4.insert(0, str(curre) + str(yh))

        Button(fr3, text="Press here to Enter the Height in meter", font=("Courier", 10),command=height).grid(row=1, columnspan=2, column=0)

        Button(fr3, text="1", font=("Courier", 20), command=lambda: num(1)).grid(row=5, column=0)
        Button(fr3, text=str(2), font=("Courier", 20), command=lambda: num(2)).grid(row=5, column=1)
        Button(fr3, text=str(3), font=("Courier", 20), command=lambda: num(3)).grid(row=5, column=2)
        Button(fr3, text=str(4), font=("Courier", 20), command=lambda: num(4)).grid(row=4, column=0 )
        Button(fr3, text=str(5), font=("Courier", 20), command=lambda: num(5)).grid(row=4, column=1 )
        Button(fr3, text=str(6), font=("Courier", 20), command=lambda: num(6)).grid(row=4, column=2 )
        Button(fr3, text=str(7), font=("Courier", 20), command=lambda: num(7)).grid(row=3, column=0 )
        Button(fr3, text=str(8), font=("Courier", 20), command=lambda: num(8)).grid(row=3, column=1)
        Button(fr3, text=str(9), font=("Courier", 20), command=lambda: num(9)).grid(row=3, column=2)
        Button(fr3, text=str(0), font=("Courier", 20), command=lambda: num(0)).grid(row=6, column=1)
        Button(fr3, text=".", font=("Courier", 20), command=lambda: num(".")).grid(row=6, column=2)
        Button(fr3, text="Go", font=("Courier", 20),command=Go).grid(row=6, column=0)
        global l6
        l6=Label(fr3,text="")
        l6.grid(row=2,column=0)
        def back1():
            cons()
            fr = Frame(root)
            fr.grid(row=0, column=0)
            r1()
            for widg in fr3.winfo_children():
                widg.destroy()
            b11.destroy()


        b11=Button(root,text="<--",font=("Courier", 20),command=back1)
        b11.grid(row=0,column=0)
        def back():
            if (variable==1):
                u = str(l3.get())
                l3.delete(0, END)
                i = len(u)
                t = u[0:i - 1]
                if (t[i - 2:i - 1] == "."):
                    l3.insert(0, t[0:i - 2])
                else:
                    l3.insert(0, t[0:i - 1])
            elif  (variable==2):
                u1 = str(l4.get())
                l4.delete(0, END)
                i1 = len(u1)
                t1 = u1[0:i1 - 1]
                if (t1[i1 - 2:i1 - 1] == "."):
                    l4.insert(0, t1[0:i1 - 2])
                else:
                    l4.insert(0, t1[0:i1 - 1])

        def delete():
            if(variable==1):
                l3.delete(0,END)
            elif(variable==2):
                l4.delete(0,END)
        Button(fr3,image=img,command=back,height=40).grid(row=3,rowspan=2,column=3)
        Button(fr3, text="AC", command=delete,font=("Courier,30"),height=5).grid(row=5, rowspan=2, column=3)
    def dis():
        global ca
        global ex
        global dol
        ca.destroy()
        ex.destroy()
        dol.destroy()
        for wid in fr1.winfo_children():
            wid.destroy()
        fr4 = Frame(root)
        ca.destroy()
        ex.destroy()
        dol.destroy()
        fr4.grid(row=1, column=0, columnspan=4)
        l3 = Entry(fr4, width=30, borderwidth=5)
        l3.grid(row=0, column=2,columnspan=2)
        l4 = Entry(fr4, width=30, borderwidth=5)
        l4.grid(row=1, column=2,columnspan=2)
        global varia
        varia =0
        def weight():
            global  varia
            varia=1
        def height():
            global varia
            varia=2
        def num(yh):
            global varia
            if(varia==1):
                curren = l3.get()
                l3.delete(0, END)
                l3.insert(0, str(curren) + str(yh))
            elif(varia==2):
                curre = l4.get()
                l4.delete(0, END)
                l4.insert(0, str(curre) + str(yh))
        def back():
            if (varia==1):
                u = str(l3.get())
                l3.delete(0, END)
                i = len(u)
                t = u[0:i - 1]
                if (t[i - 2:i - 1] == "."):
                    l3.insert(0, t[0:i - 2])
                else:
                    l3.insert(0, t[0:i - 1])
            elif  (varia==2):
                u1 = str(l4.get())
                l4.delete(0, END)
                i1 = len(u1)
                t1 = u1[0:i1 - 1]
                if (t1[i1 - 2:i1 - 1] == "."):
                    l4.insert(0, t1[0:i1 - 2])
                else:
                    l4.insert(0, t1[0:i1 - 1])

        def delete():
            if(varia==1):
                l3.delete(0,END)
            elif(varia==2):
                l4.delete(0,END)
        def back1():
            fr = Frame(root)
            fr.grid(row=0, column=0)

            for widg in fr4.winfo_children():
                widg.destroy()
            b11.destroy()
            cons()

            r1()
        def Go():
            global l5
            l5.destroy()
            global l6
            l6.destroy()
            price=double(l3.get())-(double(l3.get())*double(l4.get())/100)
            disc_price=double(l3.get()) * double(l4.get()) / 100
            l5=Label(fr4,text=str(price),font=("Courier",20))
            l5.grid(row=2,column=2)
            l6=Label(fr4,text="You Save"+" "+ str(disc_price),font=("Courier",20))
            l6.grid(row=3,column=1)

        Button(fr4, text="Press here to Enter the Discount(% off)", font=("Courier", 10), command=height).grid(row=1,columnspan=2,column=0)
        Button(fr4, text="Press here to Enter the  Original Price", font=("Courier", 10), command=weight).grid(row=0,columnspan=2,column=0)
        Label(fr4,text="Final Price :",font=("Courier",20)).grid(row=2,column=0,columnspan=2)
        Button(fr4, text="1", font=("Courier", 20), command=lambda: num(1)).grid(row=6, column=0)
        Button(fr4, text=str(2), font=("Courier", 20), command=lambda: num(2)).grid(row=6, column=1)
        Button(fr4, text=str(3), font=("Courier", 20), command=lambda: num(3)).grid(row=6, column=2)
        Button(fr4, text=str(4), font=("Courier", 20), command=lambda: num(4)).grid(row=5, column=0)
        Button(fr4, text=str(5), font=("Courier", 20), command=lambda: num(5)).grid(row=5, column=1)
        Button(fr4, text=str(6), font=("Courier", 20), command=lambda: num(6)).grid(row=5, column=2)
        Button(fr4, text=str(7), font=("Courier", 20), command=lambda: num(7)).grid(row=4, column=0)
        Button(fr4, text=str(8), font=("Courier", 20), command=lambda: num(8)).grid(row=4, column=1)
        Button(fr4, text=str(9), font=("Courier", 20), command=lambda: num(9)).grid(row=4, column=2)
        Button(fr4, text=str(0), font=("Courier", 20), command=lambda: num(0)).grid(row=7, column=1)
        Button(fr4, text=".", font=("Courier", 20), command=lambda: num(".")).grid(row=7, column=2)
        Button(fr4, text="Go", font=("Courier", 20), command=Go).grid(row=7, column=0)
        b11 = Button(root, text="<--", font=("Courier", 20), command=back1)
        b11.grid(row=0, column=0)
        Button(fr4, image=img, command=back, height=40).grid(row=3, rowspan=2, column=3)
        Button(fr4, text="AC", command=delete, font=("Courier,30"), height=5).grid(row=5, rowspan=2, column=3)
        global l5
        global  l6
        l5=Label(fr4,text="")
        l5.grid(row=2,column=2)
        l6 = Label(fr4, text="")
        l6.grid(row=3, column=1)
    def lent():
        global ca
        global ex
        global dol
        ca.destroy()
        ex.destroy()
        dol.destroy()

        for wid in fr1.winfo_children():
            wid.destroy()
        fr5 = Frame(root)
        fr5.grid(row=1, column=0, columnspan=4)
        menu = StringVar()
        menu.set("Select the unit")
        drop = OptionMenu(fr5, menu, "Meter", "Kilometer", "Centimeter", "Millimeter", "Foot", "Inch")
        drop.grid(row=0, column=1)
        Label(fr5, text="From").grid(row=0, column=0)
        l = Entry(fr5, width=30, borderwidth=5)
        l.grid(row=0, columnspan=2, column=2)
        l1 = Entry(fr5, width=30, borderwidth=5)
        l1.grid(row=1, columnspan=2, column=2)
        men = StringVar()
        men.set("Select the unit")
        dro = OptionMenu(fr5, men, "Meter", "Kilometer", "Centimeter", "Millimeter", "Foot", "Inch")
        dro.grid(row=1, column=1)
        Label(fr5, text="To").grid(row=1, column=0)
        def numb(uj):
            fi=l.get()
            l.delete(0,END)
            l.insert(0,str(fi)+str(uj))
            if (menu.get() == "Meter"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 100))
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 1000))
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 3.28084))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 39.3701))
            elif (menu.get() == "Kilometer"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) * 1000)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 100000))
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 1000000))
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 3280.84))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 39370.1))
            elif (menu.get() == "Centimeter"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 100)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 100000)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 10))
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.0328084))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.393701))
            elif (menu.get() == "Millimeter"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000000)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 10)
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.00328084))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.0393701))
            elif (menu.get() == "Foot"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 3.28084)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 3280.84)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.0328084)
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.00328084)
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 12))
            elif (menu.get() == "Inch"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) * 0.0254)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 39370.1)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.393701)
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.0393701)
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 12)
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())


        def back():
            fr = Frame(root)
            fr.grid(row=0, column=0)
            for widg in fr5.winfo_children():
                widg.destroy()
            b11.destroy()
            cons()
            r1()
        def delete():
            u = str(l.get())
            l.delete(0, END)
            i = len(u)
            t = u[0:i - 1]
            if (t[i - 2:i - 1] == "."):
                l.insert(0, t[0:i - 2])
            else:
                l.insert(0, t[0:i - 1])
            if (menu.get() == "Meter"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 100))
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 1000))
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 3.28084))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 39.3701))
            elif (menu.get() == "Kilometer"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) * 1000)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 100000))
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 1000000))
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 3280.84))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 39370.1))
            elif (menu.get() == "Centimeter"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 100)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 100000)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 10))
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.0328084))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.393701))
            elif (menu.get() == "Millimeter"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000000)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 10)
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.00328084))
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 0.0393701))
            elif (menu.get() == "Foot"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 3.28084)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 3280.84)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.0328084)
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.00328084)
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, str(double(l.get()) * 12))
            elif (menu.get() == "Inch"):
                if (men.get() == "Meter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) * 0.0254)
                elif (men.get() == "Kilometer"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 39370.1)
                elif (men.get() == "Centimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.393701)
                elif (men.get() == "Millimeter"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 0.0393701)
                elif (men.get() == "Foot"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 12)
                elif (men.get() == "Inch"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())

        Button(fr5, text="1", font=("Courier", 20), command=lambda: numb(1)).grid(row=4, column=0)
        Button(fr5, text=str(2), font=("Courier", 20), command=lambda: numb(2)).grid(row=4, column=1)
        Button(fr5, text=str(3), font=("Courier", 20), command=lambda: numb(3)).grid(row=4, column=2)
        Button(fr5, text=str(4), font=("Courier", 20), command=lambda: numb(4)).grid(row=3, column=0)
        Button(fr5, text=str(5), font=("Courier", 20), command=lambda: numb(5)).grid(row=3, column=1 )
        Button(fr5, text=str(6), font=("Courier", 20), command=lambda: numb(6)).grid(row=3, column=2 )
        Button(fr5, text=str(7), font=("Courier", 20), command=lambda: numb(7)).grid(row=2, column=0)
        Button(fr5, text=str(8), font=("Courier", 20), command=lambda: numb(8)).grid(row=2, column=1)
        Button(fr5, text=str(9), font=("Courier", 20), command=lambda: numb(9)).grid(row=2, column=2)
        Button(fr5, text=str(0), font=("Courier", 20), command=lambda: numb(0)).grid(row=5, column=1)
        Button(fr5, text=".", font=("Courier", 20), command=lambda: numb(".")).grid(row=5, column=2)
        b11 = Button(root, text="<--", font=("Courier", 20), command=back)
        Button(fr5, image=img, command=delete, height=40).grid(row=2, rowspan=2, column=3)
        Button(fr5, text="AC", command=delete, font=("Courier,30"), height=5).grid(row=4, rowspan=2, column=3)
        b11.grid(row=0, column=0)

    def mggb():
        global ca
        global ex
        global dol
        ca.destroy()
        ex.destroy()
        dol.destroy()

        for wid in fr1.winfo_children():
            wid.destroy()
        fr2=Frame(root)
        fr2.grid(row=1,column=0,columnspan=4)
        def back():
            global b12
            fr=Frame(root)
            fr.grid(row=0,column=0)
            r1()
            for widg in fr2.winfo_children():
                widg.destroy()
            b11.destroy()
            cons()

        def numb(uj):
            fi=l.get()
            l.delete(0,END)
            l.insert(0,str(fi)+str(uj))
            if(menu.get()=="Kb"):
                if(men.get()=="Kb"):
                    l1.delete(0,END)
                    l1.insert(0,l.get())
                if(men.get()=="Mb"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get())/1000)
                if(men.get()=="Gb"):
                    l1.delete(0, END)
                    l1.insert(0,str(double(l.get())/1000000))
            if (menu.get() == "Mb"):
                if (men.get() == "Kb"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get())*1000)
                if (men.get() == "Mb"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                if (men.get() == "Gb"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) / 1000)
            if (menu.get() == "Gb"):
                if (men.get() == "Kb"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get())*100000)
                if (men.get() == "Mb"):
                    l1.delete(0, END)
                    l1.insert(0, double(l.get()) * 1000)
                if (men.get() == "Gb"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
        Button(fr2,text="1",font=("Courier",20),command=lambda :numb(1)).grid(row=4,column=0,padx=20,pady=20)
        Button(fr2, text=str(2), font=("Courier", 20), command=lambda: numb(2)).grid(row=4 , column=1, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(3), font=("Courier", 20), command=lambda: numb(3)).grid(row=4, column=2, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(4), font=("Courier", 20), command=lambda: numb(4)).grid(row=3, column=0, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(5), font=("Courier", 20), command=lambda: numb(5)).grid(row=3, column=1, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(6), font=("Courier", 20), command=lambda: numb(6)).grid(row=3, column=2, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(7), font=("Courier", 20), command=lambda: numb(7)).grid(row=2, column=0, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(8), font=("Courier", 20), command=lambda: numb(8)).grid(row=2, column=1, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(9), font=("Courier", 20), command=lambda: numb(9)).grid(row=2, column=2, padx=20,
                                                                                     pady=20)
        Button(fr2, text=str(0), font=("Courier", 20), command=lambda: numb(0)).grid(row=5, column=1, padx=20,
                                                                                     pady=20)
        Button(fr2, text=".", font=("Courier", 20), command=lambda: numb(".")).grid(row=5, column=2, padx=20,pady=20)

        b11=Button(root,text="<--",font=("Courier",20),command=back)
        b11.grid(row=0,column=0)
        menu=StringVar()
        menu.set("Select the unit")
        drop=OptionMenu(fr2,menu,"Kb","Mb","Gb")
        drop.grid(row=0,column=1)
        Label(fr2,text="From").grid(row=0,column=0)
        l=Entry(fr2,width=30,borderwidth=5)
        l.grid(row=0,columnspan=2,column=2)
        l1= Entry(fr2, width=30, borderwidth=5)
        l1.grid(row=1, columnspan=2, column=2)
        men = StringVar()
        men.set("Select the unit")
        dro = OptionMenu(fr2, men, "Kb", "Mb", "Gb")
        dro.grid(row=1, column=1)
        Label(fr2, text="To").grid(row=1, column=0)

        def de():
            u = str(l.get())
            l.delete(0, END)
            i = len(u)
            t = u[0:i - 1]
            if (t[i - 2:i - 1] == "."):
                l.insert(0, t[0:i - 2])
            else:
                l.insert(0, t[0:i - 1])
            if (menu.get() == "Kb"):
                if (men.get() == "Kb"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                if (men.get() == "Mb"):
                    l1.delete(0, END)
                    l1.insert(0, str(float(l.get()) / 1000))
                if (men.get() == "Gb"):
                    l1.delete(0, END)
                    l1.insert(0, str(float(l.get()) / 1000000))
            if (menu.get() == "Mb"):
                if (men.get() == "Kb"):
                    l1.delete(0, END)
                    l1.insert(0, float(l.get()) * 1000)
                if (men.get() == "Mb"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())
                if (men.get() == "Gb"):
                    l1.delete(0, END)
                    l1.insert(0, str(float(l.get()) / 1000))
            if (menu.get() == "Gb"):
                if (men.get() == "Kb"):
                    l1.delete(0, END)
                    l1.insert(0, float(l.get()) * 100000)
                if (men.get() == "Mb"):
                    l1.delete(0, END)
                    l1.insert(0, str(float(l.get()) * 1000))
                if (men.get() == "Gb"):
                    l1.delete(0, END)
                    l1.insert(0, l.get())

        Button(fr2, image=img,command=de).grid(row=4,rowspan=2,column=3,pady=20)

        def cl():
            l.delete(0, END)
            l1.delete(0,END)

        clear = Button(fr2, text="AC", command=cl, font=("Courier", 20)).grid(row=2,column=3,rowspan=2)

    b1=Button(fr1,text="mggb",command=mggb)
    b1.grid(row=0,column=0,pady=20,padx=20)
    b2 = Button(fr1, text="bmi",command=bmi)
    b2.grid(row=0, column=1, pady=20, padx=20)
    b3 = Button(fr1, text="dis",command=dis)
    b3.grid(row=0, column=2, pady=20, padx=20)
    b4 = Button(fr1, text="len",command=lent)
    b4.grid(row=1, column=0, pady=20, padx=20)
    b5 = Button(fr1, text="area")
    b5.grid(row=1, column=1, pady=20, padx=20)
    b6 = Button(fr1, text="volu")
    b6.grid(row=1, column=2, pady=20, padx=20)
    b7 = Button(fr1, text="temp")
    b7.grid(row=2, column=0, pady=20, padx=20)
    b8 = Button(fr1, text="speed")
    b8.grid(row=2, column=1, pady=20, padx=20)
    b9 = Button(fr1, text="time")
    b9.grid(row=2, column=2, pady=20, padx=20)
    b10 = Button(fr1, text="mass")
    b10.grid(row=3, column=0, pady=20, padx=20)
    b11 = Button(fr1, text="numeral")
    b11.grid(row=3, column=1, pady=20, padx=20)
def tt():
    global  root

    global fr
    global fr1
    for widget in fr1.winfo_children():
        widget.destroy()

    fr=Frame(root)
    fr.grid(row=1,column=0,columnspan=4)
    root.title("CALCULATOR")
    r= Entry(fr,width=60,borderwidth=5)
    r.grid(row=1,column=0,columnspan=10,pady=20)


    def de():
        u=str(r.get())
        r.delete(0,END)
        i=len(u)
        t=u[0:i-1]
        if(t[i-2:i-1]=="."):
            r.insert(0,t[0:i-2])
        else:
            r.insert(0,t[0:i-1])
    def add(nm):
        current=r.get()
        r.delete(0,END)
        r.insert(0, str(current)+str(nm))
    def func():
        new = str(r.get())

        for char in new:
            if(char=='+'):
                y= new.find(char)
                gn=float(new[0:y])+float(new[y+1:])
            if (char == '-'):
                y = new.find(char)
                gn = float(new[0:y]) - float(new[y + 1:])
            if (char == '*'):
                y = new.find(char)
                gn = float(new[0:y]) * float(new[y + 1:])
            if (char == '/'):
                y = new.find(char)
                gn = float(new[0:y]) / float(new[y + 1:])
            if (char == '%'):
                y = new.find(char)
                gn = float(new[0:y]) %float(new[y + 1:])
            if (char == '^'):
                y = new.find(char)
                gn = float(new[0:y]) ** float(new[y + 1:])
        r.delete(0,END)
        r.insert(0,gn)
    def cl():
        r.delete(0,END)


    Button(fr,text="1",fg="black",bg="white",command=lambda :add(1),font=("Courier",20)).grid(row=5,column=0)

    c= Button(fr,text="2",fg="black",bg="white",command=lambda :add(2),font=("Courier",20)).grid(row=5,column=1,padx=20,pady=20)
    d= Button(fr,text="3",fg="black",bg="white",command=lambda :add(3),font=("Courier",20)).grid(row=5,column=2,padx=20,pady=20)
    e= Button(fr,text="4",fg="black",bg="white",command=lambda :add(4),font=("Courier",20)).grid(row=4,column=0,padx=20,pady=20)
    f= Button(fr,text="5",fg="black",bg="white",command=lambda :add(5),font=("Courier",20)).grid(row=4,column=1,padx=20,pady=20)
    g= Button(fr,text="6",fg="black",bg="white",command=lambda :add(6),font=("Courier",20)).grid(row=4,column=2,padx=20,pady=20)
    h= Button(fr,text="7",fg="black",bg="white",command=lambda :add(7),font=("Courier",20)).grid(row=3,column=0,padx=20,pady=20)
    i= Button(fr,text="8",fg="black",bg="white",command=lambda :add(8),font=("Courier",20)).grid(row=3,column=1,padx=20,pady=20)
    j= Button(fr,text="9",fg="black",bg="white",command=lambda :add(9),font=("Courier",20)).grid(row=3,column=2,padx=20,pady=20)
    k= Button(fr,text="0",fg="black",bg="white",command=lambda :add(0),font=("Courier",20))
    p= Button(fr,text="+",fg="black",bg="white",command=lambda :add("+"),font=("Courier",20))
    sub= Button(fr,text="-",fg="black",bg="white",command=lambda :add("-"),font=("Courier",20))
    mul= Button(fr,text="*",fg="black",bg="white",command=lambda :add("*"),font=("Courier",20))
    div= Button(fr,text="/",fg="black",bg="white",command=lambda :add("/"),font=("Courier",20))
    mod= Button(fr,text="%",fg="black",bg="white",command=lambda :add("%"),font=("Courier",20))
    po = Button(fr,text="^",fg="black",bg="white",command=lambda :add("^"),font=("Courier",20))
    en= Button(fr,text="=",fg="black",bg="white",command=func,font=("Courier",20))
    clear=Button(fr,text="C",command=cl,font=("Courier",20),fg="black",bg="white")
    do = Button(fr,text=".",fg="black",bg="white",command=lambda :add("."),font=("Courier",20))
    j= Button(fr,image=img,fg="black",bg="white",command=de).grid(row=2,column=1,padx=20,pady=20)
    do.grid(row=6,column=2,padx=20,pady=20)
    k.grid(row =6,column=1,padx=20,pady=20)
    p.grid(row =5 ,column=3,padx=20,pady=20)
    sub.grid(row =4 ,column=3,padx=20,pady=20)
    mul.grid(row =3 ,column=3,padx=20,pady=20)
    div.grid(row =2 ,column=3,padx=20,pady=20)
    mod.grid(row =2 ,column=2,padx=20,pady=20)
    en.grid(row =6 ,column=3,padx=20,pady=20)
    clear.grid(row=2,column=0,padx=20,pady=20)
    root.mainloop()
root=Tk()
fr=Frame(root)
fr.grid(row=1,column=0,columnspan=4)
root.title("CALCULATOR")
r= Entry(fr,width=60,borderwidth=5)
r.grid(row=1,column=0,columnspan=10,pady=20)
img=PhotoImage(file="backspace_outline_icon_139934.png")
img1=PhotoImage(file="icon.png")
img2=PhotoImage(file="call.png")
img3=PhotoImage(file="dollar.png")

def de():
    u=str(r.get())
    r.delete(0,END)
    i=len(u)
    t=u[0:i-1]
    if(t[i-2:i-1]=="."):
        r.insert(0,t[0:i-2])
    else:
        r.insert(0,t[0:i-1])
def add(nm):
    current=r.get()
    r.delete(0,END)
    r.insert(0, str(current)+str(nm))
def func():
    new = str(r.get())

    for char in new:
        if(char=='+'):
            y= new.find(char)
            gn=float(new[0:y])+float(new[y+1:])
        if (char == '-'):
            y = new.find(char)
            gn = float(new[0:y]) - float(new[y + 1:])
        if (char == '*'):
            y = new.find(char)
            gn = float(new[0:y]) * float(new[y + 1:])
        if (char == '/'):
            y = new.find(char)
            gn = float(new[0:y]) / float(new[y + 1:])
        if (char == '%'):
            y = new.find(char)
            gn = float(new[0:y]) %float(new[y + 1:])
        if (char == '^'):
            y = new.find(char)
            gn = float(new[0:y]) ** float(new[y + 1:])
    r.delete(0,END)
    r.insert(0,gn)
def cl():
    r.delete(0,END)
Button(fr,text="1",fg="black",bg="white",command=lambda :add(1),font=("Courier",20)).grid(row=5,column=0)
c= Button(fr,text="2",fg="black",bg="white",command=lambda :add(2),font=("Courier",20)).grid(row=5,column=1,padx=20,pady=20)
d= Button(fr,text="3",fg="black",bg="white",command=lambda :add(3),font=("Courier",20)).grid(row=5,column=2,padx=20,pady=20)
e= Button(fr,text="4",fg="black",bg="white",command=lambda :add(4),font=("Courier",20)).grid(row=4,column=0,padx=20,pady=20)
f= Button(fr,text="5",fg="black",bg="white",command=lambda :add(5),font=("Courier",20)).grid(row=4,column=1,padx=20,pady=20)
g= Button(fr,text="6",fg="black",bg="white",command=lambda :add(6),font=("Courier",20)).grid(row=4,column=2,padx=20,pady=20)
h= Button(fr,text="7",fg="black",bg="white",command=lambda :add(7),font=("Courier",20)).grid(row=3,column=0,padx=20,pady=20)
i= Button(fr,text="8",fg="black",bg="white",command=lambda :add(8),font=("Courier",20)).grid(row=3,column=1,padx=20,pady=20)
j= Button(fr,text="9",fg="black",bg="white",command=lambda :add(9),font=("Courier",20)).grid(row=3,column=2,padx=20,pady=20)
k= Button(fr,text="0",fg="black",bg="white",command=lambda :add(0),font=("Courier",20))
p= Button(fr,text="+",fg="black",bg="white",command=lambda :add("+"),font=("Courier",20))
sub= Button(fr,text="-",fg="black",bg="white",command=lambda :add("-"),font=("Courier",20))
mul= Button(fr,text="*",fg="black",bg="white",command=lambda :add("*"),font=("Courier",20))
div= Button(fr,text="/",fg="black",bg="white",command=lambda :add("/"),font=("Courier",20))
mod= Button(fr,text="%",fg="black",bg="white",command=lambda :add("%"),font=("Courier",20))
po = Button(fr,text="^",fg="black",bg="white",command=lambda :add("^"),font=("Courier",20))
en= Button(fr,text="=",fg="black",bg="white",command=func,font=("Courier",20))
clear=Button(fr,text="C",command=cl,font=("Courier",20),fg="black",bg="white")
do = Button(fr,text=".",fg="black",bg="white",command=lambda :add("."),font=("Courier",20))
j= Button(fr,image=img,fg="black",bg="white",command=de)
j.grid(row=2,column=1,padx=20,pady=20)
do.grid(row=6,column=2,padx=20,pady=20)
k.grid(row =6,column=1,padx=20,pady=20)
p.grid(row =5 ,column=3,padx=20,pady=20)
sub.grid(row =4 ,column=3,padx=20,pady=20)
mul.grid(row =3 ,column=3,padx=20,pady=20)
div.grid(row =2 ,column=3,padx=20,pady=20)
mod.grid(row =2 ,column=2,padx=20,pady=20)
en.grid(row =6 ,column=3,padx=20,pady=20)
clear.grid(row=2,column=0,padx=20,pady=20)
global ca
global ex
global dol
ca = Button(root, image=img2, fg="black", bg="white", font=("Courier", 20), command=tt)
ca.grid(row=0, column=1,padx=20, pady=20)
ex = Button(root, image=img1, fg="black", bg="white", font=("Courier", 20),command=r1)
ex.grid(row=0, column=2, padx=20, pady=20)
dol = Button(root, image=img3, fg="black", bg="white", font=("Courier", 20))
dol.grid(row=0, column=3, padx=20, pady=20)
def cons():
    global ca
    global ex
    global dol
    ca = Button(root, image=img2, fg="black", bg="white", font=("Courier", 20), command=tt)
    ca.grid(row=0, column=1, padx=20, pady=20)
    ex = Button(root, image=img1, fg="black", bg="white", font=("Courier", 20), command=r1)
    ex.grid(row=0, column=2, padx=20, pady=20)
    dol = Button(root, image=img3, fg="black", bg="white", font=("Courier", 20))
    dol.grid(row=0, column=3, padx=20, pady=20)
def dee():
    global fr
    for widget in fr.winfo_children():
        widget.destroy()
root.mainloop()


