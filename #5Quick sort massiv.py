#import random
'''
Один из самых быстрых известных универсальных алгоритмов сортировки массивов:
Является  улучшенным вариантом алгоритма сортировки с помощью прямого обмена («Пузырьковая сортировка» и «Шейкерная сортировка»),
известного, в том числе, своей низкой эффективностью. Принципиальное отличие состоит в том, что в первую очередь производятся
перестановки на наибольшем возможном расстоянии и после каждого прохода элементы делятся на две независимые группы.
Любопытный факт: улучшение самого неэффективного прямого метода сортировки дало в результате один из наиболее эффективных
улучшенных методов.
Общая идея алгоритма состоит в следующем:
1) Выбрать из массива элемент, называемый опорным. Это может быть любой из элементов массива. От выбора опорного элемента не зависит корректность алгоритма, но в отдельных случаях может сильно зависеть его эффективность (см.ниже).
2) Сравнить все остальные элементы с опорным и переставить их в массиве так, чтобы разбить массив на три непрерывных отрезка, следующие друг за другом: «меньшие опорного», «равные» и «большие»[1].
Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина отрезка больше единицы.
На практике массив обычно делят не на три, а на две части: например, «меньшие опорного» и «равные и большие»; такой подход в общем случае эффективнее, так как упрощает алгоритм разделения
'''

with open('#5Quick sort.txt', 'r') as ar:
    for mas in ar:
        mas = mas.strip().split(',')   # Режем файл по символу ","
nums = [int(t) for t in mas]           # переводим str -> int и в массив
print('Исходный массив nums из файла #5Quick sort.txt:', nums)      # [4, 1, 6, 3, 2, 7, 8]

def quicksort(nums):                   # Функция быстрой сортировки
    if len(nums) <= 1:
        return nums
    else:
        #q = random.choice(nums)
        #print('q', q)
        q = nums[len(nums)//2]          # q - опорный элемент, делит массив пополам
        s_nums = []                     # меньше опорного
        m_nums = []                     # больше опорного
        e_nums = []                     # равны
        for n in nums:
            #print(n)
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        #print('s_nums', s_nums)
        #print('m_nums', m_nums)
        #print('e_nums', e_nums)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)

print('Отсортированный массив', quicksort(nums))