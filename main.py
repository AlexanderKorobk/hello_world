n = 4
matrix = [['-'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j != 0:
            matrix[i][j] = j - 1
        elif j == 0 and i != 0:
            matrix[i][j] = i - 1
        elif i == 0 and j == 0:
            matrix[i][j] = " "


def hello():
    print("Крестики - Нолики!")
    print("Для выбора клетки введите 2 цифры через пробел")


def show():
    for r in range(n):
        for c in range(n):
            print(matrix[r][c], end=' ')
        print()


def ask():
    while True:
        coord = input("Ввод: ").split()
        if len(coord) != 2:
            print("Введите 2 координаты!")
            continue

        if not (coord[0].isdigit()) or not (coord[1].isdigit()):
            print("Введите цифры")
            continue

        x, y = [int(i) for i in coord]

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Введите правильные координаты!!!")
            continue
        if matrix[x + 1][y + 1] != '-':
            print("Выберите другую клетку!!!")
            continue
        return x, y


def check_win():
    for i in range(n):
        if matrix[i][1:] == ["X", "X", "X"]:
            print("Выйграл Крестик")
            return True
        elif matrix[i][1:] == ["O", "O", "O"]:
            print("Выйграл Нолик")
            return True
    if [matrix[1][1] + matrix[2][1] + matrix[3][1]] == ["XXX"] or \
            [matrix[1][2] + matrix[2][2] + matrix[3][2]] == ["XXX"] or \
            [matrix[1][3] + matrix[2][3] + matrix[3][3]] == ["XXX"] or \
            [matrix[1][1] + matrix[2][2] + matrix[3][3]] == ["XXX"] or \
            [matrix[1][3] + matrix[2][2] + matrix[3][1]] == ["XXX"]:
        print("Выйграл Крестик")
        return True
    elif [matrix[1][1] + matrix[2][1] + matrix[3][1]] == ["OOO"] or \
            [matrix[1][2] + matrix[2][2] + matrix[3][2]] == ["OOO"] or \
            [matrix[1][3] + matrix[2][3] + matrix[3][3]] == ["OOO"] or \
            [matrix[1][1] + matrix[2][2] + matrix[3][3]] == ["OOO"] or \
            [matrix[1][3] + matrix[2][2] + matrix[3][1]] == ["OOO"]:
        print("Выйграл Нолик")
        return True

    return False


hello()
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()
    if count % 2 == 1:
        matrix[x + 1][y + 1] = 'X'
    else:
        matrix[x + 1][y + 1] = 'O'

    if check_win():
        break

    if count == 9:
        print("Ничья")
        break

print("Молодец")
