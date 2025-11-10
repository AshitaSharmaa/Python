
from pandas.core.interchange.dataframe_protocol import DataFrame
from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient ="records")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_back_image)

def known_card():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg = BACKGROUND_COLOR,padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400,153, text= "", font=("Ariel", 40, "italic"), fill = "black")
card_word = canvas.create_text(400,263, text= "", font=("Ariel", 60, "bold"), fill = "black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command = next_card)
cross_button.grid(row = 1, column = 0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command = known_card)
right_button.grid(row = 1, column = 1)



next_card()



window.mainloop()

