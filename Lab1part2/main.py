# group number: G16
# student names: Navraj Bains, Amraj Aujla, Greg Berezhnov

import random, sys


class TwentyFortyEight:
    def __init__(self) -> None:  # Use as is
        """
            initializes the board data field
            and displays the initial board
            and prints a welcome message
        """

        self.board: list = []  # a 2-D list to keep current status of the game board
        for _ in range(4):  # initialize the board cells/tiles with ''
            rowList = []
            for i in range(4):
                rowList.append('')
            self.board.append(rowList)

        # add two starting 2's at random cells; using a trivial search
        countOfTwosPlacedAtTheBeginning = 0
        while countOfTwosPlacedAtTheBeginning < 2:
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if self.board[row][column] == '':  # if not already taken
                self.board[row][column] = 2
                countOfTwosPlacedAtTheBeginning += 1

        print();
        print("Welcome! Let's play the 2048 game.");
        print()

    def displayGame(self) -> None:  # Use as is
        """ displays the current board on the console """

        print("+-----+-----+-----+-----+")
        for row in range(4):
            for column in range(4):
                cell = self.board[row][column]
                print(f"|{str(cell).center(5)}", end="")
            print("|")
            print("+-----+-----+-----+-----+")

    def addANewTwoToBoard(self) -> None:
        """
            adds a new 2 at a random available cell
        """
        randrow = random.randint(0,3)
        randcolumn = random.randint(0,3)

        while(self.board[randrow][randcolumn] != ""):
            randrow = random.randint(0, 3)
            randcolumn = random.randint(0, 3)

        self.board[randrow][randcolumn] = '2'

    def isFull(self) -> bool:
        """ returns True if no empty cell is left, False otherwise """
        for i in range(4):

            for j in range(4):
                if (self.board[i][j] == ""):
                    return False

        return True

    def getCurrentScore(self) -> int:
        """
            calculates and returns the score
            the score is the sum of all the numbers currently on the board
        """

        score = 0
        for row in range(len(self.board)):
            for column in range(len(self.board)):
                if self.board[row][column] != '':
                    score += int(self.board[row][column])
        return score  # To Implement

    def updateTheBoardBasedOnTheUserMove(self, move: str) -> None:
        """
            updates the board field based on the move argument
            the move argument is either 'W', 'A', 'S', or 'D'
            directions: W for up; A for left; S for down, and D for right
        """


        if move == 'W':
            for column in range(len(self.board)):
                for row in range(len(self.board)):
                    if self.board[column][row] == "":
                        temp = row
                        for i in range(row + 1, len(self.board)):
                            if self.board[column][i] != '':
                                self.board[column][temp] = self.board[row][i]
                                temp += 1
                                self.board[column][i] = ''

            for column1 in range(len(self.board)):
                for row1 in range(len(self.board)):
                    current = self.board[row1][column1]
                    if self.board[row1][column1] != "":
                        current = int(self.board[row1][column1])

                        if int(current) + 1 < len(self.board) and self.board[row1 + 1][column1] == current:
                            self.board[row1][column1] = str(int(self.board[row1][column1] * 2))
                            for i in range(column + 1, len(self.board)):
                              if i + 1 < len(self.board):
                                  self.board[i][column1] = self.board[i+1][column1]
                                  self.board[i+1][column1] = ''





        elif move == 'A':

            for column in range(4):
                    temp = 0
                    for i in range(1, 4):
                        if self.board[column][temp] == "":
                            for j in range (temp+1, 4):
                                if self.board[column][j] != "":
                                    self.board[column][temp] = self.board[column][j]
                                    self.board[column][j] = ""
                                    break
                        temp +=1


            for column in range(4):
                    temp =0
                    for i in range(1, 4):
                        if (self.board[column][temp] == self.board[column][i] and self.board[column][temp] != ''):
                                self.board[column][temp] = int(self.board[column][temp])*2
                                self.board[column][i] = ""
                                i += 1
                                temp +=1

                        temp +=1






                            






        elif move == 'D':

            column = 4
            while column >= 0:
                column -= 1
                row = 3
                while row >= 0:
                    row -=1
                    for possible in range(3 , column , -1):
                        if self.board[row][column] != "":
                            print(column)
                            if self.board[row][column] == self.board[row][possible]:
                                print(possible)
                                self.board[row][possible] = str(int(self.board[row][possible])*2)
                                self.board[row][column] = ""
                                row = 3
                                column = 3
                                break
                            if self.board[row][possible] == "":
                                self.board[row][possible] = str(int(self.board[row][column]))
                                self.board[row][column] = ""
                                row = 3
                                column = 3
                                break

        elif move == 'S':
            for column in range(len(self.board)):
                for row in range(len(self.board)):
                    if self.board[row][column] != '':
                        if self.board[row][column] == self.board[row + 1][column]:
                            self.board[row + 1][column] = int(self.board[row+1][column]) * 2
                            self.board[row][column] = ''
                            break
                        for i in range(row + 1, len(self.board)):
                            if self.board[i][column] == '':
                                number = self.board[row][column]
                                self.board[row][column] = ''
                                self.board[i][column] = number
                                break



if __name__ == "__main__":  # Use as is
    def promptGamerForTheNextMove() -> str:  # A function used in super-loop
        """
            prompts the gamer to select the next move or Q (to quit)
            valid move direction: one of 'W', 'A', 'S' or 'D'.
            either returns a valid move direction or terminates the game
        """
        print("Enter one of WASD (move direction) or Q (to quit)")
        while True:  # prompt until a valid input is entered
            move = input('> ').upper()
            if move in ('W', 'A', 'S', 'D'):  # a valid move direction
                return move
            if move == 'Q':  # for quit
                print("Exiting the game. Thanks for playing!")
                sys.exit()
            print('Enter one of "W", "A", "S", "D", or "Q"')  # otherwise inform the user about valid input


    game = TwentyFortyEight()

    while True:  # Super-loop for the game
        game.displayGame()
        print(f"Score: {game.getCurrentScore()}")
        game.updateTheBoardBasedOnTheUserMove(promptGamerForTheNextMove())
        game.addANewTwoToBoard()

        if game.isFull():
            game.displayGame()
            print("Game is over. Check out your score.")
            print("Thanks for playing!")
            break