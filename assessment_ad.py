from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as msg
import re

def create_conn():
    return mysql.connector.connect(
        host ="localhost",
        username ="root",
        password= "",
        database= "hotel_management"
    )

root = Tk()
root.geometry("1600x900")
root.configure(bg='light green')
root.title("my Tkinter Example")


def checkinn():

    new= Toplevel(root)
    new.geometry("600x600")
    new.title("Register")

    
    window_width = new.winfo_reqwidth()
    window_height = new.winfo_reqheight()
    position_right = int(new.winfo_screenwidth()/3 - window_width/2)
    position_down = int(new.winfo_screenheight()/4 - window_height/2)
    new.geometry("+{}+{}".format(position_right, position_down))
    
    error_message = StringVar()
    error_label = Label(new, textvariable=error_message, font=("arial",15), fg="red")
    error_label.place(x=250, y=400)
    
    success_message = StringVar()    
    success_label = Label(new, textvariable=success_message, font=("arial",15), fg="blue")
    success_label.place(x=250, y=400)
    
    def submit():
        if e_sname.get() =="" or  e_contact.get() =="" or e_email.get() =="" or gender.get() =="" or state.get() =="" or cityvariable.get() =="":
            error_message.set("All Fields Are Mandatory")
        elif not re.match(r"^[0-9]{10}$", e_contact.get()):
            error_message.set("Enter Valid Mobile Number")
        elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", e_email.get()):
            error_message.set("Enter Valid Email Id")
        else:
            conn = create_conn()
            curser = conn.cursor()
            query = "insert into assessment(name,contact,email,gender,state,city) values(%s,%s,%s,%s,%s,%s)"
            args = (e_sname.get(),e_contact.get(),e_email.get(),gender.get(),state.get(),cityvariable.get())
            curser.execute(query,args)
            conn.commit()
            conn.close()
         
            
            success_message.set("Insert Data Successfully")
                        
            neq= Toplevel(root)
            neq.title("Register")
            neq.geometry("1600x900")


            def save_to_database():
                try:
                    days_input=e_day.get()
                    if e_name.get() == "" or e_address.get() == "" or e_number.get() == "" or e_day.get() == "" or (var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0) or (cash.get() == 0 and card.get() == 0):

                            error_message = StringVar()
                            error_label = Label(neq, textvariable=error_message, font=("arial",15), fg="red")
                            error_label.place(x=1200, y=520)
                            error_message.set("Enter All Mandatory Fields")
                    
                    elif not days_input.isdigit() or int(days_input) <= 0:

                        error_message = StringVar()
                        error_label = Label(neq, textvariable=error_message, font=("arial",15), fg="red")
                        error_label.place(x=1200, y=520)
                        error_message.set("Invalid input. Please enter a valid positive number of days")
                    else:
                        conn = create_conn()  
                        cursor = conn.cursor()

                        
                        name = e_name.get()
                        address = e_address.get()
                        number = e_number.get()
                        days = e_day.get()

                        
                        room_types = []
                        if var1.get():
                            room_types.append("DELUX")
                        if var2.get():
                            room_types.append("FULL DELUX")
                        if var3.get():
                            room_types.append("GENERAL")
                        if var4.get():
                            room_types.append("JOINT")

                        
                        payment_method = None
                        if cash.get():
                            payment_method = "By Cash"
                        elif card.get():
                            payment_method = "By Credit/Debit Card"

                        
                        sql_guest = "INSERT INTO guest (name, address, number, days, payment) VALUES (%s, %s, %s, %s, %s)"
                        values_guest = (name, address, number, days, payment_method)
                        cursor.execute(sql_guest, values_guest)
                        
                        
                        guest_id = cursor.lastrowid

                        
                        sql_room_type = "INSERT INTO room_type (type) VALUES (%s)"
                        sql_guest_room_type = "INSERT INTO guest_room_type (guest_id, room_type_id) VALUES (%s, %s)"
                        
                        for room_type in room_types:
                            
                            cursor.execute(sql_room_type, (room_type,))
                            
                            
                            room_type_id = cursor.lastrowid
                            
                            
                            cursor.execute(sql_guest_room_type, (guest_id, room_type_id))

                        conn.commit()
                        conn.close()
                        msg.showinfo("Check INN Status","You Are CheckINN Succssfuly")
                        neq.destroy()
                        new.destroy()

                except mysql.connector.Error as err:
                    print("Error:", err)



            room_label = tk.LabelFrame(neq,  bd=4)
            room_label.pack(fill="x", padx=20, pady=15)  
            room_label.config(height=100)
            room_label1 = tk.LabelFrame(neq,  bd=4) 
            room_label1.pack(fill="x", padx=20, pady=5)
            room_label1.config(height=420) 
            room_label2 = tk.LabelFrame(neq,  bd=4)
            room_label2.pack(fill="x", padx=20, pady=15)  
            room_label2.config(height=200)

            def name_o():
                success_message = StringVar()
                success_label = Label(neq, textvariable=success_message, font=("arial", 10), fg="black")
                success_label.place(x=30, y=590)
                name_input = e_name.get()
                if name_input == "":
                    success_message.set("Name field is empty")
                else:
                    
                    
                    success_message.set("Name has been inputted")

            def address_o():
                success_message = StringVar()
                success_label = Label(neq, textvariable=success_message, font=("arial", 10), fg="black")
                success_label.place(x=30, y=610)
                address_input = e_address.get()
                if address_input == "":
                    success_message.set("Address field is empty")
                else:
                    
                    success_message.set("Address has been inputted")

            def number_o():
                success_message = StringVar()
                success_label = Label(neq, textvariable=success_message, font=("arial", 10), fg="black")
                success_label.place(x=30, y=630)
                number_input = e_number.get()
                
                if not re.match(r"^[0-9]{10}$", number_input):
                    success_message.set("Invalid input. Please enter a valid 10-digit number")
                else:
                    success_message.set("")  
                    success_messaged = StringVar()
                    success_labeld = Label(neq, textvariable=success_messaged, font=("arial", 10), fg="black")
                    success_labeld.place(x=30, y=650)
                    success_messaged.set("Mobile number has been inputted")

            def day_o():
                success_message = StringVar()
                success_label = Label(neq, textvariable=success_message, font=("arial", 10), fg="black")
                success_label.place(x=30, y=670)  

                days_input = e_day.get()

                if not days_input.isdigit() or int(days_input) <= 0:
                    success_message.set("Invalid input. Please enter a valid positive number of days")
                else:
                    success_message.set("")  
                
                    success_messaged = StringVar()
                    success_labeld = Label(neq, textvariable=success_messaged, font=("arial", 10), fg="black")
                    success_labeld.place(x=30, y=690)  
                    success_messaged.set("Number of days has been inputted")       
                
            t=tk.Label(neq,text="YOU    CLICK    ON ",font=("impact",30))
            t.place(x=300,y=45)
            t1=tk.Label(neq,text=" : ",font=("impact",30))
            t1.place(x=750,y=45)
            t2=tk.Label(neq,text="YOU CLICK ON ",font=("impact",30))
            t2.place(x=1000,y=45)


            name=tk.Label(neq,text="ENTER YOUR NAME",font=("Arial Bold",20))
            name.place(x=160,y=170)
            tk.Label(neq,text=":",font=("Arial Bold",20)).place(x=680,y=170)

            e_name=Entry(neq,font=("impact",20),width=40)
            e_name.place(x=730,y=170)
            e_name.insert(0,e_sname.get())
            

            address=tk.Label(neq,text="ENTER YOUR ADDRESS",font=("Arial Bold",20))
            address.place(x=160,y=230)
            tk.Label(neq,text=":",font=("Arial Bold",20)).place(x=680,y=230)

            e_address=Entry(neq,font=("impact",20),width=40)
            e_address.place(x=730,y=230)
            e_address.insert(0,(cityvariable.get(),state.get()))

            
           

            number=tk.Label(neq,text="ENTER YOUR NUMBER ",font=("Arial Bold",20))
            number.place(x=160,y=290)
            tk.Label(neq,text=":",font=("Arial Bold",20)).place(x=680,y=290)

            e_number=Entry(neq,font=("impact",20),width=40)
            e_number.place(x=730,y=290)
            e_number.insert(0,e_contact.get())
         
         
            

            day=tk.Label(neq,text="NUMBER OF DAYS",font=("Arial Bold",20))
            day.place(x=160,y=350)
            tk.Label(neq,text=":",font=("Arial Bold",20)).place(x=680,y=350)

            e_day=Entry(neq,font=("impact",20),width=40)
            e_day.place(x=730,y=350)

            name_ok = Button(neq,text="OK",font=("impact",15),width=5,command=name_o)
            name_ok.place(x=1310,y=165)

            address_ok = Button(neq,text="OK",font=("impact",15),width=5,command=address_o)
            address_ok.place(x=1310,y=225)

            number_ok = Button(neq,text="OK",font=("impact",15),width=5,command=number_o)
            number_ok.place(x=1310,y=285)

            day_ok = Button(neq,text="OK",font=("impact",15),width=5,command=day_o)
            day_ok.place(x=1310,y=345)

            choose=tk.Label(neq,text="CHOOSE YOUR ROOM",font=("Arial Bold",20))
            choose.place(x=520,y=390)

            var1 = IntVar()
            delux=Checkbutton(neq, text="DELUX", variable=var1,font=("arial bold",13),padx=20)
            delux.place(x=300,y=420)

            var2 = IntVar()
            fdelux=Checkbutton(neq, text="FULL DELUX", variable=var2,font=("arial bold",13),padx=20)
            fdelux.place(x=310,y=450)

            var3 = IntVar()
            gen=Checkbutton(neq, text="GENERAL", variable=var3,font=("arial bold",13),padx=20)
            gen.place(x=800,y=420)

            var4 = IntVar()
            joint=Checkbutton(neq, text="JOINT", variable=var4,font=("arial bold",13),padx=20)
            joint.place(x=790,y=450)

            payment=tk.Label(neq,text="CHOOSE PAYMENT METHOD",font=("Arial Bold",20))
            payment.place(x=430,y=480)

            cash = IntVar()
            delux=Checkbutton(neq, text="By Cash", variable=cash,font=("arial bold",10),padx=20)
            delux.place(x=310,y=510)

            card = IntVar()
            fdelux=Checkbutton(neq, text="By Credit/Debit Card", variable=card,font=("arial bold",10),padx=20)
            fdelux.place(x=800,y=510)

            submitb=Button(room_label1,text="submit",font=("impact",25),width=10,command=save_to_database)
            submitb.place(x=1050,y=300)
    
    name = Label(new,text="Name : " ,font=("arial",15))
    name.place(x=150,y=100)
    
    e_sname = Entry(new,width=25,font=("arial",13))
    e_sname.place(x=250,y=107)
    
    contact = Label(new,text="Contact : " ,font=("arial",15))
    contact.place(x=150,y=150)
    
    e_contact = Entry(new,width=25,font=("arial",13))
    e_contact.place(x=250,y=152)
    
    email = Label(new,text="Email : " ,font=("arial",15))
    email.place(x=150,y=200)
    
    e_email = Entry(new,width=25,font=("arial",13))
    e_email.place(x=250,y=203)
    
    g = Label(new,text="Gender : " ,font=("arial",15))
    g.place(x=150,y=250)
    
    gender = StringVar()
    male = Radiobutton(new, text="Male", variable=gender, value="male")
    male.place(x=250,y=250)
    male.configure(font=('arial', 12))
    
    female = Radiobutton(new, text="Female", variable=gender, value="female")
    female.place(x=330,y=250)
    female.configure(font=('arial', 12))
    
    state = Label(new,text="State : " ,font=("arial",15))
    state.place(x=150,y=300)
    

        
    states = ["Select Your State","Gujarat", "Maharashtra", "Rajasthan", "Punjab", "Uttar Pradesh"]

    state = StringVar(root)
    state.set(states[0]) 
    statemenu = OptionMenu(new,state, *states)
    statemenu.place(x=250,y=300)
    statemenu.config(width=26,font=("arial",10))

    city = Label(new,text="City : " ,font=("arial",15))
    city.place(x=150,y=350)   
    
    cities = ["Select Your City","Ahmedabad", "Gandhinagar", "Jaipur", "Ajmer", "Mumbai", "Pune", "Lucknow", "Etawa"]
    
    cityvariable = StringVar(root)
    cityvariable.set(cities[0]) 

    citimenu = OptionMenu(new,cityvariable, *cities)
    citimenu.place(x=250,y=350)
    citimenu.config(width=26,font=("arial",10))
    
    submit = Button(new,text="SUBMIT",bg="red",fg="white",font=("Impact",15),width=16,command=submit)
    submit.place(x=250,y=430)



            





