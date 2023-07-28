import sys

def func_row(isFirstTurn,direction,row_f,column_f):
    global score
    row_f += direction
    
    if len(matrix) > row_f >= 0:
        prevCell = startingPoint if isFirstTurn else matrix[row_f-direction][column_f]
        cell = matrix[row_f][column_f]

        if cell == prevCell:
            score += value[matrix[row_f-direction][column_f]]
            matrix[row_f-direction][column_f] = " "
            func_row(False,direction,row_f,column_f)
            func_column(True,1,row_f,column_f)
            func_column(True,-1,row_f,column_f)

        else:
            row_f = row_f-direction
            if not isFirstTurn:
                score += value[matrix[row_f][column_f]]
                matrix[row_f][column_f] = " "

    else:
        row_f = row_f-direction
        if not isFirstTurn:
            score += value[matrix[row_f][column_f]]
            matrix[row_f][column_f] = " "

def func_column(isFirstTurn,direction,row_f,column_f):
    global score
    column_f += direction
    
    if len(matrix[0]) > column_f >= 0:
        prevCell = startingPoint if isFirstTurn else matrix[row_f][column_f-direction]
        cell = matrix[row_f][column_f]

        if cell == prevCell:
            score += value[matrix[row_f][column_f-direction]]
            matrix[row_f][column_f-direction] = " "
            func_column(False,direction,row_f,column_f)
            func_row(True,1,row_f,column_f)
            func_row(True,-1,row_f,column_f)

        else:
            column_f = column_f-direction
            if not isFirstTurn:
                score += value[matrix[row_f][column_f]]
                matrix[row_f][column_f] = " "

    else:
        column_f = column_f-direction
        if not isFirstTurn:
            score += value[matrix[row_f][column_f]]
            matrix[row_f][column_f] = " "

def bomb(row_f,column_f):
    global score
    matrix[row_f][column_f] = " "

    for i in range(len(matrix[0])):
        score += value[matrix[row_f][i]]
        if matrix[row_f][i] == "X":
            matrix[row_f][i] = " "
            bomb(row_f,i)
        else:
            matrix[row_f][i] = " "

    for i in range(len(matrix)):
        score += value[matrix[i][column_f]]
        if matrix[i][column_f] == "X":
            matrix[i][column_f] = " "
            bomb(i,column_f)
        else:
            matrix[i][column_f] = " "

score = 0
value = {'B':9, 'G':8, 'W':7, 'Y':6, 'R':5, 'P':4, 'O':3, 'D':2, 'F':1, 'X':0, ' ':0}

with open(sys.argv[1]) as inpFile:
    matrix = [line.split() for line in inpFile]

for row in matrix:
    print(" ".join(row))

print(f"\nYour score is: {score}")

while True:
    while True:
        try:
            inp = input("\nPlease enter a row and column number: ").split()
            assert len(inp) == 2
            assert float(inp[0])%1 == 0 and float(inp[1])%1 == 0
            row, column = int(inp[0]), int(inp[1])
            assert 0 <= row < len(matrix) and 0 <= column < len(matrix[0])
            break

        except KeyboardInterrupt:
            raise KeyboardInterrupt

        except:
            print("\nPlease enter a valid size!")

    startingPoint = matrix[row][column]

    if startingPoint == "X":
        bomb(row,column)
    elif startingPoint == " ":
        pass
    else:
        func_row(True,1,row,column)
        func_row(True,-1,row,column)
        func_column(True,1,row,column)
        func_column(True,-1,row,column)

    # if a cell is empty, shifts the upper cells downward
    for column in range(len(matrix[0])):
        for row in range(len(matrix)-1,0,-1):
            for i in range(len(matrix)):
                if matrix[row][column] == " ":
                    for row2 in range(row,0,-1):
                        matrix[row2][column] = matrix[row2-1][column]
                        matrix[row2-1][column] = " "
                else:
                    break

    # deletes an empty row
    checkValue = [" " for i in range(len(matrix[0]))]
    tempMatrix = []
    for row in matrix:
        if row != checkValue:
            tempMatrix.append(row)
    matrix = tempMatrix.copy()

    if len(matrix) == 0:
        print(f"\nYour score is: {score}")
        break

    # if a column is empty, shifts the columns at right to the left
    columnList = []
    checkValue = [" " for i in range(len(matrix))]
    counter = 0
    for column in range(len(matrix[0])):
        columnList = []
        for row in matrix:
            columnList.append(row[column-counter])
        if columnList == checkValue:
            for row in range(len(matrix)):
                matrix[row].pop(column-counter)
            counter += 1

    print()
    for row in matrix:
        print(" ".join(row))

    print(f"\nYour score is: {score}")

    # Final check for possible moves
    isEnd = True

    if len(matrix) == 0:
        break

    if len(matrix) == 1 and len(matrix[0]) == 1:
        break

    for column in range(len(matrix[0])-1):
        for row in range(len(matrix)-1):
            if ((matrix[row][column] == matrix[row+1][column] or matrix[row][column] == matrix[row][column+1]) and matrix[row][column] != " ") or matrix[row][column] == "X":
                isEnd = False
                break
        if not isEnd:
            break

    for column in range(len(matrix[0])-1):
        row = len(matrix)-1
        if (matrix[row][column] == matrix[row][column+1] and matrix[row][column] != " ") or matrix[row][column] == "X":
            isEnd = False
            break

    for row in range(len(matrix)-1):
        column = len(matrix[0])-1
        if (matrix[row][column] == matrix[row+1][column] and matrix[row][column] != " ") or matrix[row][column] == "X":
            isEnd = False
            break

    if isEnd:
        break

print("\nGame over!")