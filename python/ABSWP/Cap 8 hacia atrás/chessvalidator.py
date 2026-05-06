import sys, copy

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ', 'e1': 'wK', 'f1': 'ww',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

def isValidChessboard(board):
    validation = {'kings': False,   # There's a king of each color and no more
                  'number': False,  # Up to 16 pieces
                  'pawns': False,   # No more than 8 pawns
                  'places': False,  # Only Valid places
                  'colors': False,  # Names begin with w or b
                  'name': False     # Names continue with 'P','N','B','R','Q','K'
                  }
    # Initialize counter kings:
    bkings = 0
    wkings = 0
    # Initialize counter for pieces:
    bpieces = 0
    wpieces = 0
    # Initialize counter for pawns:
    wpawns = 0
    bpawns = 0

    # For loop to check every thing in the board
    for square, piece in board.items():
        # Count kings
        if piece == 'bK':
            bkings += 1
        elif piece == 'wK':
            wkings += 1i
        # Count pieces
        if piece[0] == 'b':
            bpieces += 1
        elif piece[0] == 'w':
            wpieces += 1
        # Count pawns
        if piece[0] == 'bP':


    # Check kings
    if bkings == 1 and wkings == 1:
        validation['kings'] = True
    else: 
        print('There is an incorrect number of kings')
    # Check 16 pieces
    if bpieces == 16 and wpieces == 16:
        validation['number'] = True
    else:
        print('There are too many pieces')
        


    #def state
    if False in validation.values():
        state = False
    else:
        state = True
    return(state)



def print_chess_board(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            #print(x, y, is_white_square)  # DEBUG: Shows coordinates in order.
            if x + y in board.keys():
              squares.append(board[x + y])
            else:
              if is_white_square:
                squares.append(WHITE_SQUARE)
              else:
                squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))

def print_help():
    print('Interactive Chess Board')
    print('by Al Sweigart al@inventwithpython.com')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')


main_board = copy.copy(STARTING_PIECES)
print_help()
while True:
    print_chess_board(main_board)
    response = input('> ').split()

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'help':
        print_help()
    elif response[0] == 'quit':
        sys.exit()
