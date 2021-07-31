# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''Мое решение'''
list1 = []
list2 = []
for i in list1:
    if i>0:
        list2.append(i)
list1.sort()
for k in list1:
    if k == 0:
        list2.append(k)
print(list2)


arr = [1, 0, 1, 2, 0, 1, 3]
l = [i for i in arr if isinstance(i, bool) or i!=0]
print(l+[0]*(len(arr)-len(l)))
'''
l = [i for i in arr if isinstance(i, bool) or i!=0] -> Создает список сверху без нулей

>>>
l+[0]*(len(arr)-len(l)) -> это действие добавляет в конец списка l нули ( [0] ),
количество которых зависит от разницы длины старого и нового списка
>>>

'''


