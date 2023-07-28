def paint(axis,init,final):
    if axis == x:
        for i in range(init,final+1):
            l[i][position[1]] = "*"
    else:
        for i in range(init,final+1):
            l[position[0]][i] = "*"

t = 0
while t == 0:
    t = 1
    inp = input("<-----RULES----->\n1. BRUSH DOWN\n2. BRUSH UP\n3. VEHICLE ROTATES RIGHT\n4. VEHICLE ROTATES LEFT\n5. MOVE UP TO X\n6. JUMP\n7. REVERSE DIRECTION\n8. VIEW THE MATRIX\n0. EXIT\nPlease enter the commands with a plus sign (+) between them.\n")
    inp = inp.split("+")

    while True:
        try:
            inp[0] = int(inp[0])
            break
        except:
            t = 0
            print("You entered an incorrect command. Please try again!")
            break
    
    if t == 0:
        continue

    if int(inp[0]) <= 0:
        t = 0
        print("You entered an incorrect command. Please try again!")

    if t == 0 :
        continue

    else:
        n = int(inp[0])+2
        l, l[0], l[-1] = [" "]*n, ["+"]*n, ["+"]*n

        for i in range(1,n-1):
            l[i], l[i][0], l[i][-1]  = [" "]*n, "+", "+"

        position, x, y, direction, brush, d = [1,1], 0, 0, 1, 0, 0

        for i in range(1,len(inp)):
            mov, initialpos = inp[i], position.copy()

            if mov == "1":
                brush, l[position[0]][position[1]] = 1, "*"
                continue
        
            elif mov == "2":
                brush = 0
                continue
        
            elif mov == "3":
                direction -= 1
                continue
        
            elif mov == "4":
                direction += 1
                continue
        
            elif mov == "5_":
                print("You entered an incorrect command. Please try again!")
                t = 0
                break

            elif mov[0:2] == "5_":
                x = int(mov[2:])
        
            elif mov == "6":
                brush ,x = 0, 3
        
            elif mov == "7":
                direction += 2
                continue

            elif mov == "8":
                plist = []
                for i in range(n):
                    for j in range(n):
                        plist.append(l[j][i])
                    print("".join(plist))
                    plist = []
                continue

            elif mov == "0":
                break

            else:
                print("You entered an incorrect command. Please try again!")
                t = 0
                break

            if direction == 1:
                pass

            elif direction == 0:
                direction = 4

            elif direction == 5:
                direction = 1

            elif direction == 6:
                direction = 2
        
            if direction == 1:
                pass

            elif direction == 2:
                y, x = -x, 0

            elif direction == 3:
                x = -x

            elif direction == 4:
                y, x = x, 0

            if x != 0:
                position[0] += x
                if 0 < position[0] <= n-2:
                    if brush == 1:
                        paint(x,position[0],initialpos[0]) if initialpos[0] > position[0] else paint(x,initialpos[0],position[0])
                else:
                    if x >= n-2 or x <= 2-n:
                        d = 1
                    position[0] = position[0] % (n-2)
                    if position[0] == 0:
                        position[0] = n-2
            
                    if brush == 1:
                        if d == 1:
                            paint(x,1,n-2)
                        elif direction == 1:
                            paint(x,initialpos[0],n-2)
                            paint(x,1,position[0])
                        elif direction == 3:
                            paint(x,1,initialpos[0])
                            paint(x,position[0],n-2)

            elif y != 0:
                position[1] += y
                if 0 < position[1] <= n-2:
                    if brush == 1:
                        paint(y,position[1],initialpos[1]) if initialpos[1] > position[1] else paint(y,initialpos[1],position[1])
                else:
                    if y >= n-2 or y <= 2-n:
                        d = 1
                    position[1] = position[1] % (n-2)
                    if position[1] == 0:
                        position[1] = 8
            
                    if brush == 1:
                        if d == 1:
                            paint(y,1,n-2)
                        if direction == 2:
                            paint(y,position[1],n-2)
                            paint(y,1,initialpos[1])
                        elif direction == 4:
                            paint(y,1,position[1])
                            paint(y,initialpos[1],n-2)
            x, y, d = 0, 0, 0