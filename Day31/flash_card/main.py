from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
curr_word={}
timer = None

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/hungarian_words.csv")
finally:
    words = data.to_dict('records')


# --------------------------RANDOM WORD-------------------------------- #
def next_word():
    global curr_word

    curr_word = random.choice(words)
    canvas.itemconfig(title, text="Hungarian", fill="black")
    canvas.itemconfig(word, text=curr_word["Hungarian"], fill="black")
    canvas.itemconfig(canvas_card, image=front_img)
    global timer
    timer=window.after(3000, card_back)


def right_word():
    global curr_word
    global words
    try:
        words.remove(curr_word)
    except ValueError:
        pass
    finally:
        new_data = pandas.DataFrame(words)
        new_data.to_csv("data/words_to_learn.csv", index=False)
        next_word()



def card_back():
    global curr_word
    canvas.itemconfig(canvas_card, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=curr_word["English"], fill="white")
    global timer
    window.after_cancel(timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# images
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_card = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_btn.grid(row=1, column=0)
right_btn = Button(image=right_img, highlightthickness=0, command=right_word)
right_btn.grid(row=1, column=1)


window.mainloop()
