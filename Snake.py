from __future__ import print_function
from termcolor import colored
import random



class Pole:  # Klasa Pole i jego incjalizacja
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.owoc = None
        self.map = [['#' for i in range(x)] for y in range(y)]
        next = ['1']
        for col in range(2, self.x, 4):
            self.map[1][col] = " "
            self.map[1][col + 1] = " "
            self.map[-2][col] = " "
            self.map[-2][col + 1] = " "
        for row in range(2, self.y - 2):
            for col in range(0, self.x):
                if next[-1] == '2' and col != 0 and col != 1 and col != self.x - 2 and col != self.x - 1:
                    self.map[row][col] = " "

                elif next[-1] == '1' and col != 0 and col != self.x - 1:
                    self.map[row][col] = " "

                elif next[-1] == '3' and col != 0 and col != 1 and col != 2 and col != self.x - 1 and \
                        col != self.x - 2 and col != self.x - 3:
                    self.map[row][col] = " "

            if next[-1] == '1' or next[-1] == '3':
                next.append('2')
            elif next[-1] == '2':
                if next[-2] == '1':
                    next.append('3')
                else:
                    next.append('1')

    def rysuj(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.map[i][j] == "s":
                    print(colored(self.map[i][j], "yellow"), end="")
                elif self.map[i][j] == "o":
                    print(colored(self.map[i][j], "blue"), end="")
                elif self.map[i][j] == "w":
                    print(colored(self.map[i][j], "green"), end="")
                else:
                    print(colored(self.map[i][j], "red"), end="")
            print("")

    def dodaj(self, x, y, znak):
        self.map[y][x] = znak
        self.map[y + 1][x] = znak
        self.map[y - 1][x] = znak
        self.map[y][x - 1] = znak
        self.map[y][x + 1] = znak
        self.map[y - 1][x + 1] = znak
        self.map[y + 1][x + 1] = znak
        self.map[y][x + 2] = znak


class Snake(Pole):
    def __init__(self, x, y, map, gracz):
        self.map = map
        self.x = x
        self.y = y
        self.body = []
        self.gracz = gracz
        self.body.append(self.x)
        self.body.append(self.y)
        if gracz == 1:
            self.dodaj(x, y, "s")
        else:
            self.dodaj(x, y, "w")


class Owoc(Pole):
    def __init__(self, x, y, map):
        self.map = map
        self.x = x
        self.y = y
        self.dodaj(x, y, "o")


def hexagon(x, y):
    coordinates = [[x, y], [x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y], [x + 1, y - 1], [x + 1, y + 1],
                   [x + 2, y]]
    return coordinates


def ruch(pole, snake, owoc, komenda, gracz):
    valid = False
    if gracz == 1:
        if komenda == 'g':
            snake.x -= 4
        elif komenda == 'j':
            snake.x += 4
        elif komenda == 't':
            snake.x -= 2
            snake.y -= 2
        elif komenda == 'u':
            snake.x += 2
            snake.y -= 2
        elif komenda == 'b':
            snake.x -= 2
            snake.y += 2
        elif komenda == 'm':
            snake.x += 2
            snake.y += 2
    elif gracz == 2:
        if komenda == 'a':
            snake.x -= 4
        elif komenda == 'd':
            snake.x += 4
        elif komenda == 'q':
            snake.x -= 2
            snake.y -= 2
        elif komenda == 'e':
            snake.x += 2
            snake.y -= 2
        elif komenda == 'z':
            snake.x -= 2
            snake.y += 2
        elif komenda == 'c':
            snake.x += 2
            snake.y += 2

    owo, przeszk = is_valid([snake.x, snake.y], 0, pole, "snake", gracz)

    if przeszk:
        return True
    elif not owo:
        pole.dodaj(snake.body[0], snake.body[1], " ")
        snake.body.pop(0)
        snake.body.pop(0)
        snake.body.append(snake.x)
        snake.body.append(snake.y)
        if gracz == 1:
            pole.dodaj(snake.x, snake.y, "s")
        else:
            pole.dodaj(snake.x, snake.y, "w")
        return False
    else:
        if gracz == 1:
            pole.dodaj(snake.x, snake.y, "s")
        else:
            pole.dodaj(snake.x, snake.y, "w")
        snake.body.append(snake.x)
        snake.body.append(snake.y)
        while not valid:
            x = random.randint(1, pole.x - 1)
            y = random.randint(1, pole.y - 1)
            valid, pole.owoc = is_valid([x, y], 1, pole, 'owoc', 0)
        return False


def valid_hex(new, pole):
    a, b = False, False
    for i in range(pole.x):
        if pole.map[new[1]][i] == "#":
            if (new[0] % 4) == i + 2:
                a = True
    for i in range(pole.y):
        if pole.map[i][new[0]] == "#":
            if (new[1] % 4) == i + 2:
                b = True

    if a == True and b == True:
        return True
    else:
        return False


def is_valid(new, create, pole, type, gracz):
    hasz, owoc = False, False
    new_cord = hexagon(new[0], new[1])

    if create:
        if not valid_hex(new, pole):
            return False, False
        for i, j in new_cord:
            if pole.map[j][i] == 's' or pole.map[j][i] == '#' or pole.map[j][i] == 'o' or pole.map[j][i] == 'w':
                return False, False
        if type == 'snake':
            snake = Snake(new[0], new[1], pole.map, gracz)
            return True, snake
        else:
            owoc = Owoc(new[0], new[1], pole.map)
            owoc.x = new[0]
            owoc.y = new[1]
            return True, owoc
    else:
        try:
            for i, j in new_cord:
                if pole.map[j][i] == 's' or pole.map[j][i] == '#' or pole.map[j][i] == 'w':
                    hasz = True
                elif pole.map[j][i] == 'o':
                    owoc = True
            if hasz:
                return False, True
            elif owoc:
                return True, False
            else:
                return False, False
        except:
            return False, True
