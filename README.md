# 📇 Flash Card App - Capstone Project

A GUI-based desktop application designed to facilitate language learning using the **Spaced Repetition** technique. This project demonstrates data persistence, graphical user interface design, and robust error handling.

## 🎯 Project Overview

This application helps users learn the most frequent words in a new language (English-Spanish). It tracks the user's progress by removing known words from the study pool, ensuring efficient learning sessions. It was built as the Day 31 Capstone Project.

## ✨ Features

* **Interactive GUI:** Smooth card flipping animation and intuitive button controls
* **Data Persistence:** Automatically saves progress to a CSV file
* **Smart Session Management:** Loads previous progress and resets if all words are learned
* **Timer Mechanism:** Auto-flips cards after 3 seconds to reveal translations
* **Robust Error Handling:** Manages missing files or empty datasets gracefully

## 🛠️ Technologies Used

* Python 3.x
* **Tkinter** (GUI Toolkit)
* **Pandas** (Data Analysis Library)
* **Random Module** (Standard Library)

## 📂 Project Structure

```text
flash-card-app/
├── main.py              # Main application logic
├── data/
│   ├── english_words.csv    # Original dataset (source)
│   └── words_to_learn.csv   # User progress (generated)
├── images/
│   ├── card_front.png       # UI Assets
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── README.md            # Project documentation
```

## 🏗️ Key Concepts Implemented

The project focuses on three main technical areas:

**1. Pandas DataFrames**
* Reading CSV files into DataFrames
* Converting DataFrames to dictionaries (`orient="records"`) for easy iteration
* Saving updated datasets back to CSV to persist state

**2. Tkinter Canvas & Events**
* Using `Canvas` for layering images and text
* Implementing `window.after()` for the timer mechanism (non-blocking delays)
* Canceling scheduled events using `window.after_cancel()`

**3. Exception Handling**
* Using `try/except/else` blocks to handle `FileNotFoundError` and `pandas.errors.EmptyDataError` to ensure the app never crashes on startup

## 🚀 How to Run

1.  Clone this repository
2.  Ensure you have Python 3.x and Pandas installed:
    ```bash
    pip install pandas
    ```
3.  Run the program:
    ```bash
    python main.py
    ```

## 💡 Usage

1.  **The Card:** A word appears in English on a white card.
2.  **The Timer:** You have 3 seconds to guess the Spanish translation.
3.  **The Flip:** The card turns green and reveals the answer.
4.  **The Controls:**
    * ❌ (Red): You didn't know the word. It will appear again later.
    * ✅ (Green): You knew the word. It is removed from the list and saved to progress.

## 📚 What I Learned

* **GUI Event Loop:** How to manage timed events within a main loop without freezing the interface
* **Data Serialization:** Reading and writing structured data using Pandas is significantly more efficient than standard file I/O
* **Dynamic Typing:** Handling dynamic paths for file loading and image referencing

## 🔗 Related Projects

* **Password Manager** - Another GUI application focusing on JSON data management and security

## 👤 Author

**Leonardo Mejia**
* GitHub: [leonardomejiadev-cell](https://github.com/leonardomejiadev-cell)
* Learning Journey: 100 Days of Code - Python

## 📝 License

This project is part of my learning journey with Angela Yu's 100 Days of Code course.