class Document:
    """
    Программа выполняет функции сортировки бинарного дерева и превращения его в Двоичную куча, пирамиду, или сортиру́ющее дерево.
    Бинарное дерево — это иерархическая структура данных, в которой каждый узел имеет значение, значения не должны повторятся, (оно же является в данном случае и ключом) и
    ссылки на левого и правого потомка. Узел, находящийся на самом верхнем уровне (не являющийся чьим либо потомком) называется корнем. Узлы, не имеющие потомков
    (оба потомка которых равны NULL) называются листьями.
    Двоичная куча (binary heap) – просто реализуемая структура данных, позволяющая быстро (за логарифмическое время) добавлять элементы и извлекать элемент
    с максимальным приоритетом (например, максимальный по значению).
    Св-ва binary heap
        1. Значение в любой вершине не меньше, чем значения её потомков.
        2. Глубина всех листьев (расстояние до корня) отличается не более чем на 1 слой.
        3. Последний слой заполняется слева направо без «дырок».
    В программе изначально вызывается функция function_inicializathion_wood - функция инициализации дерева, которой передается кол-во элементов в слое, глубину дерева,
    массив в котором будет храниться полученное дерево, номер слоя. Полученное дерево не является отсортированным.
    Двоичную кучу удобно хранить в виде одномерного массива - N, причем левый потомок вершины с индексом i имеет индекс 2*i+1, а правый 2*i+2.
    Корень дерева – элемент с индексом 0. Высота двоичной кучи равна высоте дерева, то есть log2 N, где N – количество элементов массива.
    Из свойства процедуры Heapify нашей прирамиды потомки есть только  с [ N / 2 ]-го и кончая первым. Таким образом при инициализации пирамиды в функции function_inicializathion_wood
    необходимо указывать дерево у которого обязатьельно будет и левый, и правый сын, и кол-во листьев будет равно len(N)/2 округленнное до целого (Пр: 10 вершин в дереве, из них,
    5 листьев; 9 вершин из них 4 листа)
    Далее вызывается фенкция initializathipn_A которой передается наш неотсортированный массив, индекс по которому будем идти по неотсортированному массиву и непосредственно
    Одномерный массив который должен будет хранить наше дерево.
    Далее вызывается непосредственно функция Heapify которая должна будет превратить неупорядоченный массив в двочную кучу (Пирамиду), функция применяется к неупорядоченному
    массиву A начиная (согластно войствам процедуры Heapify) с len(A)/2 т.е с середины масссива A и до первого элемента с индексом 0
    (Для итерации можно использовать массив mas_wood т.к в данном представлении бинарного дерева, кол-во элементов len(mas_wood)-1) будет ровно числу элементов которые имеют
    потомков из массива A).
    Все остальные элементы которые стоят в неотсортированном масссива A превее являются лисьями и для них попытка применить Heapify приведет к ошибке
    т.к потомков они не имеют. На выходе получаем все тот же массив A, однако теперь отсортированый.
    Далее восстанавливаем из отсортированного массива дерево для более наглядной его демонстрации
    https://habr.com/post/65617/  -                  Структуры данных: бинарные деревья. Часть 1
    https://ru.wikipedia.org/wiki/Двоичная куча   -  Двоичная куча
    https://habr.com/post/112222/  -                 Структуры данных: двоичная куча (binary heap)

    """
#print(Document.__doc__)


