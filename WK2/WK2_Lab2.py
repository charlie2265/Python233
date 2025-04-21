# Program:      WK2 Lab - Order Entry Form
# Programmer:   Charlie Ritter
# Date:         4/8/2025
# Purpose:      Design a functional GUI program using Tkinter. An Order Form with selections and itemized totals. 

# from tkinter import * # Did not bring in combobox
from tkinter import ttk # Imported for combobox
import tkinter as tk

#---------Functions----------#
# Function will take the qty amount and display in items sum_frame entry box
def quantity():
    sel_sand = int(item_qty.get())
    sandwich["text"] = f"X {sel_sand}"
    
    sel_chips = int(item_qty2.get())
    chips["text"] = f"X {sel_chips}"

    sel_drink = int(item_qty3.get())
    drinks["text"] = f"X {sel_drink}"

     
# sum all of the sum_frame entry boxes and display total.
def total():
    # sandwich total
    sel_sand = int(item_qty.get())
    sand_tot = sel_sand * 5
    sand_price["text"] = f"${sand_tot}"

    # chips total
    sel_chips = int(item_qty2.get())
    chips_tot = sel_chips * 2
    chips_price["text"] = f"${chips_tot}"

    # drinks total
    sel_drinks = int(item_qty3.get())
    drinks_tot = sel_drinks * 1
    drinks_price["text"] = f"${drinks_tot}"

    sum_total = sand_tot + chips_tot + drinks_tot
    order_total["text"] = f"${sum_total}"

# Clear qty spinboxes in the sel_frame when
# called with the "Clear Order" button command.
def clear_qty():
    Clear_var = tk.IntVar(sel_frame)
    Clear_var.set(0)
    item_qty.config(textvariable=Clear_var)

    Clear_var2 = tk.IntVar(sel_frame)
    Clear_var2.set(0)
    item_qty2.config(textvariable=Clear_var2)

    Clear_var3 = tk.IntVar(sel_frame)
    Clear_var3.set(0)
    item_qty3.config(textvariable=Clear_var3)

# Clear item Comboboxes in the sel_frame when
# called with the "Clear Order" button command.
def clear_sel(): 
    choose_sand.set("")
    choose_drink.set("")
    choose_chips.set("")
    

window = tk.Tk()
window.title("Lunch Order Form")

#-------Frame set ups---------#
bg_one = "#E6FFCC"
d_grey = "#3399FF"
# page title
header_frame = tk.Frame(master=window, width=1000, height= 100, bg='#FFCCCC')
header_frame.pack(fill='both', expand=True)

# order fill here
sel_frame = tk.Frame(master=window, width=800, height=400, bg=bg_one)
sel_frame.pack(fill='both', side=tk.LEFT, expand=True)

# itemized totals
sum_frame = tk.Frame(master=window, width=200, bg=d_grey)
sum_frame.pack(fill='both', side=tk.RIGHT, expand=True)

# -----header frame----- #
label = tk.Label(master=header_frame,                 
                 text=('Place Your Lunch Order'),
                 bg='#FFCCCC',
                 font=('Time', '33', 'italic'))
label.place(x=290, y=20)

# ----Fill out the order form in sel_frame---- #
# Enter Item Labels
label = tk.Label(master=sel_frame, 
                 text="Choose Sandwich - $5", 
                 bg=bg_one,
                 font=('Helvetica', '12', 'bold', 'italic'))
label.place(x=100, y=50)

label = tk.Label(master=sel_frame, 
                 text="Choose Chips - $2", 
                 bg=bg_one,
                 font=('Helvetica', '12', 'bold', 'italic'))
label.place(x=100, y=100)

label = tk.Label(master=sel_frame, 
                 text="Choose Drink - $1", 
                 bg=bg_one,
                 font=('Helvetica', '12', 'bold', 'italic'))
label.place(x=100, y=150)

# Enter Sandwich Combobox
choose_sand = ttk.Combobox(master=sel_frame,                            
                           values=("Ham", "Turkey", "Pastrami", "Sietan"))
                           
choose_sand.place(x=300, y=50)

