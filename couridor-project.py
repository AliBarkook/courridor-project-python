import msvcrt # ? for get movement from keyboard button:

boardMap = [ [ '.' for i in range(17) ] for j in range(17) ]

firstPlayerPlace = [0,8]
secondPlayerPlace = [16,8]
boardMap[firstPlayerPlace[0]][firstPlayerPlace[1]] = '1'
boardMap[secondPlayerPlace[0]][secondPlayerPlace[1]] = '2'


def initialMap():
    for i,row in enumerate(boardMap):
        if (i % 2 == 1):
            boardMap[i] = [' ']*17
            continue
            
        for index,col in enumerate(row):
            if (index % 2 == 1):
                boardMap[i][index] = ' '

def printMap() :
    for i in range(19):
        print('#', end='')

    print('')

    for row in boardMap:
        print('#', end='')
        for col in row:
            print(col, end='')
        print('#', end=' ')
        print('')


    for i in range(19):
        print('#', end='')

def movement(player):

    while(True):
        print('select t(trap) or m(move)')
        movementType = msvcrt.getch() 

        if movementType == b'm':

            while(True):
                print("enter 'w','d','s','a' key to move:")

                move = (msvcrt.getch()) # ? get movement from keyboard button:

                selectedPlayerPlace = [0,0]
                selectedPlayer = '0'

                if (player == 'first'):
                    selectedPlayerPlace = firstPlayerPlace
                    selectedPlayer = '1'
                else:
                    selectedPlayerPlace = secondPlayerPlace
                    selectedPlayer = '2'

                boardMap[selectedPlayerPlace[0]][selectedPlayerPlace[1]] = '.'

                if move == b'w' and selectedPlayerPlace[0]>1:
                    selectedPlayerPlace[0] -= 2
                    boardMap[selectedPlayerPlace[0]][selectedPlayerPlace[1]] = selectedPlayer
                    break
                elif move == b'd' and selectedPlayerPlace[1]<15:
                    selectedPlayerPlace[1] += 2
                    boardMap[selectedPlayerPlace[0]][selectedPlayerPlace[1]] = selectedPlayer
                    break
                elif move == b's' and selectedPlayerPlace[0]<15:
                    selectedPlayerPlace[0] += 2
                    boardMap[selectedPlayerPlace[0]][selectedPlayerPlace[1]] = selectedPlayer
                    break
                elif move == b'a' and selectedPlayerPlace[1]>1:
                    selectedPlayerPlace[1] -= 2
                    boardMap[selectedPlayerPlace[0]][selectedPlayerPlace[1]] = selectedPlayer
                    break
                else:
                    print('invalid move!')
            break

        elif movementType == b't':

            while(True):
                trapPlace = (input('enter cordinate(ex: 0 1) to place trap:')).split(' ')
                trapPlace = list(map(int, trapPlace))
                if (trapPlace[0]>-1 and trapPlace[1]>-1 and trapPlace[0]<17 and trapPlace[1]<17 and trapPlace[0]%2 == 0 and trapPlace[1]%2 == 1):
                    boardMap[trapPlace[0]][trapPlace[1]] = '|'
                    break
                elif (trapPlace[0]>-1 and trapPlace[1]>-1 and trapPlace[0]<17 and trapPlace[1]<17 and trapPlace[0]%2 == 1 and trapPlace[1]%2 == 0):
                    boardMap[trapPlace[0]][trapPlace[1]] = '-'
                    break
                else:
                    print('invalid cordinate!')
            break

        else:
            print('invalid input!')



print('couridor game is runnig')

firstPalyer = input('enter fist player name:')
secondPalyer = input('enter second player name:')

initialMap()

printMap()

while(True):
    print('')
    print(firstPalyer, 'turn:')
    movement('first')
    printMap()
    
    if (firstPlayerPlace[0] == 16):
        print('firstPlayer won the game!')
        break

    print('')
    print(secondPalyer, 'turn:')
    movement('second')
    printMap()

    if (secondPlayerPlace[0] == 0):
        print('secondPlayer won the game!')
        break
