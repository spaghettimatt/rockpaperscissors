from random import randint as ran

def rockPaperScissors():
    com = ran(0, 2)
    gamerChoice = input('Pick Rock Paper or Scissors: \n')
    comStr = ['Rock', 'Paper', 'Scissors']
    epic = comStr[com]
    if gamerChoice == epic:
        print('They Chose {}!'.format(epic))
        q = input('Tie \nReplay? y/n: ')
        if q == 'y':
            rockPaperScissors()
        else:
            quit
    if gamerChoice == 'Rock':
        if epic == 'Scissors':
            q = input('You Win! \nReplay? y/n: ')
            if q == 'y':
                rockPaperScissors()
            else:
                quit
        elif epic == 'Paper':
            print('They Chose {}!'.format(epic))
            q = input('You Lose! \nReplay? y/n: ')
            if q == 'y':
                rockPaperScissors()
            else:
                quit
    elif gamerChoice == 'Paper':
        if epic == 'Rock':
            q = input('You Win! \nReplay? y/n: ')
            if q == 'y':
                rockPaperScissors()
            else:
                quit
        elif epic == 'Scissors':
            print('They Chose {}!'.format(epic))
            q = input('You Lose! \nReplay? y/n: ')
            if q == 'y':
                rockPaperScissors()
            else:
                quit
    elif gamerChoice == 'Scissors':
        if epic == 'Rock':
            print('They Chose {}!'.format(epic))
            q = input('You Lose! \nReplay? y/n: ')
            if q == 'n':
                rockPaperScissors()
            else:
                quit
        elif epic == 'Paper':
            q = input('You Win! \nReplay? y/n: ')
            if q == 'y':
                rockPaperScissors()
            else:
                quit
    else:
        q = input('Invalid Choice \n Replay? y/n: ')
        if q == 'y':
            rockPaperScissors()
        else:
            quit
rockPaperScissors()