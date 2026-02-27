import curses

board = {
    'width': 20,
    'height': 13, 
    'bot': {'x': 10, 'y': 9},
    'player': {'x': 0, 'y': 0},
    'object': {'x': 10, 'y': 10},
    'split': {'x': 10, 'y': range(2, 5)},
    # 'split': {'x': 10, 'y': 2},
    # 'split': {'x': 10, 'y': 3},  
        # ASCII icons
    'colorbot': "\U00002B1C",
    'colorplayer': "\U00002B1C",
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
            elif x == board['split']['x'] and y == board['split']['y']:
                row += board['colorsplit']
            else:
                row += board['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)