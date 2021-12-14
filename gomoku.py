# Gomoku - Programming 1

from tkinter import *

# When tested on a secondary Windows device, it was revealed that dimensions may differ across devices
# If the bottom of the main menu is cut-off, please change this variable to 600
height_val = 550
bg_color = '#F1A369'
font_type = "Rockwell"

window = Tk()
window.title("Gomoku - Programming 1 Assignment by Arihaan S. Negi")
window.geometry(f'800x{height_val}')
window['bg'] = bg_color


# Handles the different menus in the game, i.e. main menu, instructions, game screen
def raise_frame(top_frame):
    top_frame.tkraise()


# Functions to change button color on hover
def on_enter(e):
    e.widget['highlightbackground'] = '#E77D2D'


def on_leave(e):
    e.widget['highlightbackground'] = bg_color


# Defining the different menus
StartMenu = Frame(window, height=height_val, width=800, bg=bg_color)
Instructions = Frame(window, height=height_val, width=800, bg=bg_color)
PlayerChoose = Frame(window, height=height_val, width=800, bg=bg_color)
GameView = Frame(window, height=height_val, width=800, bg=bg_color)
EmptyFrame = Frame(window, height=height_val, width=800, bg=bg_color)

for frame in (StartMenu, Instructions, GameView, PlayerChoose, EmptyFrame):
    frame.grid(row=0, column=0, sticky='nsew')


class StartMenuClass:
    # Headers
    Header1 = Label(StartMenu, text="Welcome to", font=(font_type, 40), bg=bg_color, fg="#000").pack(pady=(60, 15))
    Header2 = Label(StartMenu, text="GOMOKU", font=(font_type, 80), bg=bg_color, fg="#000").pack(pady=(0, 5))
    Header3 = Label(StartMenu, text="(五目並べ)", font=(font_type, 30), bg=bg_color, fg="#000").pack(pady=(0, 30))

    # Buttons
    button1 = Button(StartMenu, text="Play Game", height='2', font=(font_type, 20), highlightbackground=bg_color,
                     fg='black', command=lambda: raise_frame(PlayerChoose))
    button2 = Button(StartMenu, text="How to play Gomoku", height='2', font=(font_type, 20),
                     highlightbackground=bg_color, fg='black', command=lambda: raise_frame(Instructions))
    button1.pack(pady=(0, 10))
    button2.pack()

    # Binding hover events to buttons
    button1.bind("<Enter>", on_enter)
    button1.bind("<Leave>", on_leave)
    button2.bind("<Enter>", on_enter)
    button2.bind("<Leave>", on_leave)

    # Credits to self
    Credits = Label(StartMenu, text="Developed by Arihaan S. Negi for Programming 1",
                    font=(font_type, 15), bg=bg_color, fg="#000").pack(pady=(30, 0))
    Credits2 = Label(StartMenu, text="Code available at github.com/Arihaan",
                     font=(font_type, 10), bg=bg_color, fg="#000").pack(pady=(5, 0))


class InstructionsClass:
    # Creating the instructions menu:
    # Back button
    button1 = Button(Instructions, text="Back", height='1', font=(font_type, 17), highlightbackground=bg_color,
                     fg='black', command=lambda: raise_frame(StartMenu))
    button1.pack(side='top', anchor='nw', padx=(5, 0), pady=(5, 0))
    button1.bind("<Enter>", on_enter)
    button1.bind("<Leave>", on_leave)

    # Header
    Howto_header = Label(Instructions, text="How to play Gomoku", font=(font_type, 40), bg=bg_color, fg="#000")\
        .pack(pady=(0, 10))

    # Instruction labels
    howtotext = ("Gomoku is a two-player game of strategy, originating from Japan. "
                 "In the Japanese language, it is referred to as 'gomokunarabe' where 'go' means five, 'moku' is a "
                 "counter word for pieces and 'narabe' means line-up.\n\n"
                 "The objective of the game is to get 'Five in a Row', i.e. create an unbroken row of five consecutive "
                 "pieces of your color (black or white). These pieces may be placed horizontally, vertically or "
                 "diagonally.\n\n"
                 "In order to place your piece, click the grid intersection where you desire to place it. Each player "
                 "will get one turn and the current turn would be indicated by a label on the right.")
    MainInstructions = Label(Instructions, text=howtotext, font=(font_type, 20), bg=bg_color, fg="#000",
                             wraplength=700, justify="left").pack(padx=(5, 0), pady=(0, 0))


def name_update_helper():
    raise_frame(GameView)
    texttoput = PlayerChooseClass.player1input.get()
    if texttoput == '':
        texttoput = "Player 1"
    GameViewClass.current_player_label.config(text=texttoput)