def checkout():
    new = Toplevel(root)
    new.geometry("600x600")
    new.title("Checkout")

    
    window_width = new.winfo_reqwidth()
    window_height = new.winfo_reqheight()
    position_right = int(new.winfo_screenwidth()/3 - window_width/2)
    position_down = int(new.winfo_screenheight()/4 - window_height/2)
    new.geometry("+{}+{}".format(position_right, position_down))
    


    def checkouts():
        try:
            error_message = StringVar()
            error_label = Label(new, textvariable=error_message, font=("arial",15), fg="red")
            error_label.place(x=250, y=400)
            
            success_message = StringVar()    
            success_label = Label(new, textvariable=success_message, font=("arial",15), fg="blue")
            success_label.place(x=250, y=400)
            if e_name.get() == "":
                error_message.set("Name is Mandatory")
            else:
                conn = create_conn()
                cursor = conn.cursor()

                
                name = e_name.get()

                
                sql_guest_id = "SELECT id FROM guest WHERE name = %s"
                cursor.execute(sql_guest_id, (name,))
                guest_id = cursor.fetchone()

                if guest_id:
                    guest_id = guest_id[0]

                
                    sql_guest_room_type = "DELETE FROM guest_room_type WHERE guest_id = %s"
                    cursor.execute(sql_guest_room_type, (guest_id,))

                    
                    sql_guest = "DELETE FROM guest WHERE id = %s"
                    cursor.execute(sql_guest, (guest_id,))

                    
                    sql_assessment = "DELETE FROM register WHERE name = %s"
                    cursor.execute(sql_assessment, (name,))

                    
                    conn.commit()
                    conn.close()
                    success_message.set("Checkout Successful")
                else:
                    error_message.set("Guest Not Found")
        except mysql.connector.Error as err:
            print("Error:", err)



    name = Label(new, text="Name : ", font=("arial", 15))
    name.place(x=150, y=100)

    e_name = Entry(new, width=25, font=("arial", 13))
    e_name.place(x=250, y=107)

    submit = Button(new, text="SUBMIT", bg="red", fg="white", font=("Impact", 15), width=16, command=checkouts)
    submit.place(x=250, y=430)
    
    


