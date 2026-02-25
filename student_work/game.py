import curses

board = {
    'width': 21,
    'height': 14, 
    'bot': {'x': 1, 'y': 3},
    'player': {'x': 1, 'y': 3},
    'object': {'x': 1, 'y': 1},
    'split': 11,
      
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
            if x == board['player']['x'] and y == board['player']['y']:
                row += board['colorplayer']
                # Eagle
                # elif x == game_data['eagle_pos']['x'] and y == game_data['eagle_pos']['y']:
                #     row += game_data['eagle_icon']
                # Obstacles
                # elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
                #     row += game_data['obstacle']
                # # Collectibles
                # elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                #     row += game_data['leaf']
            else:
                row += board['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)