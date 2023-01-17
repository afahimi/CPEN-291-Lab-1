# group number: G16
# student names: Greg Berezhnov, Amraj Aujla, Amin Fahiminia, Navraj Bains

import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played)
            and prints the banner messages
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell,
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        print(
        """
         {0} | {1} | {2}   0 | 1 | 2
        ---+---+--- ---+---+---
         {3} | {4} | {5}   3 | 4 | 5
        ---+---+--- ---+---+---
         {6} | {7} | {8}   6 | 7 | 8
           
        """.format(self.board[0],self.board[1],self.board[2],self.board[3],self.board[4],self.board[5],self.board[6],self.board[7],self.board[8])
        )

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number;
            error checks that the input is a valid cell number;
            and prints the info and the updated self.board;
        """
        while True:
            #init user prompt
            userMove = input("Enter next player move (0-8): ")

            #checks for valid user cell input
            if not userMove.isdigit() :
                print("Input is not an integer")
            elif not (int(userMove) >= 0 and int(userMove) < 9) :
                print("Enter a valid cell between 0 and 8")
            else:
                #place an X in the selected cell if it is empty
                if self.board[int(userMove)] == ' ':
                    self.board[int(userMove)] = 'X'
                    break
                else:
                    print("Cell is not empty")

        self.printBoard()
    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell,
            and prints the info and the updated self.board
        """
        computerMove = random.randint(0, 8)
        while (self.board[computerMove] == "O" or self.board[computerMove] == "X"):
            computerMove = random.randint(0, 8)

        self.board[computerMove] = "O"
        self.printBoard()



    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """


        for i in range(3):
            #checks for vertical win
            if self.board[0+i] == who and self.board[3+i] == who and self.board[6+i] == who:
                return True;
            #checks for horizontal win
            if self.board[3*i] == who and self.board[3*i+1] == who and self.board[3*i+2] == who:
                return True;
            #checks for diagonal win
        if self.board[4] == who:
            if self.board[0] == who and self.board[8] == who:
                return True
            elif self.board[2] == who and self.board[6] == who:
                return True

        return False

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or
                 "You lost! Thanks for playing." or
                 "A draw! Thanks for playing."
        """
        #Checks for win and writes the corresponding end message.
        if self.hasWon(who):
            print("You won! Thanks for playing")
            return True;
        #finds the opponents character, checks for loss and writes the corresponding end message.

        if who == "O":
            opponent = "X"
        elif who == "X":
            opponent = "O"

        if self.hasWon(opponent):
            print("You Lost! Thanks for playing")
            return False

        #Checks for draw and writes the corresponding end message.
        draw = True;
        for i in range(9):
            if self.board[i] != "X" and self.board[i] != "O":
                draw = False;

        if draw:
            print("A draw! Thanks for playing.")
            return True;

        #Nobody won, so return false.
        return False

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate