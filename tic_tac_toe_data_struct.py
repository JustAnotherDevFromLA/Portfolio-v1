import pprint

def printBoard(board):
    print(board ['top-L'] + '|'+ board ['top-M'] + '|'+ board ['top-R'])
    print(" ---")
    print(board ['mid-L'] + '|'+ board ['mid-M'] + '|'+ board ['mid-R'])
    print(" ---")
    print(board ['low-L'] + '|'+ board ['low-M'] + '|'+ board ['low-R'])

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ','mid-M': ' ',
            'mid-R': ' ','low-L': ' ','low-M': ' ','low-R': ' '}

theBoard['top-L'] = 'X'
theBoard['top-M'] = 'X'
theBoard['top-R'] = 'X'
theBoard['low-L'] = 'X'

printBoard(theBoard)

pprint.pprint(theBoard)

