def pythonTest():
    N = 5

    x,y = 1,1

    #  R, L, D, U
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    move_type = ["R", "L", "D", "U"]

    arr = ["R","R","R","D","D"]

    for i in arr:
        for j in range(len(move_type)):
            if i == move_type[j]:
                nx = dx[j] + x
                ny = dy[j] + y
                if 1 <= nx <= N and 1 <= ny<= N:
                    x = nx
                    y = ny

    print(x,y)
