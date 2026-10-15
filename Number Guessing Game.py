from random import randint

tot = [0,0,0]

totEasy = totMed = totHard =0

print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

while True:
    
    cho = int(input('''Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    4. Ranking
    5. Leave
    '''))

    match cho:
        case 1:
            rand = randint(1,100)
            print('''Great! You have selected the Easy difficulty level.
Let's start the game!
    ''')
            for c in range(0, 10):
                cho = int(input('Enter your guess: '))
                totEasy+=1
                if cho > rand:
                    print(f'Incorrect! The number is less than {cho}.')
                elif cho < rand:
                    print(f'Incorrect! The number is greater than {cho}')
                    
                if cho == rand:
                    print(f'Congratulations! You guessed the correct number in {totEasy} attempts.')
                    print()
                    if tot[0] == 0 or tot[0] >= totEasy:
                        tot[0] = totEasy
                        totEasy = 0
                        break
                    elif tot[0] < totEasy:
                        totEasy = 0
                        break
                elif totEasy == 10:
                    print(f"Sorry! You didn't guess the correct number. The correct number was {rand}.")
                    print()
                    totEasy = 0
                    break

        case 2:
            rand = randint(1,100)
            print('''Great! You have selected the Medium difficulty level.
Let's start the game!
            ''')
            for c in range(0, 5):
                cho = int(input('Enter your guess: '))
                totMed+=1
                if cho > rand:
                    print(f'Incorrect! The number is less than {cho}.')
                elif cho < rand:
                    print(f'Incorrect! The number is greater than {cho}')
                
                if cho == rand:
                    print(f'Congratulations! You guessed the correct number in {totMed} attempts.')
                    print()
                    if tot[1] == 0 or tot[1] >= totMed:
                        tot[1] = totMed
                        totMed = 0
                        break
                    elif tot[1] < totMed:
                            totMed = 0
                            break
                elif totMed == 5:
                    print(f"Sorry! You didn't guess the correct number. The correct number was {rand}.")
                    print()
                    totMed = 0
                    break

        case 3:
            rand = randint(1,100)
            print('''Great! You have selected the Hard difficulty level.
Let's start the game!
                ''')
            for c in range(0, 3):
                cho = int(input('Enter your guess: '))
                totHard+=1
                if cho > rand:
                    print(f'Incorrect! The number is less than {cho}.')
                elif cho < rand:
                    print(f'Incorrect! The number is greater than {cho}')
                
                if cho == rand:
                    print(f'Congratulations! You guessed the correct number in {totHard} attempts.')
                    print()
                    if tot[2] == 0 or tot[2] >= totHard:
                        tot[2] = totHard
                        totHard = 0
                        break
                    elif tot[2] < totHard:
                        totHard = 0
                        break
                elif totHard == 3:
                    print(f"Sorry! You didn't guess the correct number. The correct number was {rand}.")
                    print()
                    totHard = 0
                    break

        case 4:
            print('BEST ATTEMPTS SCOREBOARD')
            print(f'''
| Difficulty | Attempts |
|------------|----------|
| 🟢 Easy    | {tot[0]:>5}    |
| 🟡 Medium  | {tot[1]:>5}    |
| 🔴 Hard    | {tot[2]:>5}    |
''')
        
        case 5:
            break