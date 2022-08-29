# #Множества. Мы можем создавать множества.Set- множество
# a = {1,2,3,4,5}
# print(a)

# #Так же можно создать множества строк. Так же множества не имеют индекса, и поэтому они выводятся в произвольном порядке.
# a = {'Яблоко','Банан','Груша',(1,2,3),2.0}
# print(a)

# #Создание множеств.Можно создать множество из списков при помощи функции set
# num_set = set([1,2,3,4,5,6])
# print(num_set)

# #Множества не содержат дубликатов, если слово или цифра повторяется, то при выводе он уберёт дубликат
# a = set([1,2,3,2,1])
# print(a)
# b={1,2,3,2,1}
# print(b)

# #При создании пустого множества, скорее всего создадиться пустой словарь
# x = {}
# print(type(x))
# x = set()
# print(type(x))

#Пример.
# x = set(['Mar','feb','Jun'])
# for m in x:
#     print(m)

# #Можно проверить на начилие элемента
# x = set(['Mar','feb','Jun'])
# print('feb' in x)

# #Можно добавить элемент
# x = set(['Mar','feb','Jun'])
# x.add('Jul')#Добавление элемента
# print(x)

# #Удаление элемента из множества
# num_set = {1,2,3,4,5,6}
# num_set.discard(3)#Удаление элемента.Не выдает ошибку, если нет изначально элемента
# print(num_set)
# num_set = {1,2,3,4,5,6}
# num_set.remove(7)# как discard, но если нет изначально элемента, то он выдаст ошибку
# print(num_set)

# #С методом pop(), мы можем удалить и вернуть элемент.
# num_set = {1,2,3,4,5,6}
# print(num_set.pop())
# print(num_set)

# #Удаляет все элементы
# num_set={1,2,3,4,5,6}
# num_set.clear()
# print(num_set)

# #Объединение множеств
# x = {1,2,3,4,5}
# y = {6,7,8,9,10}
# z = x.union(y)
# print(z)
# x = {1,2,3,4,5}
# y = {6,7,8,9,10}
# print(x | y)

# #Пересечение множеств.Выводит повторяющийся элемент
# x = {1,2,3}
# y = {4,3,6}
# print('Результат: ',x & y)#Операция пересечения во множествах может быть достигнута как при помощи оператора &, так и метода intersection().

# #Предположим, у вас есть два множества: А и В.
# # Разница между А и В (А — В) — это множество со всеми элементами, которые содержатся в А, но не в В.
# # Соответственно, (В — А) — это множество со всеми элементами в В, но не в А.
# A = {1,2,3}
# B = {4,3,6}
#
# print(A - B)
# print(B - A)

# #Метод copy()
# #Этот метод возвращает копию множества.
# string_set = {'Nikolas', 'Michaelle', 'John', 'Mercy'}
# x = string_set.copy()
# print(x)

# #Метод isdisjoint()
# #Этот метод проверяет, является ли множество пересечением или нет.
# x = {1,2,3}
# y = {4,5,6}
# z = x.isdisjoint(y)
# print(z)

# #Единственное отличие set от frozenset заключается в том, что set - изменяемый тип данных, а frozenset - нет.
# x = frozenset([1,2,3,-10,40])
# print(type(x))

# #Задание 1. Проверить есть ли в последовательности чисел списка дубликат
# x = {1,2,3,4,5,6,}
# y = {7,8,2,9,10}
# z = x.isdisjoint(y)
# print(z,'\n',x | y)

# #Задание 2
# x = {1,2,3,4}
# y = frozenset([5,6,7,8,2])
# print('Объединение множеств: ',x | y,'\n','пересечение множеств:',x & y)

# #Исключение.Исключения необходимы для того, чтобы сообщать программисту об ошибках.
# a = 100/0

# #Конструкция try - except
# try:#блок кода в котором мы хотим поимать ошибку
#     k = 1/0
# except ZeroDivisionError:#указываем что за ошибка
#     k=0
# print(k)

# #В блоке try мы выполняем инструкцию, которая может породить исключение, а в блоке except мы перехватываем их.
# # При этом перехватываются как само исключение, так и его потомки.
# try:
#     k = 1/0
# except ArithmeticError:
#     k = 0
# print(k)

# #По той же теме
# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = my_dict['d']
# except IndexError:
#     print('Такого индекса не существует')
# except KeyError:
#     print('Этого ключа нет в словаре')
# except:
#     print('Произошла другая ошибка')

# #Оператор finnaly.Finally выполняет блок инструкций в любом случае, было ли исключение,
# # или нет (применима, когда нужно непременно что-то сделать, к примеру, закрыть файл).
# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError')
# finally:
#     print('Оператор finnaly выполнен')

# #1-ое задание
# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# try:
#     c = a/b
# except ZeroDivisionError:
#     print('Ошибка деления на ноль')
# else:
#     print('Ошибки нет',c**2)
# finally:
#     print('Оператор finnaly выполнен')
#
# #2-ое задание

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)
