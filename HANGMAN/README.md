#  Hangman — Classic Python Game with ASCII Art

A simple **Hangman** game written in **pure Python**, using ASCII art to show the hangman as you guess wrong letters.

---

##  **About This Project**

-  **Beginner-Friendly:** Uses only core Python — no external libraries.
-  **Visual:** Displays classic hangman figure in ASCII as you play.
-  **Modular:** Clear functions for word selection and game loop.
-  **Documented:** Code includes step-by-step TODOs so you can follow the logic and learn.
-  **Fun:** Random words every round.

---

##  **How It Works**

1. **Word Selection:**  
   The game picks a random word from a predefined list.

2. **ASCII Art:**  
   The game uses a list of ASCII art stages. Each incorrect guess progresses the hangman.

3. **User Input:**  
   The player inputs letters. Correct guesses reveal letters; wrong guesses draw more of the hangman.

4. **Game Over:**  
   The player wins if they guess all letters. They lose if the hangman is fully drawn.

---

##  **How to Run**

```bash
python hangman.py
