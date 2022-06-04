# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1.
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# Вторая — которая отфильтрует этот список

from functools import reduce
from os import remove


namesProgrammingLanguages = ['Basic', 'Cg', 'JOVIAL', 'Pascal', 'QBASIC', 'PL/M', 'REXX', 'C++', 'C#', 'ColdFusion', 'Dart', 'Object Pascal',
                             'Dylan', 'Eiffel', 'Java', 'JavaScript', 'PHP', 'Pike', 'Python', 'Ruby', 'Self', 'Simula', 'Smalltalk', 'Swift',
                             'Vala', 'Visual Basic']

serialNumbers = [i for i in range(1, len(namesProgrammingLanguages))]

def tuplesFunctionOne(listOne, listTwo):
    tuplesLanguagesList = list(
        map(lambda x: (listOne[x], listTwo[x].upper()), range(0, len(listOne))))
    return tuplesLanguagesList

def counterFunctionTwo(listTuples: list):
    newList = []
    for i in range(len(listTuples)):
        count = 0
        for k in listTuples[i][1]:
            count += ord(k)
        if count % listTuples[i][0] == 0:
            buf = list(listTuples[i])
            buf[0] = count
            listTuples[i] = tuple(buf)
            newList.append(listTuples[i])
    print(f'Новый список: {newList}')
    sum = reduce(lambda s, y: s + y[0] , newList, 0)
    return sum


tuplesList = tuplesFunctionOne(serialNumbers, namesProgrammingLanguages)
print(f'Исходный список: {tuplesList}\n')
sumPoint = counterFunctionTwo(tuplesList)
print(f'Сумма оставшихся чисел: {sumPoint}')
