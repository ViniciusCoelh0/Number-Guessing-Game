# 🎯 Number Guessing Game

A simple command-line number guessing game developed in **Python**, where players must guess a randomly generated number between 1 and 100.

This project was developed as part of the [Number Guessing Game Challenge](https://roadmap.sh/projects/number-guessing-game) from **roadmap.sh**.

The main goal is to practice Python fundamentals, including functions, loops, conditional statements, random number generation, and code organization.

## 🚀 Features

- **Random Number Generation:** Generates a new random number between 1 and 100 for each round.
- **Three Difficulty Levels:** Easy, Medium, and Hard.
- **Hint System:** Provides feedback indicating whether the secret number is higher or lower than the player's guess.
- **Attempt Counter:** Tracks the number of attempts made during each round.
- **High Score System:** Records the fewest attempts needed to win in each difficulty level.
- **Multiple Rounds:** Allows players to play repeatedly without restarting the program.
- **Exit Option:** Players can leave the game through the main menu.
- **Modular Code:** Uses reusable functions to organize the game logic and reduce code duplication.

## 🎮 Difficulty Levels

| Difficulty | Maximum Attempts |
|------------|------------------|
| 🟢 Easy | 10 |
| 🟡 Medium | 5 |
| 🔴 Hard | 3 |

Each difficulty level uses the same game logic, with a different maximum number of attempts.

## 🛠️ Technologies Used

- **Python 3.10+**
- **random module** — Generates random numbers.
- **Functions** — Organize reusable game logic.
- **match-case** — Handles menu navigation.
- **Loops (`while`, `for`)** — Control game execution.
- **Conditional statements** — Evaluate guesses and update records.
- **Lists** — Store high scores for each difficulty.

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

When the game starts, the following menu appears:

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

Select a difficulty level and enter your guesses.

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

If the player runs out of attempts, the correct number is revealed.

```text
Sorry! You didn't guess the correct number.
The correct number was 42.
```

After each round, the game returns to the main menu.

## 🏆 High Score System

The game tracks the best performance for each difficulty level.

The best score is determined by the **fewest attempts needed to guess the correct number**.

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

- Each difficulty level has an independent record.
- Only successful rounds count toward the ranking.
- A lower number of attempts represents a better score.
- Losing a round does not affect existing records.
- Scores are stored in memory and reset when the program closes.
- A score of `0` indicates that no successful round has been recorded.

## 🧩 Code Structure

The project uses functions to separate responsibilities and improve code readability.

| Function | Description |
|----------|-------------|
| `starting()` | Generates and returns a random number between 1 and 100. |
| `play()` | Controls the game loop, tracks attempts, and checks win/loss conditions. |
| `atempet()` | Provides hints based on the player's guess. |
| `result()` | Displays the victory message and updates the high score. |
| `lose()` | Displays the defeat message and reveals the correct number. |

### Game Flow

```text
Start
  |
  v
Main Menu
  |
  +-- Easy (10 attempts)
  |
  +-- Medium (5 attempts)
  |
  +-- Hard (3 attempts)
  |       |
  |       v
  |   Generate Random Number
  |       |
  |       v
  |   Start Game
  |       |
  |       v
  |   Enter Guess
  |       |
  |       +-- Correct --> Update Ranking
  |       |
  |       +-- Incorrect --> Show Hint
  |                             |
  |                             +-- Attempts left --> Try Again
  |                             |
  |                             +-- No attempts --> Game Over
  |
  +-- Ranking --> Display Best Scores
  |
  +-- Leave --> Exit Program
```

## 📚 What I Learned

During the development of this project, I practiced:

- Generating random numbers using `randint()`.
- Creating and calling functions with parameters.
- Understanding local variables and function scope.
- Working with mutable data structures such as lists.
- Using `match-case` for menu navigation.
- Controlling program execution with loops and `break`.
- Implementing a high score system.
- Refactoring repetitive code into reusable functions.
- Separating responsibilities to improve maintainability.

## 🔗 Project Reference

This project was developed based on the **Number Guessing Game** challenge from roadmap.sh.

**Challenge:** https://roadmap.sh/projects/number-guessing-game

## 📄 License

This project is available for educational and learning purposes.
