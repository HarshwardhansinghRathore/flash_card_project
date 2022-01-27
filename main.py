from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# --------FUNCTIONS----------#


def change_fr_to_eng(item):
    eng_word = item['English']
    canvas.itemconfig(front_page, image=back_image)
    canvas.itemconfig(above_text, text='English')
    canvas.itemconfig(below_text, text=eng_word)


def wrong_button():

    item = choice(dict_data)
    canvas.itemconfig(front_page, image=front_image)
    canvas.itemconfig(above_text, text='French')
    fr_word = item['French']
    canvas.itemconfig(below_text, text=fr_word)
    canvas.after(3000, change_fr_to_eng, item)


def right_button():
    item = choice(dict_data)
    canvas.itemconfig(front_page, image=front_image)
    canvas.itemconfig(above_text, text='French')
    fr_word = item['French']
    canvas.itemconfig(below_text, text=fr_word)
    canvas.after(3000, change_fr_to_eng, item)

    dict_data.remove(item)
    words_to_learn_data = pandas.DataFrame(dict_data)
    words_to_learn_data.to_csv('words_to_learn.csv', index=False)


# -----------WINDOW----------#
window = Tk()
window.title('flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----------CARD FRONT-------#
# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)

# creating image on canvas
front_image = PhotoImage(file='images\\card_front.png')
back_image = PhotoImage(file='images\\card_back.png')
front_page = canvas.create_image(400, 263, image=front_image)

# creating text
above_text = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
below_text = canvas.create_text(400, 263, text='Trouve', font=('Arial', 60, 'bold'))


# creating buttons

# wrong button
wrong_image = PhotoImage(file='images\\wrong.png')
wrong_mark_button = Button(image=wrong_image, command=wrong_button, highlightthickness=0, height=99, width=100)
wrong_mark_button.grid(row=1, column=0)

# check button
check_image = PhotoImage(file='images\\right.png')
check_mark_button = Button(image=check_image, command=right_button, highlightthickness=0, height=99, width=100)
check_mark_button.grid(row=1, column=1)

# opening csv data
try:
    data = pandas.read_csv('words_to_learn.csv')
    dict_data = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv('data\\french_words.csv')
    dict_data = data.to_dict(orient='records')

# griding canvas
canvas.grid(row=0, column=0, columnspan=2)


mainloop()
