#!/usr/bin/env python3
import sys
import re

operations_list = ['+', '-', '*', '/']


def calculate(a: str, b: str, operation: str):
    """
    Рассчитывает результат применения операции operation к аргументам a и b 
    """
    a, b = int(a), int(b)
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
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
    print_result(a, b, method)


def print_result(**kwargs):
    """
    Выводит результат операции
    """
    result, error = calculate(**kwargs)
    if error:
        print(error)
        exit(1)
    else:
        print(result)
        exit()


if __name__ == '__main__':
    filename = sys.argv[0]
    target_pattern = re.compile(
        r'^(?P<a>\d*)(?P<operation>[\*\+\-\/]?)(?P<b>\d*)$')
    first_message = 'Simple calc 0.0'
    help_message = f'See "{filename} --help".'

    for ind in range(1, len(sys.argv)):
        arg = sys.argv[ind]
        arg_target = re.match(target_pattern, arg)
        if arg_target and all(arg_target.groups()):
            print_result(**arg_target.groupdict())
        else:
            if arg == '-h' or arg == '--help':
                print(first_message)
                print(f'Usage: python3 {filename} [options] [target] ...\n')
                print('Options:\n')
                print('\t-h, --help\tPrint this message and exit.')
                print('\t-v, --version\tPrint the version number of make and exit.')
                exit()
            elif arg == '-v' or arg == '--version':
                print(first_message)
                print(help_message)
            else:
                print('Unknown flag:', arg)
                print(help_message)
                exit(1)
    # main()
