import random


def tokenChoice():
    answer = ""
    while not (answer == 'X' or answer == 'O'):
        print("which token - x or o?")
        answer = input().upper()
    match answer:
        case 'X':
            return ['X', 'O']
        case 'O':
            return ['O', 'X']


def setBoard(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


def whoStarts():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def isItFree(board, move):
    return board[move] == ' '


def playerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isItFree(board, int(move)):
        print("input tile value")
        move = input()
    return int(move)


def computerMove(board, playerTok, compTok):
    for i in range(1, 10):
        copy = board[:]
        if isItFree(copy, i):
            makeMove(copy, i, compTok)
            if isWin(copy, compTok):
                return i

    for i in range(1, 10):
        copy = board[:]
        if isItFree(copy, i):
            makeMove(copy, i, playerTok)
            if isWin(copy, playerTok):
                return i

    move = randomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isItFree(board, 5):
        return 5

    return randomMove(board, [2, 4, 6, 8])


def randomMove(board, moveList):
    returnList = []
    for i in moveList:
        if isItFree(board, i):
            returnList.append(i)

    if (len(returnList) != 0):
        return random.choice(returnList)
    else:
        return None


def makeMove(board, move, tok):
    board[move] = tok


def isWin(board, tok):
    return (
            (board[1] == tok and board[2] == tok and board[3] == tok) or
            (board[4] == tok and board[5] == tok and board[6] == tok) or
            (board[7] == tok and board[8] == tok and board[9] == tok) or
            (board[1] == tok and board[4] == tok and board[7] == tok) or
            (board[2] == tok and board[5] == tok and board[8] == tok) or
            (board[3] == tok and board[6] == tok and board[9] == tok) or
            (board[1] == tok and board[5] == tok and board[9] == tok) or
            (board[3] == tok and board[5] == tok and board[7] == tok)
    )


def isBoardFull(board):
    for i in range(1, 10):
        if isItFree(board, i):
            return False
    return True


def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def main():
    print('tic-tac-toe')
    while True:
        playerToken, compToken = tokenChoice()
        mainBoard = [" "] * 10
        turn = whoStarts()
        print(turn)
        loopControl = True
        while loopControl:
            if turn == 'player':
                setBoard(mainBoard)
                move = playerMove(mainBoard)
                makeMove(mainBoard, move, playerToken)
                if isWin(mainBoard, playerToken):
                    setBoard(mainBoard)
                    print('player wins')
                    loopControl = False
                else:
                    if isBoardFull(mainBoard):
                        setBoard(mainBoard)
                        print('tie')
                        break
                    else:
                        turn = 'computer'

            else:
                move = computerMove(mainBoard, playerToken, compToken)
                makeMove(mainBoard, move, compToken)
                if isWin(mainBoard, compToken):
                    setBoard(mainBoard)
                    print('comp wins')
                    loopControl = False
                else:
                    if isBoardFull(mainBoard):
                        print('tie')
                        break
                    else:
                        turn = 'player'

        if not playAgain():
            break


if __name__ == '__main__':
    main()
