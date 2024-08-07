# Магические квадраты издавна интриговали воображение людей: дата изготовления древнейшей сохранившейся таблицы относится к 2200 г. до н.э. 
# Магический квадрат – это квадратная таблица размера n х n, составленная из всех чисел 1, 2, 3 … n2 таким образом, что суммы по каждому столбцу, каждой строке и каждой диагонали равны между собой. 
# Напишем программу, которая определяет, можно ли считать матрицу магическим квадратом.

#Пример ввода
# 3
# 8 1 6
# 3 5 7
# 4 9 2

#Пример вывода
# YES


# Способ 1:

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if all(i in sum(matrix,[]) for i in range(1, n**2 + 1)):
    print('YES' if all(sum(i) == sum(j) == sum([matrix[i][i] for i in range(n)]) == sum([matrix[n-i-1][i] for i in range(n)]) for i in matrix for j in list(map(list, zip(*matrix)))) else 'NO')
else:
    print('NO')


# Способ 2 – с магической константой и множествами:

n = int(input())
square = [[*map(int, input().split())] for _ in range(n)]
m_const = n * (1 + n ** 2) // 2                                                      
print(('NO', 'YES')[all(sum(el) == m_const for x in (((square[i][i] for i in range(n)),(square[i][~i] for i in range(n))), square, zip(*square)) for el in x) and set(sum(square, [])) == set(range(1, n ** 2 + 1))])

