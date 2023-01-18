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

        #generate random cells until one is empty, place two there
        while self.board[randrow][randcolumn] != "":
            randrow = random.randint(0, 3)
            randcolumn = random.randint(0, 3)

        self.board[randrow][randcolumn] = '2'

    def isFull(self) -> bool:
        """ returns True if no empty cell is left, False otherwise """
        for i in range(4): #Checks all the rows if
            for j in range(4): #Checks all the coloumns
                if self.board[i][j] == "": #checks the location at the specfic column and row to see if it is occupied
                    return False #if any spot is not occupied it returns false

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
            move_order = [0, 1, 2, 3]
            for column in move_order:
                moved = [True, True, True, True]
                for row in move_order:
                    if self.board[row][column] != '':
                        for i in range(0, row, +1):
                            if self.board[i][column] == '':
                                self.board[i][column] = self.board[row][column]
                                self.board[row][column] = ''
                                break

                            if int(self.board[i][column]) == int(self.board[row][column]) and moved[i]:
                                j = row + 1
                                open = True
                                # checks to see if there are no numbers present between the two we want to combine
                                while j < row:
                                    if self.board[j][column] != '':
                                        open = False
                                    j += 1

                                if open:
                                    self.board[i][column] = int(self.board[i][column]) * 2
                                    moved[i] = False
                                    self.board[row][column] = ''
                                    break
        elif move == 'A':
            a = [3, 2, 1, 0]
            b = [0, 1, 2, 3]
            for row in a:
                moved = [True, True, True, True]
                for column in b:
                    if self.board[row][column] != '':
                        for i in range(0, column, +1):
                            if self.board[row][i] == '':
                                self.board[row][i] = self.board[row][column]
                                self.board[row][column] = ''
                                break
                            if int(self.board[row][i]) == int(self.board[row][column]) and moved[i]:
                                j = column+1
                                open = True
                                # checks to see if there are no numbers present between the two we want to combine
                                while j < column:
                                    if self.board[row][j] != '':
                                        open = False
                                    j+=1

                                if open:
                                    self.board[row][i] = int(self.board[row][i]) * 2
                                    moved[i] = False
                                    self.board[row][column] = ''
                                    break
        elif move == 'D':
            a = [3, 2, 1, 0]
            for row in a:
                for column in a:
                    if self.board[row][column] != '':
                        for i in range(3, column, -1):
                            if self.board[row][i] == '':
                                self.board[row][i] = self.board[row][column]
                                self.board[row][column] = ''
                                break

                            if int(self.board[row][i]) == int(self.board[row][column]):
                                self.board[row][i] = int(self.board[row][i]) * 2
                                self.board[row][column] = ''
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