# Дана разреженная матрица CSS. Найти сумму её элементов.
'''
По заданию в файле #2- sparse matrix.txt лежит разряженная матрица.
Разрежённая матрица — это матрица с преимущественно нулевыми элементами. В противном случае, если большая часть элементов матрицы ненулевые,
матрица считается плотной. Необходимо найти Сумму некоторых элементов матрицы. Всю матрицу необходимо хранить в виде 4 массивов.
Мaссив A -  Массив ненулевых элементов матрицы,
LJ - Номера столбцов у этих элементов,
N - массив от 1 до максимального кол-ва ненулевых элементов,
LI - местоположение первого ненулевого элемента
доступ к элементу матрицы необходимо осуществлять с использованием этих массивов, после инициализации всех 4 массивов. Необходимо ввеслти
кол-во элементов которые хотим просумировать, далее вводим индексы элементов которые хотим просумировать, передаем их в функцию item_search
и выводим этот элемент, после чего просумируем его с summa_elemwntov_discharged_matrix, тоже самое проделываем с другим элеметом и выводим конечную
сумму элементов (summa_elemwntov_discharged_matrix)
'''

with open("#2- sparse matrix.txt", 'r') as inf:
    my_love_massiv = []
    for line in inf:
        line = line.rstrip().split(' ')
        my_love_massiv.append(line)                         # Массив строк матрицы
    #print('my_love_massiv', my_love_massiv)
    A = []                                                  # A ['2', '1', '5', '1', '9', '1', '8', '4', '3']  - Массив ненулевых элементов матрицы.
    LJ = []                                                 # LJ [2, 4, 2, 6, 5, 6, 2, 4, 6] - Номера столбцов у этих элементов.
    N = []                                                  # N [1, 2, 3, 4, 5, 6, 7, 8, 9] - массив от 1 до максимального кол-ва ненулевых элементов
    kol_vo_not_zero_element_in_str_matrix = []              # [2, 0, 2, 2, 0, 3] - ко-лво ненулевых элементов в каждой строке матрицы
    v = 1
    for element in my_love_massiv:
        number_of_nonzero_elements_in_a_string = 0          # кол-во ненулевых элементов в строчке
        for t in range(len(element)):
            if int(element[t]) != 0:
                A.append(element[t])
                LJ.append(t+1)                              # мы считаем массив начиная с 0 (а не 1 как было а парах), поэтому считай каждый элемент +1
                number_of_nonzero_elements_in_a_string+=1
                N.append(v)
                v+=1
        kol_vo_not_zero_element_in_str_matrix.append(number_of_nonzero_elements_in_a_string)
    #print('kol_vo_not_zero_element_in_str_matrix', kol_vo_not_zero_element_in_str_matrix) # [2, 0, 2, 2, 0, 3]
    rev_N = N[::-1]                                         # перевернутый массив N. rev_N = list(reversed(N)) # reversed переврачивает список не изменяя его, возвращает итератор
    print("rev_N", rev_N)
    LI = []                                                 #местоположение первого ненулевого элемента
    CEL = []
    for i in kol_vo_not_zero_element_in_str_matrix:
        if i == 0:
            LI.append(i)
        else:
            for t in range(i):                              # 01 01 01 012
                CEL.append(rev_N.pop())
            LI.append(CEL[0])
            CEL.clear()
    for P in range(len(LI)):
        if LI[P] == 0:
            LI[P] = LI[P+1]
    LI.append(len(N)+1)
    print("N", N)
    print("A", A)
    print("LJ", LJ)
    print("LI", LI)
    summa_elemwntov_discharged_matrix = 0

    def item_search(n, k):
        N1 = LI[n-1]
        N2 = LI[n]
        AA = 0
        for t in range(N1, N2):  # 5 6
            if LJ[t-1] == k:
                AA = A[t-1]
                break
        return AA
    try:
        for k in range(int(input("Введите кол-во суммируемых элементов:"))):
            i, j = map(int, input("Введите поочередно индексы элементов:").split())
            print(item_search(i, j))
            summa_elemwntov_discharged_matrix += int(item_search(i, j))
        print("Сумма элементов = ", summa_elemwntov_discharged_matrix)
    except IndexError:
        print("Упс, введенные индексы выходят за пределы матрицы, искомых элементов не обнаруженно, попробуйте снова")






































    

