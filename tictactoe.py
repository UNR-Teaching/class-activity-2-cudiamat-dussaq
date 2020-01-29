""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""

class Board:

    tictactoeBoard = []
    
    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        # 0-8
        # 0 - empty space, 1 - x's, 2 - o's
        for x in range(8):
            self.tictactoeBoard.append('-')

    def valid_input(self, column,row):
        input = (row*3) + column
        if(input >= 0 and input <= 8):
            return True
        else:
            return False

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        if(self.valid_input):
            input = (row*3) + column
            self.tictactoeBoard[input] = player.lower()
            self.display_board()
            return True
        else:
            return False
        
    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        # Check Columns 0-2
        for columns in range(2):
            if(tictactoeBoard[columns] == tictactoeBoard[columns+3] and
               tictactoeBoard[columns+3] == tictactoeBoard[columns+6]):
                return True

        # Check Rows..
        '''
        for rows in range(2):
            if(tictactoeBoard[] == tictactoeBoard[+1] and
               tictactoeBoard[columns+1] == tictactoeBoard[columns+2]):
        '''

        # Check Diagonals

        
        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        
        pass

    def display_board(self):
       ''' 
for i in range(2):
            for x in range(2):
                print(self.tictactoeBoard[(x*3)+i])
            print()
'''
       for i in range(8):
           print(i)
           print(self.tictactoeBoard[i])
       
            
        

