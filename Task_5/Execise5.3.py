# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import random

# print('Введите данные, которые хотите сжать: ')
# myData = input()
# print(data)

def codingRLE(data):
    coding = ''
    prevSymbol = ''
    count = 1
    for item in data:
        if item != prevSymbol:
            if prevSymbol:
                # print(prevSymbol)
                coding += str(count) + prevSymbol
            count = 1
            prevSymbol = item
        else:
            count += 1
    else:
       coding += str(count) + prevSymbol
    return coding

path = 'D:\Science\GB\Home_tasks\Python\Task_5\Input_data.txt'
dataFromFile = open(path, "r")
myData = dataFromFile.readline()
dataFromFile.close()

print(f'Имеются данные, подлежащие сжатию: \n{myData}')

myCodedData = codingRLE(myData)
print(f'В сжатом виде данные выглядят следующим образом: \n{myCodedData}')

path2 = 'D:\Science\GB\Home_tasks\Python\Task_5\Output_data.txt'
dat = open(path2, 'w')
dat.writelines(myCodedData)
dat.close()

def deCodingRLE(data):
    decoding = ''
    count = ''
    for item in data:
        if item.isdigit():
            count += item
        else:
            decoding += item * int(count)
            count = ''
    return decoding

dataFromFile2 = open(path2, "r")
myData2 = dataFromFile2.readline()
dataFromFile2.close()

print('Извлекаем из файла данные, подлежащие "разжатию"')

myDeCodedData = deCodingRLE(myData2)
print(f'В "разжатом" виде данные выглядят следующим образом: \n{myDeCodedData}')