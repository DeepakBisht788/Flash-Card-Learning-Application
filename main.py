from tkinter import *
import tkinter as t
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
screen=Tk()
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
screen.title("Flashy")
Dict={}
current_card={}
try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
    Dict = data.to_dict(orient="records")
else:
    Dict=data.to_dict(orient="records")


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def next_card():
    global current_card,timer
    screen.after_cancel(timer)
    current_card=random.choice(Dict)
    french=(current_card["French"])
    english=(current_card["English"])
    canvas.itemconfig(card_title, text="french", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=card_front)
    timer=screen.after(5000, func=flip_card)
timer=screen.after(5000, func=flip_card)
def is_know():
    Dict.remove(current_card)
    next_card()
    data=pandas.DataFrame(Dict)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()
# image
canvas= Canvas(width=800, height=526,highlightthickness=0)
card_front= PhotoImage(file="card_front.png")
card_back= PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title=canvas.create_text(400,150,text="Title", font=("Ariel",30,"italic"))
card_word=canvas.create_text(400,263,text="Word", font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0, columnspan=2)

# button
cross=PhotoImage(file="wrong.png")
wrong=Button(image=cross, highlightthickness=0,command=next_card)
wrong.grid(row=1,column=0)

right=PhotoImage(file="right.png")
tick=Button(image=right, highlightthickness=0,command=is_know)
tick.grid(row=1,column=1)


next_card()


















screen.mainloop()