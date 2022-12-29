print('Первый игрок размещает на поле одноклеточные корабли, \nВторой игрок угадывает их расположение\n')

def print_board(board):
    print("    A   B   C   D   E   F   G   H   I   J")
    print("--+---+---+---+---+---+---+---+---+---+---+")
    row_number = 0
    for row in board:
        print(" %d| %s | " % (row_number, " | ".join(row)))
        print("--+---+---+---+---+---+---+---+---+---+---+")
        row_number = row_number + 1

def ships_places (a):
  for n in range(a):
    print(f"В какую клетку поставить корабль {n + 1}?")
    s_column = input("Столбец от A до J: ")
    s_row = input("Строка от 0 до 9: ")
    if s_column.upper() not in "ABCDEFGHIJ":
        print("Столбец указан неверно, выбери значение от A до J")
        s_column = input("Столбец от A до J: ")
        s_row = input("Строка от 0 до 9: ")
    if s_row not in "0123456789":
        print("Строка указана неверно, выбери значение от 0 до 9")
        s_column = input("Столбец от A до J: ")
        s_row = input("Строка от 0 до 9: ")
    column_number = letters_to_numbers[s_column.upper()]
    row_number = int(s_row)
    if board[row_number][column_number] == 'X':
      print("Тут уже есть корабль, выбери другую клетку")
      print(f"В какую клетку поставить корабль {n + 1}?")
      s_column = input("Столбец от A до J: ")
      s_row = input("Строка от 0 до 9: ")
      column_number = letters_to_numbers[s_column.upper()]
      row_number = int(s_row)
    board[row_number][column_number] = 'X'
    print_board(board)
  fill_board = board
  return(fill_board)

def shooting(ships, compl_board):
  guesses = 0
  while guesses < ships:
    print("Где вражеский корабль?")
    column = input("Столбец от A до J: ")
    if column.upper() not in "ABCDEFGHIJ":
        print("Столбец указан неверно, выбери значение от A до J")
        column = input("Столбец от A до J: ")
    row = input("Строка от 0 до 9: ")
    if row not in "0123456789":
        print("Строка указана неверно, выбери значение от 0 до 9")
        row = input("Строка от 0 до 9: ")
    column_number = letters_to_numbers[column.upper()]
    row_number = int(row)
    if board[row_number][column_number] == 'X':
        print("\nПопал")
        g_board[row_number][column_number] = 'X'
        guesses = guesses + 1
    else:
        print("\nМимо")
        g_board[row_number][column_number] = '*'
    print_board(g_board) 

rows = 10
columns = 10
board = [[0 for x in range(columns)] for y in range(rows)]
for i in range(rows):
  for j in range(columns):
    board[i][j] = ' ' 
g_board = [[0 for x in range(columns)] for y in range(rows)]
for i in range(rows):
  for j in range(columns):
    g_board[i][j] = ' '
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

print_board(board)
ships_am = int(input("Сколько кораблей от 1 до 100 разместим? "))
ships_places(ships_am)
print("\n"*50)
print_board(g_board)
shooting(ships_am, board)
print("Конец игры!")