def fetch_all_guests():
    try:
        conn = create_conn()  
        cursor = conn.cursor()

        
        sql_guest = "SELECT * FROM guest"
        cursor.execute(sql_guest)
        guests = cursor.fetchall()

        
        window = Toplevel(root)

        
        tree = ttk.Treeview(window, columns=("ID", "Name", "Address", "Number", "Days", "Payment Method", "Room Types"), show='headings')

        
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Address", text="Address")
        tree.heading("Number", text="Number")
        tree.heading("Days", text="Days")
        tree.heading("Payment Method", text="Payment Method")
        tree.heading("Room Types", text="Room Types")

    
        sql_room_type = "SELECT type FROM room_type INNER JOIN guest_room_type ON room_type.id = guest_room_type.room_type_id WHERE guest_id = %s"
        
        for guest in guests:
            cursor.execute(sql_room_type, (guest[0],))
            room_types = cursor.fetchall()
            room_types_str = ", ".join([room_type[0] for room_type in room_types])
            
            tree.insert('', 'end', values=(guest[0], guest[1], guest[2], guest[3], guest[4], guest[5], room_types_str))

    
        tree.pack()

        conn.close()
    except mysql.connector.Error as err:
        print("Error:", err)













welcome = Label(root,text="WELCOME" ,bg="white",font=("impact",35))
welcome.place(x=650,y=10)

hotel = Label(root,text="HOTEL MANAGEMENT" ,bg="white",font=("impact",40))
hotel.place(x=900,y=150)

hotel = Label(root,text="PYTHON TKINTER" ,bg="white",font=("impact",50))
hotel.place(x=900,y=270)

hotel = Label(root,text="GUI" ,bg="white",font=("impact",80))
hotel.place(x=1050,y=400)

checkin = Button(root,text="CheckIn",bg="white",fg="black",font=("arial",23),width="30",command=checkinn)
checkin.place(x=250,y=150)

viewcustomer = Button(root,text="View All Guest",bg="white",fg="black",font=("arial",23),width="30",command=fetch_all_guests)
viewcustomer.place(x=250,y=230)

checkouts = Button(root,text="CheckOut",bg="white",fg="black",font=("arial",23),width="30",command=checkout)
checkouts.place(x=250,y=310)

info= Button(root,text="Get Info of Any Guest",bg="white",fg="black",font=("arial",23),width="30")
info.place(x=250,y=390)

exit = Button(root, text="Exit", command=root.destroy,bg="white",fg="black",font=("arial",23),width="30")
exit.place(x=250,y=470)



root.mainloop()