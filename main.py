import pandas as pd
from tkinter import *
from PIL import ImageTk
from ttkwidgets.autocomplete import AutocompleteCombobox

GREEN = '#008000'



price = (2.00, 2.00, 2.00, 2.00)
register = Tk()
register.title('Cash Register')
register.geometry('800x800')
register.config(bg='grey', pady=20, padx=5)


def register_entry():
    cart.create_text(0, 0, text=item_entry.get())

#-----Data-----#

fruit = pd.read_csv('fruit.csv')

fruit.set_index('fruit', inplace=True)

fruit_index = fruit.to_dict('index')

print(fruit_index)

shopping_cart = []
cost = []

# ----UI--- #
product_list = []

for _ in fruit_index:
    product_list.append(_)

def new_item():
    shopping_cart.append(item_entry.get())
    cost.append(fruit_index[item_entry.get()]['price'])
    cart.delete('all')
    #adds a new item on the right side of the canvas
    for i, word in enumerate(shopping_cart):
        cart.create_text(
            (10, 20 + (i * 2) * 20),
            text=f'{word}', anchor=W, font=('Arial', 20))
    #adds the price of item to the left side of the canvas
    for i, dollar in enumerate(cost):
        cart.create_text(
            (450, 20 + (i * 2) * 20),
            text=f'{dollar}', anchor=W, font=('Arial', 20))
    item_entry.delete(0, END)



title = Label(text='My Grocery Store', font=('Ariel', 35, 'bold'), fg=GREEN)
title.place(anchor=NW)

item_entry = AutocompleteCombobox(width=25, font=('Ariel', 25), completevalues=product_list)
item_entry.focus()
item_entry.bind('<KP_Enter>', new_item())
item_entry.place(x=350, y=0, height=60)




cart = Canvas(width=500, height=600)
cart.place(x=0, y=70)



fruit_img = ImageTk.PhotoImage(file='fruit.jpg')
fruit = Canvas(width=250, height=600)
fruit.create_image(10, 300, image=fruit_img)
fruit.place(x=510, y=70)

weight = Label(text='Weight=2.0 lbs', font=('Ariel', 20, 'normal'))
weight.place(x=0, y=680, width=230, height=90)

savings = Label(text="You've saved: $0.00", font=('Ariel', 20, 'normal'))
savings.place(x=240, y=680, width=230, height=90)

total = Label(text="Total: placeholder", font=('Ariel', 20, 'normal'))
total.place(x=480, y=680, width=300, height=90)




register.mainloop()