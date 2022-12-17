# Создайте программу для игры в ""Крестики-нолики"".
import random

# Tkinter

print('Имеется поле для игры в крестики-нолики. Нумерация ячеек ведётся слева направо, продолжается '
      'с переходом на новую строку.')
field = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']

def print_field(field):
    print(f' | {field[0]} | {field[1]} | {field[2]} |')
    print(' _____________')
    print(f' | {field[3]} | {field[4]} | {field[5]} |')
    print(' _____________')
    print(f' | {field[6]} | {field[7]} | {field[8]} |')

my_field = print_field(field)

# игрок A - человек
# игрок B - компьютер
print('Бросаем жребий')
step1 = random.randint(0, 1) # 0 - первым ходит человек, 1 - первым ходит компьютер
# print(step1)
if step1 == 0:
    print('Вы начинаете игру')
    print('Введите номер ячейки, в которую собираетесь поставить крестик: ')
    human_step = int(input())
    field[human_step - 1] = 'X'
    my_field = print_field(field)
    print('Следующий шаг делает компьютер: ')
    comp_step = random.randint(0, 8)
    if field[comp_step] != 'N':
        while field[comp_step] != 'N':
            comp_step = random.randint(0, 8)
    field[comp_step] = '0'
    my_field = print_field(field)

    while ((field[0] != field[1] and field[1] != field[2]) or (field[3] != field[4] and field[4] != field[5]) or
           (field[6] != field[7] and field[7] != field[8]) or (field[0] != field[4] and field[4] != field[8]) or
           (field[2] != field[4] and field[4] != field[6]) or (field[0] != field[3] and field[3] != field[6]) or
           (field[1] != field[4] and field[4] != field[7]) or (field[2] != field[5] and field[5] != field[8])):
        print('Введите номер ячейки, в которую собираетесь поставить крестик: ')
        human_step = int(input())
        if field[human_step - 1] == '0':
            while field[human_step - 1] == '0' or field[human_step - 1] == 'X':
                print('Вы не можете использовать данную ячейку, т.к. она занята')
                print('Введите номер ячейки, в которую собираетесь поставить крестик: ')
                human_step = int(input())

        field[human_step - 1] = 'X'
        my_field = print_field(field)
        if (field[0] == field[1] == field[2] == 'X'):
            print('Вы выиграли!')
            break
        elif (field[3] == field[4] == field[5] == 'X'):
            print('Вы выиграли!')
            break
        elif (field[6] == field[7] == field[8] == 'X'):
            print('Вы выиграли!')
            break
        elif (field[0] == field[4] == field[8] == 'X'):
            print('Вы выиграли!')
            break
        elif (field[2] == field[4] == field[6] == 'X'):
            print('Вы выиграли!')
            break
        elif (field[0] == field[3] == field[6] == 'X'):
            print('Вы выиграли!')
            break
        elif (field[1] == field[4] == field[7]) == 'X':
            print('Вы выиграли!')
            break
        elif (field[2] == field[5] == field[8]) == 'X':
            print('Вы выиграли!')
            break
        else:
            print('Следующий шаг делает компьютер: ')
            comp_step = random.randint(0, 8)
            if field[comp_step] != 'N':
                while field[comp_step] != 'N':
                    comp_step = random.randint(0, 8)
            field[comp_step] = '0'
            my_field = print_field(field)
            if (field[0] == field[1] == field[2] == '0'):
                print('Выиграл компьютер!')
                break
            if (field[3] == field[4] == field[5] == '0'):
                print('Выиграл компьютер!')
                break
            elif (field[6] == field[7] == field[8] == '0'):
                print('Выиграл компьютер!')
                break
            elif (field[0] == field[4] == field[8] == '0'):
                print('Выиграл компьютер!')
                break
            elif (field[2] == field[4] == field[6] == '0'):
                print('Выиграл компьютер!')
                break
            elif (field[0] == field[3] == field[6] == '0'):
                print('Выиграл компьютер!')
                break
            elif (field[1] == field[4] == field[7] == '0'):
                print('Выиграл компьютер!')
                break
            elif (field[2] == field[5] == field[8] == '0'):
                print('Выиграл компьютер!')
                break

if step1 == 1:
    print('Игру начинает компьютер')
    comp_step = random.randint(0, 8)
    if field[comp_step] != 'N':
        while field[comp_step] != 'N':
            comp_step = random.randint(0, 8)
    field[comp_step] = '0'
    my_field = print_field(field)
    print('Введите номер ячейки, в которую поставить крестик: ')
    human_step = int(input())
    if field[human_step - 1] == '0':
        while field[human_step - 1] == '0' or field[human_step - 1] == 'X':
            print('Вы не можете использовать данную ячейку, т.к. она занята')
            print('Введите номер ячейки, в которую поставить крестик: ')
            human_step = int(input())
    field[human_step - 1] = 'X'
    my_field = print_field(field)
    while ((field[0] != field[1] and field[1] != field[2]) or (field[3] != field[4] and field[4] != field[5]) or
           (field[6] != field[7] and field[7] != field[8]) or (field[0] != field[4] and field[4] != field[8]) or
           (field[2] != field[4] and field[4] != field[6]) or (field[0] != field[3] and field[3] != field[6]) or
           (field[1] != field[4] and field[4] != field[7]) or (field[2] != field[5] and field[5] != field[8])):
        print('Следующий шаг делает компьютер: ')
        comp_step = random.randint(0, 8)
        if field[comp_step] != 'N':
            while field[comp_step] != 'N':
                comp_step = random.randint(0, 8)
        field[comp_step] = '0'
        my_field = print_field(field)
        if (field[0] == field[1] == field[2] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[3] == field[4] == field[5] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[6] == field[7] == field[8] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[0] == field[4] == field[8] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[2] == field[4] == field[6] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[0] == field[3] == field[6] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[1] == field[4] == field[7] == '0'):
            print('Выиграл компьютер!')
            break
        elif (field[2] == field[5] == field[8] == '0'):
            print('Выиграл компьютер!')
            break
        else:
            print('Введите номер ячейки, где собираетесь поставить крестик: ')
            human_step = int(input())
            if field[human_step - 1] == '0':
                while field[human_step - 1] == '0' or field[human_step - 1] == 'X':
                    print('Вы не можете использовать данную ячейку, т.к. она занята')
                    print('Введите номер ячейки, где собираетесь поставить крестик: ')
                    human_step = int(input())

            field[human_step - 1] = 'X'
            my_field = print_field(field)
            if (field[0] == field[1] == field[2] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[3] == field[4] == field[5] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[6] == field[7] == field[8] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[0] == field[4] == field[8] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[2] == field[4] == field[6] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[0] == field[3] == field[6] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[1] == field[4] == field[7] == 'X'):
                print('Вы выиграли!')
                break
            elif (field[2] == field[5] == field[8] == 'X'):
                print('Вы выиграли!')
                break
if ((field[0] != field[1] and field[1] != field[2]) and (field[3] != field[4] and field[4] != field[5]) and
           (field[6] != field[7] and field[7] != field[8]) and (field[0] != field[4] and field[4] != field[8]) and
           (field[2] != field[4] and field[4] != field[6]) and (field[0] != field[3] and field[3] != field[6]) and
           (field[1] != field[4] and field[4] != field[7]) and (field[2] != field[5] and field[5] != field[8])):
    print('Результат игры - ничья')
