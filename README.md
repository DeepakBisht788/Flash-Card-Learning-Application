# Flashy - A Language Learning Flashcard App

Flashy is a Python-based flashcard application designed to help you learn new words in a fun and interactive way. The app displays words in French (or any other target language) on flashcards, allowing you to test your knowledge and track progress by saving words to revisit later.

## Features

- **Interactive Flashcards**: Displays a word in the target language (e.g., French) and flips to show the English translation after a few seconds.
- **Customizable Word Sets**: Start with a default word set or continue with a personalized set of words you need to learn (`words_to_learn.csv`).
- **Progress Tracking**: Mark words you know, and the app saves unknown words for future review.
- **User-Friendly Interface**: Built with `Tkinter`, featuring visually appealing card designs and intuitive buttons.

## Prepare Image Files:
**Ensure the following image files are in the same directory as the script:**

- `card_front.png` (Front of the flashcard)
- `card_back.png` (Back of the flashcard)
- `wrong.png` (Cross button image)
- `right.png` (Tick button image)

## Prepare Word Files:
- **Include french_words.csv in the directory. This should be a CSV file with "French" and "English" columns. If the app runs before creating words_to_learn.csv, it will automatically generate one.

## How to Use
- **Click the Right button if you know the word. It will remove the word from your review list.
- **Click the Wrong button if you don’t know the word. It will keep the word in your review list.
- **Flashcards flip automatically after a few seconds to show the English translation.
