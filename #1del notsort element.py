# Из некоторого массива необходимо удалить все неотсортированные элементы

mas_elementary = [6, 8, 2, 11, 4, 9, 20, 55]
result_mas = []
element_iterable, t = 0, len(mas_elementary)-1
while t > 0:
  try:
    if mas_elementary[element_iterable] < mas_elementary[element_iterable+1]: #68,811,1120,2055,
      if mas_elementary[element_iterable] not in result_mas:
          result_mas.append(mas_elementary[element_iterable])
      element_iterable+=1
    elif mas_elementary[element_iterable] > mas_elementary[element_iterable+1]: #82-2иск, 114-4иск,119-9иск
        if mas_elementary[element_iterable] not in result_mas:
          result_mas.append(mas_elementary[element_iterable])
        mas_elementary.pop(element_iterable+1)
        continue
    t-=1
  except IndexError:
    print("Достигнут последний элемент массива:")
    print("Массив mas_elementary преобразован в", mas_elementary)
    if mas_elementary[-1] > result_mas[-1]:
      result_mas.append(mas_elementary[-1])
      print("Результирующий массив", result_mas)
    break
