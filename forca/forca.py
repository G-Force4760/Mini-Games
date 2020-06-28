import random
import time

movies = ['inter stellar', 'end game', 'far from home']
music = ['sam the kid', 'emi nem', 'val ete']
games = ['cs go', 'dn d', 'mag ic']
possible = [movies, music, games]


while True:
    rounds = 10
    guess = []
    letter = []
    while True:
        n = input('Choose a theme! [1] Movies [2] Music [3] Games\n--> ').strip()
        if n == '1':
            tip = 'Movies'
            word = random.choice(movies)
            break
        elif n == '2':
            word = random.choice(music)
            tip = 'Music'
            break
        elif n == '3':
            word = random.choice(games)
            wordclass = possible[2]
            tip = 'Games'
            break
        else:
            print('Invalid! Try again!')
            continue
    for x in word:
        if x == ' ':
            print(' |', end='')
        else:
            print(' _', end='')
    while True:
        while True:
            print('\nTip:', tip)
            letter = input('Guess a letter: ').strip().lower()
            if letter in guess:
                print('That letter was already tried.')
                continue
            else:
                guess += letter
                break
        trying = ''
        for x in word:
            if x == ' ':
                print(' |', end='')
            elif x in guess:
                print(x, end='')
                trying += x
            else:
                print(' _', end='')
        rounds = 10
        for x in guess:
            if x not in word:
                rounds = rounds - 1
        print('\nGuesses: ',str(guess).replace('[','').replace(']', '').replace("'", ''))
        print('Rounds remaining: ',rounds)
        if rounds <= 0:
            time.sleep(0.5)
            print('You lost! The word was', word)
            break
        elif trying == str(word).replace(' ', ''):
            time.sleep(0.5)
            print('Congratulations! You won!')
            break
    again = input('Do you want to play again? [1] Yes [2] No\n').strip()
    if again == '1':
        continue
    else:
        break