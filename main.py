#!/usr/bin/env python3

methods_list = ['сложение', 'вычитание', 'умножение', 'деление']


def calculate(a, b, method):
    if method == 'сложение':
        result = a + b
    elif method == 'вычитание':
        result = a - b
    elif method == 'умножение':
        result = a * b
    elif method == 'деление':
        if b == 0:
            return None, 'Попытка делить на ноль'
        result = int(a / b)
    else:
        return None, 'Неизвестный метод'
    return result, None


def main():
    a = int(input('Введите первое число:'))
    print()
    b = int(input('Введите второе число:'))
    print()
    print('Доступные методы:')
    for i, item in enumerate(methods_list):
        print(f'[{i}] {item}')
    method_num = input('Введите число [0]:')
    if not method_num:
        method_num = 0
    method = methods_list[int(method_num)]
    result, error = calculate(a, b, method)
    if error:
        print('Ошибка:', error)
        exit(1)
    else:
        print('Результат:', result)

if __name__ == '__main__':
    main()
