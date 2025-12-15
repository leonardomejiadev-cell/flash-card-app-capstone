from tkinter import *
from tkinter import messagebox
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# Global variables for state management
current_card = {}
to_learn = {}

# ---------------------------- DATA MANAGEMENT ------------------------------- #

try:
    # Attempt to load the user's progress file
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    # If file is missing or empty (first run or reset), load the original dataset
    original_data = pandas.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # If progress file exists, load it
    to_learn = data.to_dict(orient="records")

    # Safety check: If the file exists but has no words left (game finished previously)
    if len(to_learn) == 0:
        original_data = pandas.read_csv("data/english_words.csv")
        to_learn = original_data.to_dict(orient="records")


# ---------------------------- CARD FUNCTIONS ------------------------------- #

def next_card():
    """Selects a random word and updates the UI to show the English side."""
    global current_card, flip_timer

    # Cancel the previous timer to prevent unwanted flips
    window.after_cancel(flip_timer)

    # Select a random dictionary from the list
    current_card = random.choice(to_learn)

    # Update Canvas UI for the Front Side (English)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["english"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # Set a new timer to flip the card after 3000ms (3 seconds)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Updates the UI to show the Spanish translation (Back Side)."""
    canvas.itemconfig(card_title, text="Spanish", fill="white")
    canvas.itemconfig(card_word, text=current_card["spanish"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """
    Removes the current card from the deck and saves progress.
    Triggered when the user clicks the check button.
    """
    to_learn.remove(current_card)

    # Save the updated list to CSV (excluding index numbers)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    # Check if the user has learned all words
    if len(to_learn) == 0:
        window.after_cancel(flip_timer)
        messagebox.showinfo(title="Congratulations!", message="You've learned all the words! The course is complete.")
        window.destroy()
    else:
        next_card()


# ---------------------------- UI SETUP ------------------------------- #

# Window Configuration
window = Tk()
window.title("Flashy - Language Learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize the timer with a placeholder (will be canceled immediately by next_card)
flip_timer = window.after(3000, func=flip_card)

# Canvas Configuration
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Set initial image
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Text Elements
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(row=1, column=1)

# Start the game logic
next_card()

# Main Loop
if __name__ == "__main__":
    window.mainloop()
