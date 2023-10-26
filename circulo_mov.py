import math
import os

def clear_screen():
    # Esta función limpia la pantalla de la consola (solo funciona en sistemas compatibles)
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_circulo(radio, x, y, ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            distancia = math.sqrt((i - y) ** 2 + (j - x) ** 2)
            if distancia <= radio + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    radio = 5
    ancho = 20
    alto = 20
    x = ancho // 2
    y = alto // 2

    while True:
        clear_screen()
        dibujar_circulo(radio, x, y, ancho, alto)

        # Captura la entrada del usuario para mover el círculo
        move = input("Use las teclas 'W', 'A', 'S', 'D' para mover el círculo. Presione 'Q' para salir: ").upper()

        if move == 'W' and y > 0:
            y -= 1
        elif move == 'S' and y < alto - 1:
            y += 1
        elif move == 'A' and x > 0:
            x -= 1
        elif move == 'D' and x < ancho - 1:
            x += 1
        elif move == 'Q':
            break

if __name__ == "__main__":
    main()
