def starting():
    from random import randint
    rand = randint(1,100)
    return rand

def play(chances, pos, rand, tot):
    totA = 0
    for c in range(0, chances):
        cho = int(input('Enter your guess: '))
        totA+=1
        atempet(cho, rand)
    
        if cho == rand:
            result(tot, pos, totA)
            break
        elif totA == chances:
            lose(rand)    
            break

def atempet(cho, rand):
    if cho > rand:
        print(f'Incorrect! The number is less than {cho}.')
    elif cho < rand:
        print(f'Incorrect! The number is greater than {cho}')

def result(tot, pos, totA):
    print(f'Congratulations! You guessed the correct number in {totA} attempts.')
    print()
    if tot[pos] == 0 or tot[pos] >= totA:
        tot[pos] = totA

def lose(rand):
    print(f"Sorry! You didn't guess the correct number. The correct number was {rand}.")
    print()

tot = [0,0,0]

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
            pos = cho-1
            chances = 10
            rand = starting()
            print('''Great! You have selected the Easy difficulty level.
Let's start the game!
''')
            play(chances, pos, rand, tot)

        case 2:
            pos = cho-1
            chances = 5 
            rand = starting()
            print('''Great! You have selected the Medium difficulty level.
Let's start the game!
            ''')
            
            play(chances, pos, rand, tot)

        case 3:
            pos = cho-1
            chances = 3
            rand = starting()
            print('''Great! You have selected the Hard difficulty level.
Let's start the game!
                ''')
            
            play(chances, pos, rand, tot)

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
