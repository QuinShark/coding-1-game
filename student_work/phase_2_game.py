import curses

board = {
    'width': 21,
    'height': 14, 
    'bot': [{'x': 1, 'y': 3}],
    'paddles': [{'x': 1, 'y': 3}],
    'object': [{'x': 1, 'y': 1.}],
    'split': 11
      
        # ASCII icons
    'bot': "\U00002B1C"
    'player': "\U00002B1C,
    'object': "\U00002B1C",
    'split': "\U00002B1C",
    'empty': "  "
}

print(board["bot"])