# Enter Chips Combobox
choose_chips = ttk.Combobox(master=sel_frame,                            
                           values=("Vinnegar", "Salt & Pepper", "Tortilla"))
choose_chips.place(x=300, y=100)

# Enter Drink Combobox
choose_drink = ttk.Combobox(master=sel_frame,                            
                           values=("La Croix", "Spindrift", "Coca-Cola", "Water"))
choose_drink.place(x=300, y=150)

# Item qty Entry spinbox
item_qty = tk.Spinbox(master=sel_frame, from_= 0, to=5, width=5)
item_qty.place(x=475, y=50)
label = tk.Label(master=sel_frame, text="qty", font=('Time','10'), bg=bg_one)
label.place(x=450, y=50)

# Item qty Entry spinbox
item_qty2 = tk.Spinbox(master=sel_frame, from_= 0, to=5, width=5)
item_qty2.place(x=475, y=100)
label = tk.Label(master=sel_frame, text="qty", font=('Time','10'), bg=bg_one)
label.place(x=450, y=100)

# Item qty Entry spinbox
item_qty3 = tk.Spinbox(master=sel_frame, from_= 0, to=5, width=5)
item_qty3.place(x=475, y=150)
label = tk.Label(master=sel_frame, text="qty", font=('Time','10'), bg=bg_one)
label.place(x=450, y=150)

# Submit button. Will call both quantity and total functions displaying calculated
# Data in sum_frame 
button1 = tk.Button(master=sel_frame,
                    text= "Submit",
                    width= 25,
                    command= lambda:[quantity(), total()]
                    )
button1.place(x=300, y=200)

# Clear Order button. will call both functions to clear the comboboxes and
# the spinboxes
button2 = tk.Button(master=sel_frame,
                    text= "Clear Order",
                    width= 25,
                    command= lambda:[clear_qty(), clear_sel()]
                    )
button2.place(x=120, y=200)

# -----Itemized Totals in sum_frame---- #
# Sandwiches number and total
label = tk.Label(master=sum_frame, 
                 text="Sandwiches",
                 font=('Helvetica', '12', 'bold', 'italic'),
                 bg=d_grey,
                 foreground='white')
label.place(x=5, y=75)
sandwich = tk.Label(master=sum_frame, 
                    text="0", 
                    width=10,
                    bg=d_grey,
                    foreground='white')
sandwich.place(x=110, y=75)

sand_price = tk.Label(master=sum_frame, 
                      text="0", 
                      width=10,
                      bg=d_grey,
                      foreground='white')
sand_price.place(x=110, y=100)

# Chips number and total
label = tk.Label(master=sum_frame, 
                 text="Chips",
                 font=('Helvetica', '12', 'bold', 'italic'),
                 bg=d_grey,
                 foreground='white')
label.place(x=5, y=125)
chips = tk.Label(master=sum_frame, 
                    text="0", 
                    width=10,
                    bg=d_grey,
                    foreground='white')
chips.place(x=110, y=125)

chips_price = tk.Label(master=sum_frame, 
                      text="0", 
                      width=10,
                      bg=d_grey,
                      foreground='white')
chips_price.place(x=110, y=150)

# Drinks number and total
label = tk.Label(master=sum_frame, 
                 text="Drinks",
                 font=('Helvetica', '12', 'bold', 'italic'),
                 bg=d_grey,
                 foreground='white')
label.place(x=5, y=175)
drinks = tk.Label(master=sum_frame, 
                    text="0", 
                    width=10,
                    bg=d_grey,
                    foreground='white')
drinks.place(x=110, y=175)

drinks_price = tk.Label(master=sum_frame, 
                      text="0", 
                      width=10,
                      bg=d_grey,
                      foreground='white')
drinks_price.place(x=110, y=200)

# Total
label = tk.Label(master=sum_frame, 
                 text="Total",
                 font=('Helvetica', '12', 'bold', 'italic'),
                 bg=d_grey,
                 foreground='white')
label.place(x=5, y=225)

order_total = tk.Label(master=sum_frame, 
                    text="0", 
                    width=10,
                    bg=d_grey,
                    foreground='white')
order_total.place(x=110, y=225)




window.mainloop()
