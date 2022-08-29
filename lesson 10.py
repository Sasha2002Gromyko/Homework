# f = open('example.txt','r') #Открытие файла
# print(*f) #Выводит содержимое файла
# print(f) #Выводит объект
# f.close()#После работы с файлом его надо закрыть
# #2-ой способ закрытия файла
# f = open('example.txt','r')
# try:
#     print(*f)
# finally:
#     f.close()#Альтернативный метод закрытия файла
# #3-ий способ закрытия файла
# with open('example.txt') as  f:
#     print(*f)
# #Чтение и запись файлов
# f = open('example.txt','r')
#
# print(f.read(7))#Чтение 7 символов из текстового докумен
# print(f.read(7))#При использовании той же команды, он продолжает чтение файла, а не начинает

# x = open('test.txt', 'r')
#
# print(x.readline(),'\n',x.readline())#Читает одну строку
# print(x.readlines())#Выводит все строки списком

# f = open('xyz.txt', 'w')
# f.write('Hello \nWorld')
# f.close()
# #Переименование файлов
# import os
# os.rename('abc,txt', 'abc.txt')

# #Вывод текущей директории
# import os
# print('Текущая директория:', os.getcwd())
# #Создание папок
# import os
# print('Текущая директория:', os.getcwd())
# os.mkdir('folder1')#создать пустой каталог(папку)
# #Изменение директории

# import os
# os.chdir('folder1')
# print('Текущая директория изменилась на folder1:', os.getcwd())
# #Создание вложенных папок
# import os
# os.chdir('folder1') #Изменение текущего каталога на "folder1"
# os.chdir('..') #Вернуться в предыдущую директорию
# os.makedirs()


