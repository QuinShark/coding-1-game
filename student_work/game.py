# imports
import curses
import random
import time

# player data
board = {
    'width': 20,
    'height': 13, 
    #'bot': {'x': 0, 'y': 0,  "score": 0},
    'player_1': {'x': 0, 'y': 0,  "score": 0},
    'player_2': {'x': 15, 'y': 0,  "score": 0},
    'object': {'x': 0, 'y': range(1,1)},
    # 'split': {'x': 0, 'y': range(2,5)},
    
    'colorplayer_2': "||",
    'colorplayer_1': "||",
    'colorobject': ".",
    'colorsplit': "\U00002B1C",
    'empty': "  "
}
def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
   
    stdscr.clear()
    for y in range(board['height']):
        row = ""
        # all things on screen
        for x in range(board['width']):
                # Object
            if x == board['object']['x'] and y == board['object']['y']:
                row += board['colorobject']
                # Player
            elif x == board['player_1']['x'] and y == board['player_1']['y']:
                row += board['colorplayer_1']
                # Bot
            elif x == board['player_2']['x'] and y == board['player_2']['y']:
                row += board['colorplayer_2']
                # Empty
            else:
                row += board['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))
    # WORDS - Score Edition
    stdscr.addstr(board['height'] + 1, 0,
                  f"Player 1 Score: {board['player_1']['score']} Player 2 Score: {board['player_2']['score']}",
                  curses.color_pair(1))
    try:     # WORDS - Instruction Edition
        stdscr.addstr(board['height'] + 2, 0,
                  "Player 1: Move with W for UP and S for DOWN. Player 2: Move with I and K. Both: Q to quit",
                  curses.color_pair(1))
    except curses.error:
        pass
    stdscr.refresh()

#    stdscr.refresh()
 #   stdscr.getkey()  # pause so player can see board

def move_player_1(key):
    x = board['player_1']['x']
    y = board['player_1']['y']

    new_x, new_y = x, y
    key = key.lower()

  #  while True:
    if key == "w" and y > 0:
            new_y -= 1
    elif key == "s" and y < board['height'] - 1:
            new_y += 1
    board['player_1']['x'] = new_x
    board['player_1']['y'] = new_y
    board['player_1']['score'] += 1

# Bot is currently random, plz sync up to player/ball movement
# def move_bot():
#     directions = [(0, -1), (0, 1)]
#     random.shuffle(directions)
#     #ex, ey = board['bot']['x'], board['bot']['y']
#     ey = board['bot']['y']

#     for dx, dy in directions:
#         #new_x = ex + dx
#         new_y = ey + dy
#         if 0 <= new_y < board['height']:
#                  board['bot']['y'] = new_y
#                  break
#     #board['bot']['x'] = new_x
#     board['bot']['y'] = new_y
#     board['bot']['score'] += 1

def move_player_2(key):
    x = board['player_2']['x']
    y = board['player_2']['y']

    new_x, new_y = x, y

  #  while True:
    if key == "i" and y > 0:
            new_y -= 1
    elif key == "k" and y < board['height'] - 1:
            new_y += 1
    board['player_2']['x'] = new_x
    board['player_2']['y'] = new_y
    board['player_2']['score'] += 1

# runs like all the functions
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
            #stdscr.keypad(True)
            #alt_key = stdscr.getch()
            #stdscr.addstr(0, 0, '%s' % key == curses.KEY_UP)
        except:
            key = None
            #alt_key = None

        if key:
            if key.lower() == "q":
                break

            move_player_1(key)
            move_player_2(key)
            #move_bot()

            draw_board(stdscr)
            #time.sleep(0.2)
curses.wrapper(main) 

#there's totally a diffferent trst