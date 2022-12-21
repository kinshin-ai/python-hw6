#Разметка игрового поля
board = [[' ','',''],
         [' ','',''],
         [' ','','']]
rows = len(board)
cols = len(board)
print("-----------")
for i in range(rows):
  print(board[i][0], " |", board[i][1], " |", board[i][2])
  print("-----------")
#кто чем играет
player_1 = input("игрок 1, выбери символ: Х или 0 ")
if player_1 == "X":
  player_2 = "O"
  print("игрок 2 играет O ")
else:
  player_2 = "X"
  print("игрок 2 играет X \n")

#ход игры
count = 0
winner = None
while count < 10:
  if count % 2 == 0:
        player = player_1
  elif count % 2 == 1:
        player = player_2
  print(f"игрок {player}, твой ход")
  row = int(input("выбери строку: верхняя: 0, средняя: 1, нижняя: 2  "))
  column = int(input("выбери столбец: левый: 0, средний: 1, правый: 2  "))
  #проверка клетки и границ поля
  if row > 2 or row < 0 or column > 2 or column < 0:
    #некорректно работатет после первой итерации??
    print("вне поля, выбери другую клетку")
    row = int(input("выбери строку: верхняя: 0, средняя: 1, нижняя: 2  "))
    column = int(input("выбери столбец: левый: 0, средний: 1, правый: 2  "))
  elif (board[row][column] == player_1) or (board[row][column] == player_2):
    print("клетка занята, выбери другую")
    row = int(input("выбери строку: верхняя: 0, средняя: 1, нижняя: 2  "))
    column = int(input("выбери столбец: левый: 0, средний: 1, правый: 2  "))

  if player == player_1:
    board[row][column] = player_1    
  else:
    board[row][column] = player_2
  print("-----------")
  for i in range(rows):
    print(board[i][0], " |", board[i][1], " |", board[i][2])
    print("-----------")
  #проверка выигрыша по строкам, столбцам, диагоналям
  for row in range (0, 3):
     if (board[row][0] == board[row][1] == board[row][2] == player_1):
      winner = player_1
      print(f"игрок {player_1} победил")
      count = 10
     elif (board[row][0] == board[row][1] == board[row][2] == player_2):
       winner = player_2
       print(f"игрок {player_2} победил")
       count = 10
  for col in range (0, 3):
    if (board[0][col] == board[1][col] == board[2][col] == player_1):
      winner = player_1
      print(f"игрок {player_1} победил")
      count = 10
    elif (board[0][col] == board[1][col] == board[2][col] == player_2):
      winner = player_2
      print(f"игрок {player_2} победил")
      count = 10
  if board[0][0] == board[1][1] == board[2][2] == player_1:
    winner = player_1 
    print(f"игрок {player_1} победил")
    count = 10
  elif board[0][0] == board[1][1] == board[2][2] == player_2:
    winner = player_2
    print(f"игрок {player_2} победил")
    count = 10
  elif board[0][2] == board[1][1] == board[2][0] == player_1:
    winner = player_1
    print(f"игрок {player_1} победил")
    count = 10
  elif board[0][2] == board[1][1] == board[2][0] == player_2:
    winner = player_2
    print(f"игрок {player_2} победил")
    count = 10
  count += 1

if winner == None:
    print("Ничья")
print("конец игры")