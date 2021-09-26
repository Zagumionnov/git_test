from random import randint

m = int(input("Введите размер матрицы: "))
lst1 = [[randint(1, 50) for j in range(m)] for i in range(m)]


def sort_lst(matrix):

    # Суммируем столбцы создаем список

    total = [0 for i in range(m)]
    for y in range(len(lst1)):
        total = [total[index] + i for index, i in enumerate(lst1[y])]

    # Сортируем столбцы по возрастанию сумм

    for i in range(len(total)-1):
        for j in range(len(total) - i - 1):
            if total[j] > total[j + 1]:
                total[j], total[j + 1] = total[j + 1], total[j]
                for y in range(len(lst1)):
                    matrix[y][j], matrix[y][j + 1] = matrix[y][j + 1], matrix[y][j]

    # Сортируем столбцы по четн. и нечетн. кол.

    for x in range(len(lst1)):
        for i in range(len(lst1) - 1):
            for j in range(len(lst1) - i - 1):
                if x % 2 != 0:
                    if matrix[j][x] > matrix[j + 1][x]:
                        matrix[j][x], matrix[j + 1][x] = matrix[j + 1][x], matrix[j][x]
                else:
                    if matrix[j][x] < matrix[j + 1][x]:
                        matrix[j][x], matrix[j + 1][x] = matrix[j + 1][x], matrix[j][x]

    return matrix


def lprint(matrix1):

    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            print('{:<3}'.format(lst1[i][j]), end='  ')
        print()

    total = [0 for i in range(m)]
    for y in range(len(lst1)):
        total = [total[index] + i for index, i in enumerate(lst1[y])]

    for i in range(len(total)):
        print('{:<3}'.format(total[i]), end='  ')
    print()


lprint(lst1)
z = sort_lst(lst1)
print()
lprint(lst1)
print('sdfd')
print('sdfd')
print('sdfd')
print('sdfd')
print('sdfd')
print('sdfd')
print('sdfd')
print('sdfd')
print('sdfd')