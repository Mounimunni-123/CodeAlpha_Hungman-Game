Hangman Game in Python

📌 Project Overview

The Hangman Game is a classic word-guessing game implemented in Python.
The player tries to guess the hidden word one letter at a time.
For every wrong guess, a part of the hangman figure is drawn.
The game ends when the player either guesses the correct word or the hangman figure is completely drawn.


---

🧠 Game Rules

1. A random word is chosen from a list of predefined words.


2. The player guesses letters one at a time.


3. Each correct letter is revealed in its correct position.


4. Each incorrect guess reduces the number of lives.


5. The player wins if the word is guessed before running out of lives.


6. The player loses if all lives are used up.




---

⚙️ Features

✅ Random word selection
✅ Keeps track of guessed letters
✅ Displays progress after each guess
✅ Text-based user interface (console)
✅ Handles repeated and invalid inputs


---

🧩 Requirements

To run this project, you need:

Python 3.x

A text editor (like VS Code, PyCharm, or IDLE)



---

🚀 How to Run

1. Clone or Download the project folder.


2. Open the project in VS Code or any Python IDE.


3. Run the file using:

python hangman.py


4. Follow the on-screen instructions to play.




---

💡 Example Output

Welcome to Hangman!
_ _ _ _ _
Guess a letter: a
Correct!
a _ _ _ _
Lives remaining: 6

Guess a letter: e
Wrong guess!
Lives remaining: 5


---

🧱 File Structure

hangman/
│
├── hangman.py         # Main game logic
├── words.py           # Word list file (optional)
└── README.md          # Project description


---

✨ Future Enhancements

Add graphical interface (using Tkinter or Pygame)

Allow custom word input

Add difficulty levels



---

👩‍💻 Author

Your Name Mounimunni-123
Python Developer | Project: Hangman Game
