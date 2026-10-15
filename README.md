# 🎯 Number Guessing Game

A command-line number guessing game developed in **Python**, where players must guess a randomly generated number between 1 and 100.

This project was developed as part of the [Number Guessing Game Challenge](https://roadmap.sh/projects/number-guessing-game) from **roadmap.sh**, with the goal of practicing Python fundamentals, loops, conditional statements, and game logic.

## 🚀 Features

- **Random Number Generation:** Generates a random number between 1 and 100 for each round.
- **Three Difficulty Levels:** Choose between Easy, Medium, and Hard.
- **Hints:** Receive feedback indicating whether the secret number is higher or lower than your guess.
- **Attempt Tracking:** Counts the number of guesses made during each round.
- **High Score System:** Tracks the fewest attempts needed to win at each difficulty level.
- **Multiple Rounds:** Play as many rounds as you want without restarting the program.
- **Exit Option:** Leave the game through the main menu.

## 🎮 Difficulty Levels

| Difficulty | Maximum Attempts |
|------------|------------------|
| 🟢 Easy | 10 |
| 🟡 Medium | 5 |
| 🔴 Hard | 3 |

Each difficulty level generates a new random number between 1 and 100.

## 🛠️ Technologies Used

- **Python 3.10+**
- **random module** — Random number generation.
- **match-case** — Difficulty selection and menu navigation.
- **Loops (`while`, `for`)** — Game flow and attempt management.
- **Conditional statements (`if`, `elif`, `else`)** — Guess verification and ranking logic.
- **Lists** — High score storage.

No external dependencies are required.

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/ViniciusCoelh0/Number-Guessing-Game.git
```

**2. Navigate to the project directory**

```bash
cd YOUR_REPOSITORY
```

**3. Run the game**

```bash
python main.py
```

Make sure Python 3.10 or higher is installed.

## 💻 How to Play

When you start the game, the following menu will appear:

```text
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.

Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    4. Ranking
    5. Leave
```

Select a difficulty level and enter your guesses until you find the correct number or run out of attempts.

### Example Gameplay

```text
Great! You have selected the Easy difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is greater than 50.

Enter your guess: 75
Incorrect! The number is less than 75.

Enter your guess: 63
Congratulations! You guessed the correct number in 3 attempts.
```

### Losing a Round

If you run out of attempts, the game reveals the correct number.

```text
Sorry! You didn't guess the correct number.
The correct number was 42.
```

After each round, the game returns to the main menu.

## 🏆 High Score System

The game includes a ranking system that tracks the best performance for each difficulty level.

A player's best score is determined by the **fewest attempts needed to guess the correct number**.

### Example Scoreboard

```text
BEST ATTEMPTS SCOREBOARD

| Difficulty | Attempts |
|------------|----------|
| 🟢 Easy    |     3    |
| 🟡 Medium  |     2    |
| 🔴 Hard    |     1    |
```

### Ranking Rules

- Each difficulty level has its own record.
- Only successful rounds count toward the ranking.
- A lower number of attempts represents a better score.
- Losing a round does not affect existing records.
- Scores are stored in memory and reset when the program closes.
- A score of `0` indicates that no successful round has been recorded.

## 📚 What I Learned

Through this project, I practiced:

- Generating random numbers using `randint()`.
- Implementing interactive menus with `match-case`.
- Using `while` and `for` loops to control program execution.
- Managing conditional logic with `if`, `elif`, and `else`.
- Tracking attempts using variables.
- Storing and updating records using lists.
- Implementing replay functionality.
- Using `break` to control loops.
- Organizing a command-line application.



## 🔗 Project Reference

This project is based on the **Number Guessing Game** challenge from roadmap.sh.

**Challenge URL:** https://roadmap.sh/projects/number-guessing-game

## 📄 License

This project is available for educational and learning purposes.