def function_inicializathion_wood(tenn_wood, lengt_wood, wood, number_layer):   # кол-во элементов в слое, глубина дерева, массив, номер слоя
    tenni = 0
    print(tenn_wood, 'кол-лво элементов в слое')
    print('слой', number_layer)
    if number_layer == lengt_wood:                              # 1, 2, 3, 4 - при 4х слоях мы проходим от 1 до 2, от 2 до 3, от 3 до 4. В итоге получаем лишь 3 итерации
        return
    else:
        for i in range(tenn_wood):  # 1 2 4 8
            print()
            d = {}
            parrent, child1, child2 = input().split()                           #1) 16 11 9     2) 11 12 5    3) 9 10 8     4) 12 1 4     5) 5 7 -   6) 10 - -   7) 8 - -
            if child1 == "-" and child2 == "-":                                 # потомков нет
                tenni +=2
                continue
            elif child1 == "-":                                                 # нет левого потомка
                d[parrent] = [child2]
                wood.append(d)
                tenni += 1
                continue
            elif child2 == "-":                                                 # нет праого потомка
                d[parrent] = [child1]
                wood.append(d)
                tenni += 1
                continue
            else:
                d[parrent] = [child1, child2]
            wood.append(d)
        tenn_wood = (tenn_wood*2)-tenni
        number_layer+=1     # номер слоя
        function_inicializathion_wood(tenn_wood, lengt_wood, wood, number_layer)

tenn = 1                                                                        # кол-во элементов в слое (1,2,4,8)
water_lengt = int(input("Введите глубину дерева:", ))                           # глубина дерева
mas_wood = []                                                                   # [{'16': ['11', '9']}, {'11': ['12', '5']}, {'9': ['10', '8']}, {'12': ['1', '4']}, {'5': ['7']}]
number_layer_wood = 1                                                           # номер слоя
function_inicializathion_wood(tenn, water_lengt, mas_wood, number_layer_wood)   # функция инициализации массива mas_wood
print('Предстовление бинарного дерева', mas_wood)


def initializathipn_A(mass, l, S):
    if l == 0:
        for key, value in mass[l].items():
            S.append(key)
            for i in value:
                S.append(i)
    else:
        try:
            for value in mass[l].values():
                for r in range(len(value)):
                    S.append(value[r])
        except IndexError:
            return
    l += 1
    initializathipn_A(mass, l, S)

A = []
q = 0                                                                       # индекс по которому будем идти по mas_wood
initializathipn_A(mas_wood, q, A)                                           # Инициализация массива A, в нем вершинами графа будут только len(mas_wood) элементов
print("Массив А изначального дерева", A)


def Heapify(N, i, y):           # при условии в вызове функции сыновья (хотябы один) будет в любом случае, i - 4,3,2,1,0, N - массив A, y один из элементов из массива mas_wood
    b = 0
    for value in y.values():
        for u in value:
            b += 1

    if b == 1:
        try:
            left_son = N[2*i+1]                                             # возникает ошибка "left_son не существует"
        except IndexError:
            if int(N[i]) < int(N[2*i+2]):                                   # элемент родитель для right_son (right_son = N[2*i+2]) меньше чем сын
                N[i], N[2*i+2] = N[2*i+2], N[i]

        try:
            right_son = N[2*i+2]                                            # возникает ошибка "right_son не существует"
        except IndexError:
            if int(N[i]) < int(N[2*i+1]):                                   # элемент родитель для left_son (left_son = N[2*i+1]) меньше чем сын
                N[i], N[2*i+1] = N[2*i+1], N[i]                             #left_son = N[2*i+1]

    if b == 2:
        left_son = N[2*i+1]
        right_son = N[2*i+2]
        if int(N[i]) < int(left_son):
            N[i], N[2*i+1] = N[2*i+1], N[i]
        if int(N[i]) < int(right_son):
            N[i], N[2*i+2] = N[2*i+2], N[i]


print(int((len(A)-2)/2))
print(len(mas_wood)-1)

for t in range(int((len(A)-2)/2), -1, -1):            # Если t > N/2, где N ко-во элементов в массиве, то у элемента с таким индексом сыновей нет
    Heapify(A, t, mas_wood[t])                        # Для превращения неупорядоченного массива элементов в кучу, проходим начиная с элемента N/2 до 0
for t in range(0, int((len(A)-1)/2), +1):
    Heapify(A, t, mas_wood[t])
print("A после пробразования", A)

Restored_tree = {}

for i in range(len(mas_wood)):
    children=[]
    children.append(A[(2*i)+1])
    children.append(A[(2*i)+2])
    #print(children)
    Restored_tree[A[i]] = children

print('Восстановленное дерево', Restored_tree)













