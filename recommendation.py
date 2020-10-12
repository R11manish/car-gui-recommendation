#import modules

from tkinter import *
import os
import csv
import pathlib
location=pathlib.Path(__file__).parent.absolute() 
location2 = str(location)+"\hii.png"
print(location2)

# Designing window for registration

def checkinternal():
    print(user_name.get())
    print(seat_no.get())
    print(litres_on.get())
    print(horse_power.get())
    print(choose.get())
    print(choose1.get())


def checkof():
    checkinternal()
    checkcsv()

def checkcsv():
    horse = str(horse_power.get())
    seats = seat_no.get()
    transmisssion = choose.get()
    choice = choose1.get()
    widget_list = all_children(main_screen)
    for item in widget_list:
        item.pack_forget()
    main_screen.geometry('700x600')
    main_screen.title("car recommendator")
    with open('sad1.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data.append(row)
    for cost in data:
        if seats==cost[4] and transmisssion == cost[5] and horse == cost[6] and choice == cost[7]:
            
            Label(main_screen, text="congratulations: "+user_name.get(), font=("Calibri", 20)).pack()
            Label(main_screen, text="").pack()
            Label(main_screen, text="Name of car : "+ cost[1], font=("Calibri", 15)).pack()
            Label(main_screen, text="").pack()
            Label(main_screen, text="price of  the car : " + cost[2], font=("Calibri", 15)).pack()
            Label(main_screen, text="").pack()
            Button(main_screen, text="Try more ", bg="black", fg="white", width=20,height=1, font=("Calibri", 13), command=login).pack()

           
    Label(main_screen, text="sorry: "+user_name.get(), font=("Calibri", 20)).pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="currently we don't have this specification", font=("Calibri", 15)).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Try more ", bg="black", fg="white", width=20,height=1, font=("Calibri", 13), command=login).pack()

    
# Designing window for login
def login():
    
    global user_name
    global seat_no
    global litres_on
    global horse_power
    global choose
    global choose1
    global data
    global car_name

    data =[ ]
    user_name= StringVar()
    seat_no= StringVar()
    litres_on= StringVar()
    choose1 = StringVar()

    widget_list = all_children(main_screen)
    for item in widget_list:
        item.destroy()
    main_screen.geometry('700x600')
    main_screen.title("car recommendator")

    Label(main_screen, text="Enter your name").pack()
    label_1 = Entry(main_screen,textvariable=user_name)
    label_1.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="No of seats on the car - [4 /5] ").pack()
    label_2 = Entry(main_screen, textvariable=seat_no)
    label_2.pack()

    Label(main_screen, text="").pack()
    Label(main_screen, text="litres_on_100km : ( 8 -12 )").pack()
    label_3 = Entry(main_screen, textvariable=litres_on)
    label_3.pack()

    Label(main_screen, text="").pack()
    Label(main_screen,text="""Enter the Horse power :""",justify=LEFT).pack()
    horse_power = Scale(main_screen, from_=150, to=600,length=1000,tickinterval=50,orient=HORIZONTAL)
    horse_power.set(506)
    horse_power.pack()

    
    Label(main_screen, text="").pack()
    choose = StringVar()
    #choose.set(1)  # initializing the choice, i.e. Python

    Label(main_screen,text="""Choose transmission for the car:""",justify=LEFT).pack()
    Radiobutton(main_screen,text="shiftable automatic",variable = choose,value="shiftable automatic" ).pack()
    Radiobutton(main_screen,text="continuous automatic",variable = choose,value="continuous automatic" ).pack()

    
    #choose.set(1)  # initializing the choice, i.e. Python

    Label(main_screen,text="""Choose transmission for the car:""",justify=LEFT).pack()
    Radiobutton(main_screen,text="petrol",variable = choose1,value= "petrol").pack()
    Radiobutton(main_screen,text="hybrid",variable = choose1,value= "hybrid").pack()
    Radiobutton(main_screen,text="diesel",variable = choose1,value= "diesel").pack()



    
    Label(main_screen, text="").pack()
    Button(main_screen, text="Lets Go ", bg="black", fg="white", width=10,height=1, font=("Calibri", 13), command=checkof).pack()
    


def all_children(window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("900x601")
    main_screen.title("car recommendator")
    background_image = PhotoImage(file=location2)

    background = Label(main_screen, image=background_image, bd=0)
    background.place(x=0,y=0)
    Label(text="welcome to your car showroom, please click on below button for car recommendation",
          fg="white", bg="black", width="300", height="2", font=("Calibri", 13)).pack()
    Button(text="start recommendation", bg="black", fg="white",
           height="4", width="30", font=("Calibri", 13), command=login).place(x=20,y=400)
    main_screen.mainloop()


main_account_screen()
