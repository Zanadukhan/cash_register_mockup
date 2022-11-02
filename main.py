import pandas as pd
from tkinter import *
from PIL import ImageTk
from ttkwidgets.autocomplete import AutocompleteCombobox

GREEN = '#008000'
WEIGHT = 2.0





def register_entry():
    cart.create_text(0, 0, text=item_entry.get())

# -----Data-----#


fruit = pd.read_csv('fruit.csv')

fruit.set_index('fruit', inplace=True)

fruit_index = fruit.to_dict('index')

shopping_cart = []
price = []
cost = []

# ---Functions--#
product_list = []
total = 0.00
num_items = 0

for _ in fruit_index:
    product_list.append(_)


def left_text():
    for i, word in enumerate(shopping_cart):
        cart.create_text(
            (10, 20 + (i * 2) * 20),
            text=f'{word}', anchor=W, font=('Arial', 20))


def center_price():
    for i, v in enumerate(cost):
        cart.create_text(
            (167, 20 + (i * 2) * 20),
            text=f'(${v})', anchor=W, font=('Arial', 15))


def right_cost(num):
    for i, dollar in enumerate(cost):
        cart.create_text(
            (400, 20 + (i * 2) * 20),
            text=f'${round(dollar * num, 2)}', anchor=W, font=('Arial', 20))


def new_item(event=None):
    produce = item_entry.get()
    shopping_cart.append(produce)
    cost.append(fruit_index[produce]['price'])
    cart.delete('all')
    global prod_price
    prod_price = fruit_index[produce]['price']
    if fruit_index[produce]['weight']:
        left_text()
        center_price()
        right_cost(WEIGHT)
        global total
        total += prod_price * WEIGHT
        total_transaction.configure(text=f"Total:${round(total, 2)}")
    else:
        num_items()
    item_entry.delete(0, END)

def close_win(event=0):
    units_num = num_entry.get()
    left_text()
    center_price()
    right_cost(float(units_num))
    global total
    total += prod_price * WEIGHT
    total_transaction.configure(text=f"Total:${round(total, 2)}")
    popup.destroy()
def num_items():
    global popup
    popup = Toplevel()
    popup.geometry('450x100')

    option = Label(popup, text='How many units are being purchased?', font=('Ariel', 20, 'normal'))
    option.pack()


    global num_entry
    num_entry = Entry(popup, font=('Ariel', 25))
    num_entry.pack()
    num_entry.bind('<Return>', close_win)
    num_entry.focus()
# ----UI--- #

register = Tk()
register.title('Cash Register')
register.geometry('800x800')
register.config(bg='grey', pady=20, padx=5)

title = Label(text='Cash Register', font=('Ariel', 35, 'bold'), fg=GREEN)
title.place(anchor=NW)

item_entry = AutocompleteCombobox(width=25, font=('Ariel', 25), completevalues=product_list)
item_entry.focus()
item_entry.bind('<Return>', new_item)
item_entry.place(x=350, y=0, height=60)


cart = Canvas(width=500, height=600)
cart.place(x=0, y=70)


fruit_img = ImageTk.PhotoImage(file='fruit.jpg')
fruit = Canvas(width=250, height=600)
fruit.create_image(10, 300, image=fruit_img)
fruit.place(x=510, y=70)

weight = Label(text=f'Weight={WEIGHT} lbs', font=('Ariel', 20, 'normal'))
weight.place(x=0, y=680, width=230, height=90)

savings = Label(text="You've saved: $0.00", font=('Ariel', 20, 'normal'))
savings.place(x=240, y=680, width=230, height=90)

total_transaction = Label(text=f"Total:${total} ", font=('Ariel', 20, 'normal'))
total_transaction.place(x=480, y=680, width=300, height=90)


register.mainloop()