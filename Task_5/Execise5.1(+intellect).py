# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота "интеллектом"
import random

totalNumberOfSweets = int(input('Введите количество конфет, лежащих на столе: '))


# игрок A - человек
# игрок B - компьютер
step1 = random.randint(0, 1) # 0 - первым ходит человек, 1 - первым ходит компьютер
# print(step1)
if step1 == 0:
    print('Вы начинаете игру')
    print('Введите количество конфет, которое собираетесь взять на данном шаге: ')
    numberOfSweetsHuman = int(input())
    # print(numberOfSweetsHuman)
    if numberOfSweetsHuman != totalNumberOfSweets % 29:
        numberOfSweetsComp = totalNumberOfSweets % 29
        print(f'Количество конфет, которое берет компьютер: {numberOfSweetsComp}')
    else:
        numberOfSweetsComp = random.randint(1, 28)
        print(f'Количество конфет, которое берет компьютер: {numberOfSweetsComp}')
    sum = numberOfSweetsHuman + numberOfSweetsComp
    sumStep = 0
    sumStep = sumStep + sum
    # print(f'Количество конфет, которое всего взяли участники игры: {sumStep}')
    cond = totalNumberOfSweets - sumStep
    # print(f'Количество конфет, которое осталось взять: {cond}')
    # diffNumberOfSweets = 29 - numberOfSweetsComp
    # print(f'Количество конфет, которое нужно взять для сохранения выигрышной стратегии: '
    #       f'{diffNumberOfSweets}')
    while cond > 0:
        print('Введите количество конфет, которое собираетесь взять на данном шаге: ')
        numberOfSweetsHuman = int(input())
        # print(numberOfSweetsHuman)
        sumStep = sumStep + numberOfSweetsHuman
        specialSum1 = sumStep
        # print(f'Количество конфет, которое всего взяли участники игры: {sumStep}')
        cond = totalNumberOfSweets - sumStep
        # print(f'Количество конфет, которое осталось взять: {cond}')
        # diffNumberOfSweets = 29 - numberOfSweetsComp
        # print(f'Количество конфет, которое нужно взять для сохранения выигрышной стратегии: '
        #       f'{diffNumberOfSweets}')

        if cond > 0:
            numberOfSweetsComp = 29 - numberOfSweetsHuman
            print(f'Количество конфет, которое берет компьютер: {numberOfSweetsComp}')
            sumStep = sumStep + numberOfSweetsComp
            specialSum2 = sumStep
            # print(f'Количество конфет, которое всего взяли участники игры: {sumStep}')
            cond = totalNumberOfSweets - sumStep
            # print(f'Количество конфет, которое осталось взять: {cond}')
            # diffNumberOfSweets = 29 - numberOfSweetsComp
            # print(f'Количество конфет, которое нужно взять для сохранения выигрышной стратегии: '
            #       f'{diffNumberOfSweets}')

    if specialSum2 > specialSum1:
        print('Победу одерживает компьютер')
    else:
        print('Поздравляем, Вы выиграли!')

else:
    print('Игру начинает компьютер')
    numberOfSweetsComp = totalNumberOfSweets % 29
    print(f'Количество конфет, которое взял компьютер: {numberOfSweetsComp}')
    print('Введите количество конфет, которое собираетесь взять на данном шаге: ')
    numberOfSweetsHuman = int(input())
    sum = numberOfSweetsHuman + numberOfSweetsComp
    sumStep = 0
    sumStep = sumStep + sum
    # print(f'Количество конфет, которое всего взяли участники игры: {sumStep}')
    cond = totalNumberOfSweets - sumStep
    # print(f'Количество конфет, которое осталось взять: {cond}')
    # diffNumberOfSweets = 29 - numberOfSweetsHuman
    # print(f'Количество конфет, которое нужно взять для сохранения выигрышной стратегии: '
    #       f'{diffNumberOfSweets}')

    while cond > 0:
        numberOfSweetsComp = 29 - numberOfSweetsHuman
        print(f'Количество конфет, которое берет компьютер: {numberOfSweetsComp}')
        sumStep = sumStep + numberOfSweetsComp
        specialSum1 = sumStep
        # print(f'Количество конфет, которое всего взяли участники игры: {sumStep}')
        cond = totalNumberOfSweets - sumStep
        # print(f'Количество конфет, которое осталось взять: {cond}')
        # diffNumberOfSweets = 29 - numberOfSweetsComp
        # print(f'Количество конфет, которое нужно взять для сохранения выигрышной стратегии: '
        #       f'{diffNumberOfSweets}')

        if cond > 0:
            print('Введите количество конфет, которое собираетесь взять на данном шаге: ')
            numberOfSweetsHuman = int(input())
            # print(numberOfSweetsHuman)
            sumStep = sumStep + numberOfSweetsHuman
            specialSum2 = sumStep
            # print(f'Количество конфет, которое всего взяли участники игры: {sumStep}')
            cond = totalNumberOfSweets - sumStep
            # print(f'Количество конфет, которое осталось взять: {cond}')
            diffNumberOfSweets = 29 - numberOfSweetsComp
            # print(f'Количество конфет, которое нужно взять для сохранения выигрышной стратегии: '
            #       f'{diffNumberOfSweets}')

    if specialSum2 > specialSum1:
        print('Поздравляем, Вы выиграли!')
    else:
        print('Победу одерживает компьютер')