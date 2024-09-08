from Othello_game import *

game = Othello()
print("Hello, welcome to Othello, what color would you like to play?")

error = True

while error is True:
    color = input("Press 1 for white, or 2 for black: ")

    if color == "1":
        human = Player("human player", "white")
        ai = Player("computer player", "black")
        error = False
        player_turn = False
    elif color == "2":
        human = Player("human player", "black")
        ai = Player("computer player", "white")
        error = False
        player_turn = True
    else:
        print("I'm sorry, but you can only type 1 or 2. Please try again.")

game_over = False

while game_over is False:
    error = True
    if player_turn is True:
        game.print_board()
        print("It's", human.get_player_color(), end = '')
        print("'s turn")

        while error is True:
            try:
                row, column = input("Enter the coordinate of your move: ").split(", ")
                result = game.play_game(human.get_player_color(), (int(row), int(column)))
                if result == "Invalid move":
                    print("Please enter one of these moves.")
                elif result is None:
                    error = False
                else:
                    print(result)
                    game_over = True
                    error = False
            except:
                print("Invalid coordinate. The necessary format is: 1st coordinate, 2nd coordinate")

        player_turn = False
    else:
        game.print_board()
        print("It's", ai.get_player_color(), end = '')
        print("'s turn")

        result = game.game_ai(ai.get_player_color(), human.get_player_color())

        if result is not None:
            print(result)
            game_over = True
            error = False

        player_turn = True
