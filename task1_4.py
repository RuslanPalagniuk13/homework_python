'''
Задача 1:
Напишите функцию для транспонирования матрицы
'''

matrix_init = [[1, 2, 4, 5],
               [6, 7, 8, 9]]
print("Дана матрица: \n" + '\n'.join(list(map(str, matrix_init))))

# Короткое решение с использованием zip() (zip() возвращает элементы в картеже -> в списке !)
print("Транспонированная матрица (решение в одну строку с красивым выводом):\
 \n"+'\n'.join(list(map(str, [list(line) for line in zip(*matrix_init)]))))

#Функция для транспонирования матрицы
def transpose(matrix):
    res = []
    row = len(matrix)
    colum = len(matrix[0])
    for j in range(colum):
        tmp = []
        for i in range(row):
            tmp = tmp + [matrix[i][j]]
        res = res + [tmp]
    return res

# развернуто
print("Транспонированная матрица: \n"+'\n'.join(list(map(str, transpose(matrix_init)))))