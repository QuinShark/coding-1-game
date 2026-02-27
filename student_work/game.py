import curses

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
        for x in range(board['width']):
                # Player
            if x == board['object']['x'] and y == board['object']['y']:
                row += board['colorobject']
                # Eagle
            elif x == board['player']['x'] and y == board['player']['y']:
                row += board['colorplayer']
                # Obstacles
            elif x == board['bot']['x'] and y == board['bot']['y']:
                row += board['colorbot']
                # # Collectibles
            # elif x == board['split']['x'] and y == board['split']['y']:
            #     row += board['colorsplit']
                # elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                #     row += game_data['leaf']
            else:
                row += board['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.addstr(board['height'] + 1, 0,
                  f"Player Score: {board['player']['score']} Bot Score: {board['bot']['score']}",
                  curses.color_pair(1))
    stdscr.addstr(board['height'] + 2, 0,
                  "Move with W for UP and S for DOWN, Q to quit",
                  curses.color_pair(1))
    stdscr.refresh()

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            draw_board(stdscr)

curses.wrapper(main) 