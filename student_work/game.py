# imports
import curses
import random
import time

# player data
board = {
    'width': 21,
    'height': 13, 
    #'bot': {'x': 0, 'y': 0,  "score": 0},
    'player_1': {'x': 0, 'y': 0,  "score": 0},
    'player_2': {'x': 16, 'y': 0,  "score": 0},
    'object': {'x': 0, 'y': 9},
    'split1': {'x': 8, 'y': 0},
    'split2': {'x': 8, 'y': 1},
    'split3': {'x': 8, 'y': 2},
    'split4': {'x': 8, 'y': 3},
    'split5': {'x': 8, 'y': 4},
    'split6': {'x': 8, 'y': 5},
    'split7': {'x': 8, 'y': 6},
    'split8': {'x': 8, 'y': 7},
    'split9': {'x': 8, 'y': 8},
    'split10': {'x': 8, 'y': 9},
    'split11': {'x': 8, 'y': 10},
    'split12': {'x': 8, 'y': 11},
    'split13': {'x': 8, 'y': 12},
    'split14': {'x': 8, 'y': 14},

    'colorplayer_2': "||",
    'colorplayer_1': "||",
    'colorobject': ".",
    'colorsplit': ".",
    'colorsplit1': ".",
    'colorsplit2': ".",
    'colorsplit3': ".",
    'colorsplit4': ".",
    'colorsplit5': ".",
    'colorsplit6': ".",
    'colorsplit7': ".",
    'colorsplit8': ".",
    'colorsplit9': ".",
    'colorsplit10': ".",
    'colorsplit11': ".",
    'colorsplit12': ".",
    'colorsplit13': ".",
    'colorsplit14': ".",
                        
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
            elif x == board['split1']['x'] and y == board['split1']['y']:
                row += board['colorsplit1']
            elif x == board['split2']['x'] and y == board['split2']['y']:
                row += board['colorsplit2']
            elif x == board['split3']['x'] and y == board['split3']['y']:
                row += board['colorsplit3']
            elif x == board['split4']['x'] and y == board['split4']['y']:
                row += board['colorsplit4']
            elif x == board['split5']['x'] and y == board['split5']['y']:
                row += board['colorsplit5']
            elif x == board['split6']['x'] and y == board['split6']['y']:
                row += board['colorsplit6']
            elif x == board['split7']['x'] and y == board['split7']['y']:
                row += board['colorsplit7']
            elif x == board['split8']['x'] and y == board['split8']['y']:
                row += board['colorsplit8']
            elif x == board['split9']['x'] and y == board['split9']['y']:
                row += board['colorsplit9']
            elif x == board['split10']['x'] and y == board['split10']['y']:
                row += board['colorsplit10']
            elif x == board['split11']['x'] and y == board['split11']['y']:
                row += board['colorsplit11']
            elif x == board['split12']['x'] and y == board['split12']['y']:
                row += board['colorsplit12']
            elif x == board['split13']['x'] and y == board['split13']['y']:
                row += board['colorsplit13']
            elif x == board['split14']['x'] and y == board['split14']['y']:
                row += board['colorsplit14']
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
def move_object():
    directions = [(0, -1), (0, 1)]
    random.shuffle(directions)
    #ex, ey = board['bot']['x'], board['bot']['y']
    ey = board['object']['y']

    for dx, dy in directions:
        #new_x = ex + dx
        new_y = ey + dy
        if 0 <= new_y < board['height']:
                 board['object']['y'] = new_y
                 break
    #board['bot']['x'] = new_x
    board['object']['y'] = new_y
    board['object']['score'] += 1

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