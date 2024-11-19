import curses
import time

def mostrar_clima(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    counter = 0
    temperature = 0

    while True:
        stdscr.clear()
        stdscr.addstr(1, 0,  f"Cuenta actual: {counter}", curses.color_pair(1))
        stdscr.addstr(1, 20, f"Cuenta actual: {temperature}", curses.color_pair(2))
        stdscr.addstr(1, 40, f"Cuenta actual: {counter}", curses.color_pair(3))
        stdscr.refresh()
        counter += 1
        temperature = counter *2
        time.sleep(1)

# Main code start here

curses.wrapper(mostrar_clima)