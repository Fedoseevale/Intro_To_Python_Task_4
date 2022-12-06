

data_from_file1 = open("equation1.txt", "r")
my_new_equation1 = data_from_file1.readline()
data_from_file1.close()

print(f'Имеется запись многочлена из первого файла: \n{my_new_equation1}')

data_from_file2 = open("equation2.txt", "r")
my_new_equation2 = data_from_file2.readline()
data_from_file2.close()

print(f'Имеется запись многочлена из второго файла: \n{my_new_equation2}')

def encode_equation(equation: str) -> dict:
    new_equation = []
    equation = equation.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    for item in equation:
        if not 'x' in item:
            new_equation.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    new_equation.append(['1', '1'])
                elif item == '-x':
                    new_equation.append(['-1', '1'])
                else:
                    new_equation.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    new_equation.append(('1' + item).split('x**'))
                elif item.startswith('-x'):
                    new_equation.append(item.replace('-', '-1').split('x**'))
                else:
                    new_equation.append(item.split('*x**'))
    equation_pattern = {}
    for item in new_equation:
        equation_pattern[int(item[1])] = int(item[0])
    return equation_pattern


my_new_equation1_dict = encode_equation(my_new_equation1)
my_new_equation2_dict = encode_equation(my_new_equation2)


def equation_addition(first: dict, second: dict) -> dict:
    base = {}
    base.update(first)
    base.update(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])


result_equation_dict = equation_addition(my_new_equation1_dict, my_new_equation2_dict)


def decode_equation(equation: dict) -> str:
    new_equation = ''
    first = True
    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'-{value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value} '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1 '
                    else:
                        new_equation += f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        new_equation += f'- {abs(value)}*x '
                    elif key == 0:
                        new_equation += f'- {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '
    return new_equation + '= 0'

result_equation = decode_equation(result_equation_dict)

print(f'Сумма многочленов из двух файлов:\n{result_equation}')


data = open('equation3.txt', 'w')
data.writelines(result_equation)
data.close()