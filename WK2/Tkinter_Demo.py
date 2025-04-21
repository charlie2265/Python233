# Program:      Lesson 2 Calorie Counter
# Programmer:   Charlie
# Date:         4/7/2025
# Purpose:      Demo for Tkinter. 
import tkinter as tk

def calc_cals():
    g_carbs = int(ent_carbs.get())
    g_fats = int(ent_fats.get())
    g_protien = int(ent_protien.get())

    i_cal = g_carbs * 4 + g_fats * 9 + g_protien * 4
    lbl_item_cals["text"] = f"{i_cal}"

    tot_cals = int(lbl_total_cals["text"])
    tot_items = int(lbl_total_items["text"])
    
    tot_cals += i_cal
    tot_items += 1

    lbl_total_cals["text"] = f"{tot_cals}"
    lbl_total_items["text"] = f"{tot_items}"



window = tk.Tk()
window.title("Calorie Counter")

frame1_bg = "grey90"
frame1 = tk.Frame(master=window, width=400, height=400, bg=frame1_bg)
frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=200, height=400, bg="grey")
frame2.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, height=400, bg="black")
frame3.pack(fill=tk.Y, side=tk.LEFT, expand=True)

# Frame 1 Layout
label = tk.Label(master=frame1,                 
                 text=("Charlie's Calorie Counter"),
                 bg="grey",
                 font=("Time", "18", "italic"))
label.place(x=20, y=0)

# data input 
label = tk.Label(master=frame1, text="Please enter Item Name", bg=frame1_bg)
label.place(x=0, y=40)
ent_name = tk.Entry(master=frame1, width=40)
ent_name.place(x=165, y=40)

label = tk.Label(master=frame1, text="Please enter grams of carbs", bg=frame1_bg)
label.place(x=0, y=80)
ent_carbs = tk.Entry(master=frame1, width=10)
ent_carbs.place(x=165, y=80)

label = tk.Label(master=frame1, text="Please enter fats", bg=frame1_bg)
label.place(x=0, y=105)
ent_fats = tk.Entry(master=frame1, width=10)
ent_fats.place(x=165, y=105)

label = tk.Label(master=frame1, text="Please enter grams of protien", bg=frame1_bg)
label.place(x=0, y=130)
ent_protien = tk.Entry(master=frame1, width=10)
ent_protien.place(x=165, y=130)

# button
button1 = tk.Button(master=frame1,
                    text= "Submit",
                    width= 60,
                    command=calc_cals
                    )
button1.place(x=0, y=200)

# frame 2
label = tk.Label(master=frame2, text="Totals", bg="grey",
                 font=("Times","16","bold"))
label.place(x=10, y=20)

# item cals
label = tk.Label(master=frame2, text="Item Calories", bg="grey")
label.place(x=10, y=70)

lbl_item_cals = tk.Label(master=frame2, text="0", width=10)
lbl_item_cals.place(x=100, y=70)

# total cals
label = tk.Label(master=frame2, text="Total Calories", bg="grey")
label.place(x=10, y=100)

lbl_total_cals = tk.Label(master=frame2, text="0", width=10)
lbl_total_cals.place(x=100, y=100)

# total items
label = tk.Label(master=frame2, text="Total Items", bg="grey")
label.place(x=10, y=130)

lbl_total_items = tk.Label(master=frame2, text="0", width=10)
lbl_total_items.place(x=100, y=130)




window.mainloop()













# import tkinter as tk

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=100, height=100, bg='red')
# frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)

# frame2 = tk.Frame(master=window, width=50, height=50, bg='yellow')
# frame2.pack(fill=tk.X, side=tk.LEFT, expand=True)


# frame3 = tk.Frame(master=window, width=25, height=25, bg='blue')
# frame3.pack(fill=tk.Y, side=tk.RIGHT, expand=True)


# window.mainloop()








# from tkinter import *
# root = Tk()
# theLabel = Label(root, text="This is too easy")
# theLabel.pack()

# label = Label(root, text="This is line 2")
# label.pack()

# label = Label(root, text="------------+++++++++================")
# label.pack()


# root.mainloop()








