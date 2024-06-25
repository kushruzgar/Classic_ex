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
