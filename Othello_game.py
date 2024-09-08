# Author: Gregory Lion
# GitHub username: Greg1324
# Date: 9/8/2024
# Description: Allows the user to play the game of Othello utilizing two classes: Player and Othello.
# The user will input what move they want to make and the board will update until there are no possible
# moves left for either play and then the winner will be returned.

import random

class Player:
    """Class represents a player in the game of Othello, and contains their name and the color of their pieces.
    It will be used through composition inside the Othello class"""

    def __init__(self, player_name, piece_color):
        """Initializes the information about the player which will eventually be added to a list in the Othello class
        through composition in which the class's object will be appended to Othello's player list"""
        self._player_name = player_name
        self._piece_color = piece_color

    def get_player_name(self):
        """
        Method that gets the player name from the object and returns it
        :return: player_name
        """
        return self._player_name

    def get_player_color(self):
        """
        Method that gets the player's piece color from the object and returns it
        :return: piece_color
        """
        return self._piece_color


class Othello:
    """
    Class represents the game of Othello, that contains the player and board information.
    It will allow the players to update the board information in order to play the game.
    """

    def __init__(self):
        """
        Initializes an empty list of players and the start of the board
        """
        self._player_list = []
        self._board = [["." for i in range(10)] for j in range(10)]

        for i in range(10):
            self._board[i][0] = "*"
            self._board[i][9] = "*"
            self._board[0][i] = "*"
            self._board[9][i] = "*"
        for i in range(1, 9):
            self._board[0][i] = str(i)
            self._board[i][0] = str(i)

        self._board[0][0] = " "
        self._board[4][4] = "O"
        self._board[5][5] = "O"
        self._board[4][5] = "X"
        self._board[5][4] = "X"

    def print_board(self):
        """
        Prints the current board information by going across each row and printing each character
        :return: Displayed board
        """

        for i in range(10):
            for j in range(10):
                if j == 9:
                    print(self._board[i][j])
                else:
                    print(self._board[i][j], end=" ")

    def count_colors(self):
        white_count = 0
        black_count = 0
        # Look through the entire board to count up the white and black pieces
        for i in range(1, 9):
            for j in range(1, 9):
                if self._board[i][j] == "X":
                    black_count += 1
                elif self._board[i][j] == "O":
                    white_count += 1

        return [white_count, black_count]

    def create_player(self, player_name, color):
        """
        Adds a new player object to Othello's player list
        :param player_name:
        :param color:
        :return: Adds new player to list
        """
        self._player_list.append(Player(player_name, color))

    def return_winner(self):
        """
        Compares the number of white and black pieces on the board in order to determine the winner
        :return: Prints statement saying which color won, and the player's name
        """
        white_count = 0
        black_count = 0
        # Look through the entire board to count up the white and black pieces
        for i in range(1, 9):
            for j in range(1, 9):
                if self._board[i][j] == "X":
                    black_count += 1
                elif self._board[i][j] == "O":
                    white_count += 1

        # Determine who wins based on number of white and black pieces on the board
        if white_count > black_count:
            for player in self._player_list:
                if "white" == player.get_player_color():
                    return "Winner is white player: " + player.get_player_name()
        elif white_count < black_count:
            for player in self._player_list:
                if "black" == player.get_player_color():
                    return "Winner is black player: " + player.get_player_name()
        else:
            return "It's a tie"

    def return_available_positions(self, color):
        """
        For a player's color, it will check the board for every possible position the player cna make a move
        on for that turn
        :param color:
        :return: List of possible positions
        """
        positions = []
        # Determine which type of piece in the board to look for
        if color == "white":
            piece = "O"
            other_piece = "X"
        else:
            piece = "X"
            other_piece = "O"

        # Look through the entire board for that type of piece
        for i in range(1, 9):
            for j in range(1, 9):
                if self._board[i][j] == piece:
                    # Check all available positions
                    self.right_row_pos(i, j, other_piece, positions)
                    self.left_row_pos(i, j, other_piece, positions)
                    self.north_column_pos(i, j, other_piece, positions)
                    self.south_column_pos(i, j, other_piece, positions)
                    self.northeast_diagonal_pos(i, j, other_piece, positions)
                    self.northwest_diagonal_pos(i, j, other_piece, positions)
                    self.southeast_diagonal_pos(i, j, other_piece, positions)
                    self.southwest_diagonal_pos(i, j, other_piece, positions)
        # Return the list of sorted positions
        positions.sort()
        return positions

    def make_move(self, color, piece_position):
        """
        Will insert the colored piece in the 2-D array with the same position that the user inputted.
        Will then change pieces of the other color if they are flanked by a piece of the same color.
        :param color:
        :param piece_position:
        :return: Updated board with the changed caused by the new piece
        """
        # Determine which type of piece in the board to look for
        if color == "white":
            piece = "O"
            other_piece = "X"
        else:
            piece = "X"
            other_piece = "O"

        i = piece_position[0]
        j = piece_position[1]
        # Put the player's piece on the spot they inputted
        self._board[i][j] = piece

        # Check any other possible changes to the board and update it
        self.right_row_move(i, j, piece, other_piece)
        self.left_row_move(i, j, piece, other_piece)
        self.north_column_move(i, j, piece, other_piece)
        self.south_column_move(i, j, piece, other_piece)
        self.northeast_diagonal_move(i, j, piece, other_piece)
        self.northwest_diagonal_move(i, j, piece, other_piece)
        self.southeast_diagonal_move(i, j, piece, other_piece)
        self.southwest_diagonal_move(i, j, piece, other_piece)

        return self._board

    def play_game(self, player_color, piece_position):
        """
        If the move is valid, then it will insert the colored piece of a player in the 2-D array with the same
        position that the user inputted, and then update the board. It will also check for invalid moves and
        if one is made, will print all the valid positions. Will also check if the game has ended.
        :param player_color:
        :param piece_position:
        :return: Updated board if a valid move, list of valid positions if an invalid move, and
        if the game has ended will return who won with how many pieces.
        """
        if player_color == "white":
            other_color = "black"
        else:
            other_color = "white"

        pos_list = self.return_available_positions(player_color)

        # Determine whether a move is valid or not
        if piece_position not in pos_list:
            print("Here are the valid moves: ")
            print(pos_list)
            return "Invalid move"
        else:
            self.make_move(player_color, piece_position)

        # Check to see if there exist more moves for either player
        # If there are not, then the game has ended
        pos_list = self.return_available_positions(player_color)
        other_color_pos_list = self.return_available_positions(other_color)
        if pos_list == [] and other_color_pos_list == []:
            white_count = 0
            black_count = 0
            # Look through the entire board to count up the white and black pieces
            for i in range(1, 9):
                for j in range(1, 9):
                    if self._board[i][j] == "X":
                        black_count += 1
                    elif self._board[i][j] == "O":
                        white_count += 1

            # Inform the user the game has ended
            print("Game is ended white piece: " + str(white_count) + " black piece: " + str(black_count))
            return self.return_winner()

    def game_ai(self, color, other_color):
        pos_list = self.return_available_positions(color)
        val_arr = []
        max_value = 0

        if color == "white":
            piece = "O"
            other_piece = "X"
        else:
            piece = "X"
            other_piece = "O"

        for coordinate in pos_list:
            value = (self.right_row_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.left_row_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.north_column_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.south_column_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.northeast_diagonal_move_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.northwest_diagonal_move_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.southeast_diagonal_ai_check(coordinate[0], coordinate[1], piece, other_piece)
            + self.southwest_diagonal_ai_check(coordinate[0], coordinate[1], piece, other_piece))

            if value > max_value:
                val_arr.clear()
                val_arr.append([value, coordinate])
                max_value = value
            elif value == max_value:
                val_arr.append([value, coordinate])

        if len(val_arr) > 1:
            move = random.choice(val_arr)
        elif len(val_arr) == 0:
            other_color_pos_list = self.return_available_positions(other_color)
            if pos_list == [] and other_color_pos_list == []:
                white_count = 0
                black_count = 0
                # Look through the entire board to count up the white and black pieces
                for i in range(1, 9):
                    for j in range(1, 9):
                        if self._board[i][j] == "X":
                            black_count += 1
                        elif self._board[i][j] == "O":
                            white_count += 1

                # Inform the user the game has ended
                print("Game is ended white piece: " + str(white_count) + " black piece: " + str(black_count))
                return self.return_winner()
            else:
                return
        else:
            move = val_arr[0]

        self.play_game(color, move[1])
        return move[1]

    # Helper functions for determining possible positions
    def right_row_pos(self, i, j, other_piece, positions):
        """
        Iterates through the right side of the row to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i][j + 1] == other_piece:
            while self._board[i][j + 1] == other_piece:
                j += 1
            if self._board[i][j + 1] == ".":
                if (i, j + 1) not in positions:
                    positions.append((i, j + 1))

    def left_row_pos(self, i, j, other_piece, positions):
        """
        Iterates through the left side of the row to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i][j - 1] == other_piece:
            while self._board[i][j - 1] == other_piece:
                j -= 1
            if self._board[i][j - 1] == ".":
                if (i, j - 1) not in positions:
                    positions.append((i, j - 1))

    def south_column_pos(self, i, j, other_piece, positions):
        """
        Iterates through the south side of the column to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i + 1][j] == other_piece:
            while self._board[i + 1][j] == other_piece:
                i += 1
            if self._board[i + 1][j] == ".":
                if (i + 1, j) not in positions:
                    positions.append((i + 1, j))

    def north_column_pos(self, i, j, other_piece, positions):
        """
        Iterates through the north side of the column to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i - 1][j] == other_piece:
            while self._board[i - 1][j] == other_piece:
                i -= 1
            if self._board[i - 1][j] == ".":
                if (i - 1, j) not in positions:
                    positions.append((i - 1, j))

    def southeast_diagonal_pos(self, i, j, other_piece, positions):
        """
        Iterates through the southeast side of the piece to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i + 1][j + 1] == other_piece:
            while self._board[i + 1][j + 1] == other_piece:
                i += 1
                j += 1
            if self._board[i + 1][j + 1] == ".":
                if (i + 1, j + 1) not in positions:
                    positions.append((i + 1, j + 1))

    def southwest_diagonal_pos(self, i, j, other_piece, positions):
        """
        Iterates through the southwest side of the piece to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i + 1][j - 1] == other_piece:
            while self._board[i + 1][j - 1] == other_piece:
                i += 1
                j -= 1
            if self._board[i + 1][j - 1] == ".":
                if (i + 1, j - 1) not in positions:
                    positions.append((i + 1, j - 1))

    def northeast_diagonal_pos(self, i, j, other_piece, positions):
        """
        Iterates through the northeast side of the piece to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i - 1][j + 1] == other_piece:
            while self._board[i - 1][j + 1] == other_piece:
                i -= 1
                j += 1
            if self._board[i - 1][j + 1] == ".":
                if (i - 1, j + 1) not in positions:
                    positions.append((i - 1, j + 1))

    def northwest_diagonal_pos(self, i, j, other_piece, positions):
        """
        Iterates through the northwest side of the piece to determine if there is an available position
        :param i:
        :param j:
        :param other_piece:
        :param positions:
        :return: appended positions list
        """
        if self._board[i - 1][j - 1] == other_piece:
            while self._board[i - 1][j - 1] == other_piece:
                i -= 1
                j -= 1
            if self._board[i - 1][j - 1] == ".":
                if (i - 1, j - 1) not in positions:
                    positions.append((i - 1, j - 1))

    # Helper functions for manipulating the game board when a move is made by a player

    def right_row_move(self, i, j, piece, other_piece):
        """
        Iterates through the right side of the row to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the right row of the piece in question
        """
        counter = 0
        save_j = j
        if self._board[i][j + 1] == other_piece:
            while self._board[i][j + 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                j += 1
            if self._board[i][j + 1] == piece:
                j = save_j  # Restore the original j so that it can iterate from the same position
                for x in range(0, counter):
                    self._board[i][j + 1] = piece  # Replace the opponent's pieces with the player's pieces
                    j += 1

    def left_row_move(self, i, j, piece, other_piece):
        """
        Iterates through the left side of the row to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the left row of the piece in question
        """
        counter = 0
        save_j = j
        if self._board[i][j - 1] == other_piece:
            while self._board[i][j - 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                j -= 1
            if self._board[i][j - 1] == piece:
                j = save_j  # Restore the original j so that it can iterate from the same position
                for x in range(0, counter):
                    self._board[i][j - 1] = piece  # Replace the opponent's pieces with the player's pieces
                    j -= 1

    def north_column_move(self, i, j, piece, other_piece):
        """
        Iterates through the north side of the column to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the northern column of the piece in question
        """
        counter = 0
        save_i = i
        if self._board[i - 1][j] == other_piece:
            while self._board[i - 1][j] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i -= 1
            if self._board[i - 1][j] == piece:
                i = save_i  # Restore the original i so that it can iterate from the same position
                for x in range(0, counter):
                    self._board[i - 1][j] = piece  # Replace the opponent's pieces with the player's pieces
                    i -= 1

    def south_column_move(self, i, j, piece, other_piece):
        """
        Iterates through the south side of the column to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the southern column of the piece in question
        """
        counter = 0
        save_i = i
        if self._board[i + 1][j] == other_piece:
            while self._board[i + 1][j] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i += 1
            if self._board[i + 1][j] == piece:
                i = save_i  # Restore the original i so that it can iterate from the same position
                for x in range(0, counter):
                    self._board[i + 1][j] = piece  # Replace the opponent's pieces with the player's pieces
                    i += 1

    def southeast_diagonal_move(self, i, j, piece, other_piece):
        """
        Iterates through the southeast of the piece to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the southeast diagonal of the piece in question
        """
        counter = 0
        save_i = i
        save_j = j
        if self._board[i + 1][j + 1] == other_piece:
            while self._board[i + 1][j + 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i += 1
                j += 1
            if self._board[i + 1][j + 1] == piece:
                i = save_i  # Restore the original i and j so that it can iterate from the same position
                j = save_j
                for x in range(0, counter):
                    self._board[i + 1][j + 1] = piece  # Replace the opponent's pieces with the player's pieces
                    i += 1
                    j += 1

    def southwest_diagonal_move(self, i, j, piece, other_piece):
        """
        Iterates through the southwest of the piece to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the southwest diagonal of the piece in question
        """
        counter = 0
        save_i = i
        save_j = j
        if self._board[i + 1][j - 1] == other_piece:
            while self._board[i + 1][j - 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i += 1
                j -= 1
            if self._board[i + 1][j - 1] == piece:
                i = save_i  # Restore the original i and j so that it can iterate from the same position
                j = save_j
                for x in range(0, counter):
                    self._board[i + 1][j - 1] = piece  # Replace the opponent's pieces with the player's pieces
                    i += 1
                    j -= 1

    def northeast_diagonal_move(self, i, j, piece, other_piece):
        """
        Iterates through the northeast of the piece to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the northeast diagonal of the piece in question
        """
        counter = 0
        save_i = i
        save_j = j
        if self._board[i - 1][j + 1] == other_piece:
            while self._board[i - 1][j + 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i -= 1
                j += 1
            if self._board[i - 1][j + 1] == piece:
                i = save_i  # Restore the original i and j so that it can iterate from the same position
                j = save_j
                for x in range(0, counter):
                    self._board[i - 1][j + 1] = piece  # Replace the opponent's pieces with the player's pieces
                    i -= 1
                    j += 1

    def northwest_diagonal_move(self, i, j, piece, other_piece):
        """
        Iterates through the northwest of the piece to determine if any pieces of the other color need to be
        flipped to the color of the player's piece
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: Updated game board concerning the northwest diagonal of the piece in question
        """
        counter = 0
        save_i = i
        save_j = j
        if self._board[i - 1][j - 1] == other_piece:
            while self._board[i - 1][j - 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i -= 1
                j -= 1
            if self._board[i - 1][j - 1] == piece:
                i = save_i  # Restore the original i and j so that it can iterate from the same position
                j = save_j
                for x in range(0, counter):
                    self._board[i - 1][j - 1] = piece  # Replace the opponent's pieces with the player's pieces
                    i -= 1
                    j -= 1

    def right_row_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the right side of the row to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0

        if self._board[i][j + 1] == other_piece:
            while self._board[i][j + 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                j += 1
            if self._board[i][j + 1] == piece:
                return counter
        return 0

    def left_row_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the left side of the row to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0
        if self._board[i][j - 1] == other_piece:
            while self._board[i][j - 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                j -= 1
            if self._board[i][j - 1] == piece:
                return counter
        return 0

    def north_column_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the north side of the column to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0
        if self._board[i - 1][j] == other_piece:
            while self._board[i - 1][j] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i -= 1
            if self._board[i - 1][j] == piece:
                return counter
        return 0

    def south_column_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the south side of the column to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0
        if self._board[i + 1][j] == other_piece:
            while self._board[i + 1][j] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i += 1
            if self._board[i + 1][j] == piece:
                return counter
        return 0

    def southeast_diagonal_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the southeast of the piece to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0

        if self._board[i + 1][j + 1] == other_piece:
            while self._board[i + 1][j + 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i += 1
                j += 1
            if self._board[i + 1][j + 1] == piece:
                return counter
        return 0

    def southwest_diagonal_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the southwest of the piece to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0
        if self._board[i + 1][j - 1] == other_piece:
            while self._board[i + 1][j - 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i += 1
                j -= 1
            if self._board[i + 1][j - 1] == piece:
                return counter
        return 0

    def northeast_diagonal_move_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the northeast of the piece to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        """
        counter = 0
        if self._board[i - 1][j + 1] == other_piece:
            while self._board[i - 1][j + 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i -= 1
                j += 1
            if self._board[i - 1][j + 1] == piece:
                return counter
        return 0

    def northwest_diagonal_move_ai_check(self, i, j, piece, other_piece):
        """
        Iterates through the northwest of the piece to count the number of pieces that will be flipped to the other
        color if a player makes a move on that coordinate
        :param i:
        :param j:
        :param piece:
        :param other_piece:
        :return: The number of pieces that will be flipped to the other color if a player makes a move on that coordinate
        """
        counter = 0
        if self._board[i - 1][j - 1] == other_piece:
            while self._board[i - 1][j - 1] == other_piece:
                counter += 1  # Keep track of how many iterations occur
                i -= 1
                j -= 1
            if self._board[i - 1][j - 1] == piece:
                return counter
        return 0
