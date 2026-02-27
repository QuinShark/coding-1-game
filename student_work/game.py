import curses

board = {
    'width': 20,
    'height': 13, 
    'bot': {'x': 20, 'y': 13},
    'player': {'x': 0, 'y': 0},
    'object': {'x': 11, 'y': 0},
    # 'split': {'x': 7, 'y': 5},
      
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
                # elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                #     row += game_data['leaf']
            else:
                row += board['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)