class PlayerChooseClass:
    # Creating the player choose menu:
    # Back button
    button1 = Button(PlayerChoose, text="Back", height='1', font=(font_type, 17), highlightbackground=bg_color,
                     fg='black', command=lambda: raise_frame(StartMenu))
    button1.pack(side='top', anchor='nw', padx=(5, 0), pady=(5, 0))
    button1.bind("<Enter>", on_enter)
    button1.bind("<Leave>", on_leave)

    # Labels
    Header = Label(PlayerChoose, text="Choose your pieces.", font=(font_type, 40), bg=bg_color, fg="#000") \
        .pack(pady=(20, 5))
    Header2 = Label(PlayerChoose, text="(White plays first)", font=(font_type, 20), bg=bg_color, fg="#000") \
        .pack(pady=(0, 10))

    # Pieces
    pieces = Frame(PlayerChoose, bg=bg_color)

    # Draw the white piece
    White = Canvas(pieces, bg=bg_color, width="160", height="160", highlightthickness='0')
    White.create_oval(10, 10, 155, 155, fill='white', width='3', outline='black')
    White.pack(side="left", padx="40")

    # Draw the black piece
    Black = Canvas(pieces, bg=bg_color, width="160", height="160", highlightthickness='0')
    Black.create_oval(10, 10, 155, 155, fill='#4B3F3F', width='3', outline='black')
    Black.pack(side="right", padx="40")

    pieces.pack(pady=(10, 10))

    names = Frame(PlayerChoose, bg=bg_color)

    # Ask name for white piece (player1)
    player1input = Entry(names, width='10')
    player1input.pack(side="left", padx="70")

    # Ask name for black piece (player2)
    player2input = Entry(names, width='10')
    player2input.pack(side="right", padx="70")

    names.pack(pady=(10, 10))

    # Name enter instruction
    Footer = Label(PlayerChoose, text="[Please enter player names or leave blank for default names.]",
                   font=(font_type, 15), bg=bg_color, fg="#000").pack(pady=(0, 20))

    # Start game button
    submit = Button(PlayerChoose, text="Start Game", height='2', font=(font_type, 20), highlightbackground=bg_color,
                    fg='black', command=lambda: name_update_helper())
    submit.pack()
    submit.bind("<Enter>", on_enter)
    submit.bind("<Leave>", on_leave)


# Class holding entire game logic
class GameClass:
    def __init__(self):

        # self.board is a 15 x 15 array of integers with the contents of
        # each square: 0 = empty, 1 = player 1 stone, 2 = player 2 stone
        self.board = [[0] * 14 for _ in range(14)]

        self.turn = 1  # the player whose turn it is to move (1 or 2)
        self.winner = 0  # the player who has won, if any
        self.win_x1 = self.win_y1 = None  # (x, y) pos of one end of winning line
        self.win_x2 = self.win_y2 = None  # (x, y) pos of other end of winning line

    dirs = [(1, -1), (1, 0), (1, 1), (0, 1)]

    # If either player has exactly 5 in a row starting at (x, y) in direction (dx, dy),
    # return that player number (1 or 2); otherwise return 0.
    def five_in_a_row(self, x, y, dx, dy):
        def at(x_coord, y_coord):
            return self.board[x_coord][y_coord] if 0 <= x_coord < 14 and 0 <= y_coord < 14 else None

        p = self.board[x][y]
        return (p > 0 and at(x - dx, y - dy) != p and all([at(x + i * dx, y + i * dy) == p for i in range(5)])
                and at(x + 5 * dx, y + 5 * dy) != p)

    # Check if either player has won.  If so, set self.winner and attributes
    # indicating the winning line position (self.win_x1, self.win_y1, etc.)
    def check_win(self):
        for x in range(14):
            for y in range(14):
                for dx, dy in self.dirs:
                    if self.five_in_a_row(x, y, dx, dy):
                        if self.turn == 1:
                            self.winner = 2
                        else:
                            self.winner = 1
                        self.win_x1, self.win_y1 = x, y
                        self.win_x2, self.win_y2 = x + dx * 5, y + dy * 5
                        return [True, self.win_x1, self.win_y1, self.win_x2, self.win_y2, dx, dy]
        return [False]

    # If (x, y) is a valid move for the current player, place a stone there and
    # returns tuple with True.  Otherwise returns tuple with False. The second value of tuple decides color of piece.
    def play(self, x, y):
        if self.board[y][x] == 0:
            self.board[y][x] = self.turn
            if self.turn == 2:
                self.turn = 1
            else:
                self.turn = 2
            return True
        return False

    # resets game back to its original setting
    def reset(self):
        self.__init__()


# Main Game class, all logical game events are taking place here
Game = GameClass()


# this variable helps to check if game has been reset so no new pieces are placed immediately after
pieces_placed = 0


def has_won(x1=0, y1=0, x2=0, y2=0):
    if Game.winner == 2:
        winner_name = PlayerChooseClass.player2input.get()
        if winner_name == '':
            winner_name = 'Player 2'
    else:
        winner_name = PlayerChooseClass.player1input.get()
        if winner_name == '':
            winner_name = 'Player 1'
    GameViewClass.turn_label.config(text="")
    GameViewClass.current_player_label.config(text=f'{winner_name}\nhas won this game.',
                                              font=(font_type, 30), wraplength='200')
    GameViewClass.click_anywhere_label.config(text="Click the 'Reset Board' button below or anywhere on the "
                                                   "board to start a new game!")
    GameViewClass.gomoku_grid.create_line(x1, y1, x2, y2, fill='red', width=6, tag="win-line")


