# group number: G16
# student names: Greg Berezhnov, Amraj Aujla, Amin Fahiminia, Navraj Bains

import random
from math import floor


class TicTacToe:
    def __init__(self):  # Use as is
        """ initializes data fields (board and played)
            and prints the banner messages
            and prints the initial board on the screen
        """
        self.board = [' '] * 9  # A list of 9 strings, one for each cell,
        # will contain ' ' or 'X' or 'O'
        self.played = set()  # Set (of cell num) already played: to keep track of the played cells
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
    
            """.format(self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5],
                       self.board[6], self.board[7], self.board[8])
        )

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number;
            error checks that the input is a valid cell number;
            and prints the info and the updated self.board;
        """
        while True:
            # init user prompt
            userMove = input("Enter next player move (0-8): ")

            # checks for valid user cell input
            if not userMove.isdigit():
                print("Input is not an integer")
            elif not (int(userMove) >= 0 and int(userMove) < 9):
                print("Enter a valid cell between 0 and 8")
            else:
                # place an X in the selected cell if it is empty
                if self.board[int(userMove)] == ' ':
                    self.board[int(userMove)] = 'X'
                    break
                else:
                    print("Cell is not empty")

        self.printBoard()

    def computerNextMove(self) -> None:
        """ computer  checks for possible wins. If it can win it does
         Then the computer checks for possible losses, if it prevent that it will
         A trick is to win through the diagonals, since the computer is scared of diagonals
            The computer prints the info and updated self.board
        """
        #Checks for win
        taken = []
        computerMove = -1

        for i in range(9):
            if self.board[i] == "O":
                taken.append(1)
            elif self.board[i] == "X":
                taken.append(0)
            else:
                taken.append(-1)


        found = False
        for first in range(9):

            for second in range(first, 9):
                if (found):
                    break
                if  (taken[first] == 1 and taken[second] == 1 and first != second ): # finds two distinct computer moves
                    if (first % 3 == second % 3): # if they are on the same column
                        for i in range(3):
                            if self.board[3 * i + first % 3] == ' ': # find blank space to play
                                computerMove = 3*i + (first % 3) # make the move
                                found = True
                                break
                    if floor(first/3) == floor(second/3):
                        for i in range(3):
                            if (self.board[3*floor(first/3) + i] == " "):
                                computerMove = 3*floor(first/3) + i
                                found = True
                                break

        if computerMove != -1:
            self.board[computerMove] = "O"
            self.printBoard()
            return # make it and return

        found = False
        for first in range(9):
            for second in range(first, 9):
                if (found):
                    break
                if  (taken[first] == 0 and taken[second] == 0 and first != second ): # finding two distinct oppponent moves
                    if (first % 3 == second % 3): # if the the moves are in the same column
                        for i in range(3):
                            if self.board[3 * i + first % 3] == ' ': # find blank space to play
                                computerMove = 3*i + (first % 3) # make the move
                                found = True
                                break
                    if floor(first/3) == floor(second/3):
                        for i in range(3):
                            if (self.board[3*floor(first/3) + i] == " "):
                                computerMove = 3*floor(first/3) + i
                                found = True
                                break

        if computerMove != -1:
            self.board[computerMove] = "O"
            self.printBoard()
            return

        computerMove = random.randint(0, 8)
        while (self.board[computerMove] == "O" or self.board[computerMove] == "X"):
            computerMove = random.randint(0, 8)

        self.board[computerMove] = "O"
        self.printBoard()

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """

        for i in range(3):
            # checks for vertical win
            if self.board[0 + i] == who and self.board[3 + i] == who and self.board[6 + i] == who:
                return True;
            # checks for horizontal win
            if self.board[3 * i] == who and self.board[3 * i + 1] == who and self.board[3 * i + 2] == who:
                return True;
            # checks for diagonal win
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
        # Checks for win and writes the corresponding end message.
        if self.hasWon("X"):
            print("You won! Thanks for playing")
            return True;
        #  Checks for loss and writes the corresponding end message.

        if self.hasWon("O"):
            print("You Lost! Thanks for playing")
            return False

        # Checks for draw and writes the corresponding end message.
        draw = True;
        for i in range(9):
            if self.board[i] != "X" and self.board[i] != "O":
                draw = False;

        if draw:
            print("A draw! Thanks for playing.")
            return True;

        # Nobody won, so return false.
        return False


if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()  # X starts first
        if (ttt.terminate('X')): break  # if X won or a draw, print message and terminate
        ttt.computerNextMove()  # computer plays O
        if (ttt.terminate('O')): break  # if O won or a draw, print message and terminate