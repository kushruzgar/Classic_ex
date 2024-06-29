#  Заполнение матрицы по спирали

# Способ 1:

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
dx, dy, x, y = 0, 1, 0, 0

for i in range(1, n * m + 1):
    matrix[x][y] = i
    if matrix[(x + dx) % n][(y + dy) % m]:
        dx, dy = dy, -dx
    x += dx
    y += dy    
for line in matrix:
    print(*(f'{i:<3}' for i in line), sep='')



# Способ 2:

n, m = (int(i) for i in input().split())
spiral = []
x, y, dx, dy, k = 0, 0, 1, 0, 1
spiral = [[0]* n for _ in range(m)]
for i in range(1, n * m + 1):
    spiral[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < m and 0 <= ny < n and spiral[nx][ny] == 0:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy
for i in range(n):
    for j in range(m):
        print(str(spiral[j][i]).ljust(3), end=' ')
    print()


# Способ 3:

n, m = [int(i) for i in input().split()]
spiral = [[0] * m for _ in range(n)]
c = 1
for k in range(min(n // 2 + 1, m //2 + 1)):  
    for j in range(k, m - k):  
        if spiral[k][j] == 0:  
            spiral[k][j] = c 
            c += 1
    for i in range(1 + k, n - k):  
        if spiral[i][m - k - 1] == 0:
            spiral[i][m - k - 1] = c 
            c += 1
    for j in range(m - k - 2, k - 1, -1):  
        if spiral[n - k - 1][j] == 0:
            spiral[n - k - 1][j] = c 
            c += 1
    for i in range(n - k - 2, k, -1):  
        if spiral[i][k] == 0:
            spiral[i][k] = c 
            c += 1
for i in range(n):  
    for j in range(m):
        print(str(spiral[i][j]).ljust(3), end=' ')
    print()