# function handling logic for when player clicks on the board
def piece_placed(event):
    global pieces_placed
    # check if game is finished already (someone has won)
    if Game.winner != 0:
        game_resetter()

    # counter for pieces
    pieces_placed += 1

    # check if the click was to reset the game or not
    if pieces_placed == 0:
        return

    piece_colors = ['#4B3F3F', 'white']
    # Retrieving entered player names
    player1, player2 = PlayerChooseClass.player1input.get(), PlayerChooseClass.player2input.get()
    if player1 == "":
        player1 = "Player 1"
    if player2 == "":
        player2 = "Player 2"
    player_names = [player1, player2]
    x, y = event.x, event.y
    rounder = lambda num, base: base * round(num / base)
    x_grid_val, y_grid_val = rounder(x, 33.33) // 33, rounder(y, 33.33) // 33
    if 0 < x_grid_val < 15 and 0 < y_grid_val < 15:
        if Game.play(int(x_grid_val)-1, int(y_grid_val)-1):
            GameViewClass.gomoku_grid.create_oval((33.33*x_grid_val - 13), (33.33*y_grid_val + 13),
                                                  (33.33*x_grid_val + 13), (33.33*y_grid_val - 13),
                                                  fill=piece_colors[Game.turn - 1], width='2', outline='black',
                                                  tag="piece")
            GameViewClass.current_player_label.config(text=player_names[Game.turn - 1])
    results = Game.check_win()
    if results[0]:
        x1_coord_line, y1_coord_line = (results[2] + 1) * 33.33333, (results[1] + 1) * 33.33333
        x2_coord_line, y2_coord_line = (results[4] + 1) * 33.33333, (results[3] + 1) * 33.33333
        if (results[5], results[6]) == (0, 1):
            x1_coord_line -= 20
            x2_coord_line -= 13
        elif (results[5], results[6]) == (1, 0):
            y1_coord_line -= 20
            y2_coord_line -= 13
        elif (results[5], results[6]) == (1, 1):
            x1_coord_line -= 20
            x2_coord_line -= 13
            y1_coord_line -= 20
            y2_coord_line -= 13
        else:
            x1_coord_line += 20
            x2_coord_line += 13
            y1_coord_line -= 20
            y2_coord_line -= 13
            pass
        has_won(x1_coord_line, y1_coord_line, x2_coord_line, y2_coord_line)


def game_resetter(menu=False):
    global pieces_placed
    pieces_placed = -1
    GameViewClass.gomoku_grid.delete("piece", "win-line")
    Game.reset()
    GameViewClass.turn_label.config(text="Turn:")
    GameViewClass.click_anywhere_label.config(text="")
    player1_name = PlayerChooseClass.player1input.get()
    if player1_name == "":
        player1_name = "Player 1"
    GameViewClass.current_player_label.config(text=f"{player1_name}", font=(font_type, 30))
    if menu == "Reset_Button":
        pieces_placed = 0
    elif menu:
        pieces_placed = 0
        raise_frame(StartMenu)


# all game items will be displayed using this class
class GameViewClass:
    player1 = ''
    # Making frame holding gomoku grid
    game_view = Frame(GameView, bg=bg_color)
    gomoku_grid = Canvas(game_view, width="500", height="500", bg='#F29152')

    # Creating grid lines
    temp_coord = 2
    for i in range(15):
        temp_coord += 33.333333
        gomoku_grid.create_line(temp_coord, 0, temp_coord, 510, fill='black')
        gomoku_grid.create_line(0, temp_coord, 510, temp_coord, fill='black')

    gomoku_grid.pack(padx=(15, 10), pady=(20, 0))
    game_view.pack(side="left", anchor='nw')

    # Frame holding secondary info
    turn_label = Label(GameView, text="Turn:", font=(font_type, 25), bg=bg_color, fg="#000")
    turn_label.pack(pady=(50, 10))
    current_player_label = Label(GameView, text=player1, font=(font_type, 30), bg='#F29152', fg="#000")
    current_player_label.pack(pady=(0, 20))
    click_anywhere_label = Label(GameView, text="", wraplength=200, font=(font_type, 15), bg=bg_color,
                                                fg="#000")
    click_anywhere_label.pack(pady=(30, 30))

    # Button to reset game
    reset_game_button = Button(GameView, text="Reset Board", height='2', font=(font_type, 20),
                               highlightbackground=bg_color, fg='black', command=lambda: game_resetter("Reset_Button"))
    reset_game_button.pack(pady=(25, 0))
    reset_game_button.bind("<Enter>", on_enter)
    reset_game_button.bind("<Leave>", on_leave)

    # Button to go back to main menu
    main_menu_button = Button(GameView, text="Main Menu", height='2', font=(font_type, 20),
                               highlightbackground=bg_color, fg='black', command=lambda: game_resetter("Main Menu"))
    main_menu_button.pack(pady=(10, 0))
    main_menu_button.bind("<Enter>", on_enter)
    main_menu_button.bind("<Leave>", on_leave)

    gomoku_grid.bind('<Button-1>', piece_placed)


raise_frame(StartMenu)
window.mainloop()
