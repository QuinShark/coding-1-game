# imports
import curses
import random
import time

# player data
board = {
    'width': 20,
    'height': 13, 
    'bot': {'x': 0, 'y': 0,  "score": 0},
    'player': {'x': 15, 'y': 0,  "score": 0},
    'object': {'x': 0, 'y': range(1,1)},
    # 'split': {'x': 0, 'y': range(2,5)},
    
    'colorbot': "||",
    'colorplayer': "||",
    'colorobject': "\U00002B1C",
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
            elif x == board['player']['x'] and y == board['player']['y']:
                row += board['colorplayer']
                # Bot
            elif x == board['bot']['x'] and y == board['bot']['y']:
                row += board['colorbot']
                # Empty
            else:
                row += board['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))
    # WORDS - Score Edition
    stdscr.addstr(board['height'] + 1, 0,
                  f"Player Score: {board['player']['score']} Bot Score: {board['bot']['score']}",
                  curses.color_pair(1))
    try:     # WORDS - Instruction Edition
        stdscr.addstr(board['height'] + 2, 0,
                  "Move with W for UP and S for DOWN, Q to quit",
                  curses.color_pair(1))
    except curses.error:
        pass
    stdscr.refresh()

#    stdscr.refresh()
 #   stdscr.getkey()  # pause so player can see board

def move_player(key):
    x = board['player']['x']
    y = board['player']['y']

    new_x, new_y = x, y
    key = key.lower()

  #  while True:
    if key == "w" and y > 0:
            new_y -= 1
    elif key == "s" and y < board['height'] - 1:
            new_y += 1
    board['player']['x'] = new_x
    board['player']['y'] = new_y
    board['player']['score'] += 1

# Bot is currently random, plz sync up to player/ball movement
def move_bot():
    directions = [(0, -1), (0, 1)]
    random.shuffle(directions)
    #ex, ey = board['bot']['x'], board['bot']['y']
    ey = board['bot']['y']

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

            move_player(key)
            move_player_2(key)
            #move_bot()

            draw_board(stdscr)
            #time.sleep(0.2)
curses.wrapper(main) 

#there's totally a diffferent trst