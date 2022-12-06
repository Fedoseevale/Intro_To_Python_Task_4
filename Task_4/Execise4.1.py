from random import randint as RI

def create_pattern(min: int, max: int) -> dict:
    degree = int(input('Введите максимальную степень многочлена: '))
    equation_pattern = {}
    for key in range(degree, -1, -1):
        value = RI(min, max)
        equation_pattern[key] = value
    return equation_pattern

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

my_new_pattern1 = create_pattern(-100, 100)
my_new_equation1 = decode_equation(my_new_pattern1)
print(my_new_equation1)

data = open('equation1.txt', 'w')
data.writelines(my_new_equation1)
data.close()

my_new_pattern2 = create_pattern(-100, 100)
my_new_equation2 = decode_equation(my_new_pattern2)
print(my_new_equation2)

data = open('equation2.txt', 'w')
data.writelines(my_new_equation2)
data.close()