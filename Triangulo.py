import curses

# Inicializar la pantalla de curses
stdscr = curses.initscr()

# Configuración de la pantalla
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)

# Tamaño del triángulo
size = 5

# Coordenadas iniciales del triángulo
x = 0 
y = 0

# Función para dibujar un triángulo
def dibujar_triangulo(x, y, size):
    stdscr.clear()

    for i in range(size):
        for j in range(i * 2 + 1):
            stdscr.addch(y + i, x + j, '*')

    stdscr.refresh()

# Loop principal
while True:
    dibujar_triangulo(x, y, size)
    tecla = stdscr.getch()

    if tecla == ord('w') and y > 0:
        y -= 1
    elif tecla == ord('s') and y < curses.LINES - size:
        y += 1
    elif tecla == ord('a') and x > 0:
        x -= 1
    elif tecla == ord('d') and x < curses.COLS - size * 2:
        x += 1
    elif tecla == ord('q'):
        break

# Restaurar la configuración de la terminal
curses.endwin()