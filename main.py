#Морской бой: один игрок размещает на поле одноклеточные корабли, второй игрок угадывает их расположение

#рисуем игровое поле
rows = 10
columns = 10
board = [[0 for x in range(columns)] for y in range(rows)]
for i in range(rows):
  for j in range(columns):
    board[i][j] = ' '
    
#разметка сетки
print("    A   B   C   D   E   F   G   H   I   J")
print("--+---+---+---+---+---+---+---+---+---+---+")
for i in range(rows):
  print(i, '|', board[i][0], "|", board[i][1], "|", board[i][2], "|", board[i][3], "|", board[i][4], "|", board[i][5], "|", board[i][6], "|", board[i][7], "|", board[i][8], "|", board[i][9], '|')
  print("--+---+---+---+---+---+---+---+---+---+---+")

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

#блок размещения кораблей
for n in range(5):
    print("в какую клетку  ", n + 1, "?")
    s_column = input("column (A to J):")
    s_row = input("row (0 to 9):")
    if s_column not in "ABCDEFGHIJ":
        print("That column is wrong! It should be A - J")
        s_column = input("column (A to J):")
        s_row = input("row (0 to 9):")
    if s_row not in "0123456789":
        print("That row is wrong! it should be 0 - 9")
        s_column = input("column (A to J):")
        s_row = input("row (0 to 9):")

    column_number = letters_to_numbers[s_column]
    
    row_number = int(s_row)
    if board[row_number][column_number] == 'X':
      print("That spot already has a battleship in it!")
      print("Where do you want ship ", n + 1, "?")
      s_column = input("column (A to J):")
      s_row = input("row (1 to 10):")
      column_number = letters_to_numbers[s_column]
      row_number = int(s_row)
        
    board[row_number][column_number] = 'X'
      
    print("    A   B   C   D   E   F   G   H   I   J")
    print("--+---+---+---+---+---+---+---+---+---+---+")
    for i in range(rows):
      print(i, '|', board[i][0], "|", board[i][1], "|", board[i][2], "|", board[i][3], "|", board[i][4], "|", board[i][5], "|", board[i][6], "|", board[i][7], "|", board[i][8], "|", board[i][9], '|')
      print("--+---+---+---+---+---+---+---+---+---+---+")

print("\n"*50)


g_board = [[0 for x in range(columns)] for y in range(rows)]

for i in range(rows):
  for j in range(columns):
    g_board[i][j] = ' '
    
#print the board
print("    A   B   C   D   E   F   G   H   I   J")
print("--+---+---+---+---+---+---+---+---+---+---+")
for i in range(rows):
  print(i, '|', g_board[i][0], "|", g_board[i][1], "|", g_board[i][2], "|", g_board[i][3], "|", g_board[i][4], "|", g_board[i][5], "|", g_board[i][6], "|", g_board[i][7], "|", g_board[i][8], "|", g_board[i][9], '|')
  print("--+---+---+---+---+---+---+---+---+---+---+")

guesses = 0
while guesses < 5:
    print("Guess a battleship location")
    column = input("column (A to J):")

    if column not in "ABCDEFGHIJ":
        print("That column is wrong! It should be A - J")

    row = input("row (0 to 9):")

    if row not in "0123456789":
        print("That row is wrong! it should be 0 - 9")

    column_number = letters_to_numbers[column]
    row_number = int(row)

    if board[row_number][column_number] == 'X':
        print("HIT!")
        g_board[row_number][column_number] = 'X'
        guesses = guesses + 1
    else:
        print("MISS!")
        g_board[row_number][column_number] = '*'
    print("    A   B   C   D   E   F   G   H   I   J")
    print("--+---+---+---+---+---+---+---+---+---+---+")
    for i in range(rows):
      print(i, '|', g_board[i][0], "|", g_board[i][1], "|", g_board[i][2], "|", g_board[i][3], "|", g_board[i][4], "|", g_board[i][5], "|", g_board[i][6], "|", g_board[i][7], "|", g_board[i][8], "|", g_board[i][9], '|')
      print("--+---+---+---+---+---+---+---+---+---+---+")

print("GAME OVER!")