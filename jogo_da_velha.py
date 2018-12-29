theboard = { 'top-L':' ','top-M':' ','top-R':' ',
             'mid-L':' ','mid-M':' ','mid-R':' ',
             'low-L':' ','low-M':' ','low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theboard)
    print('Turn for ' + turn + '. Mova-se em qual espaço?')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theboard)
