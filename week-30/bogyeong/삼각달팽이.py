def solution(n): # if, n=4
    triangle = [[0] * (i + 1) for i in range(n)] # [[0],[0,0],[0,0,0],[0,0,0,0]]
    num = 1
    x, y = -1, 0

    # answer = [[0],[0,0],[0,0,0],[0,0,0,0]]
    # sort: 1 2 3 4 5 6 7 8 9 10
    # triangle = [[1],[2,9],[3,10,8],[4,5,6,7]]
    # goal: [1,2,9,3,10,8,4,5,6,7]
    
    for i in range(n): # 0 1 2 3
        for _ in range(i, n): #(0*4), (1*3), (2*2), (3*1)
            if i % 3 == 0:      # 아래로
                x += 1
            elif i % 3 == 1:    # 오른쪽으로
                y += 1
            else:               # 위왼쪽 대각선으로
                x -= 1
                y -= 1

            triangle[x][y] = num
            num += 1

    # triangle = [[1],[2,9],[3,10,8],[4,5,6,7]]
    # goal: [1,2,9,3,10,8,4,5,6,7]
    goal = []
    for row in triangle:
        goal.extend(row)

    return goal
