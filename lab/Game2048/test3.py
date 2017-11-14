# actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# actions_dict = dict(zip(letter_codes, actions * 2))
# width = 5
# line = '+' + ('!------' * width + '+')[0:]

# row = [0,0,0,0]
# '|{: ^5} '.format(num) if num > 0 else '|      ' for num in row
#
# width = 4
# height = 4
# field = [[0 for i in range(width)] for j in range(height)]
#
# print(field)

# row = [0, 2, 3, 0]
# t=[(1,2,3),(4,5,6),(11,22,33),(44,55,66)]
#
# # str = '-'.join('|{: ^20} '.format(num) if num > 0 else '|      ' for num in row) + '|'
#
# str = zip(*t)
#
# print([list(str)])

import curses
def main(stdscreen):
   curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
   curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
   curses.init_pair(3, curses.COLOR_MAGENTA,curses.COLOR_BLACK)
   stdscreen.clear()
   stdscreen.addstr(3,1,"  This is a test  ",curses.color_pair(1))
   stdscreen.addstr(4,1,"  This is a test  ",curses.color_pair(2))
   stdscreen.addstr(5,1,"  This is a test  ",curses.color_pair(3))
   stdscreen.refresh()
   stdscreen.getch()
curses.wrapper(main)