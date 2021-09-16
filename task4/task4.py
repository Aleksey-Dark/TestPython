from collections.abc import Iterator


def main():
    string1 = input('Введите первую строку: ')
    string2 = input('Введите вторую строку: ')
    if len(string1) > 0 and len(string2) > 0:
        if comparison(string1, string2):
            print('OK')
        else:
            print('KO')
    else:
        print('usage')


def comparison(str_1: str, str_2: str) -> bool:
    """
    Функция сравнения строк.

    :param str_1: Первая строка
    :type str_1: str

    :param str_2: Вторая строка
    :type str_2: str

    :return: Признак соответствия строк
    :rtype: bool
    """
    print(f'{str_1} {str_2}', end=' - ')
    if not str_1 == str_2:
        sep_lst = str_2.split('*')
        if set(str_2) - set(str_1) != set('*'):
            return False
        if not cut(str_1, (i for i in sep_lst)):
            return False
    return True


def cut(string: str, lst: Iterator, i: int = 0, mask: bool = False) -> bool:
    """
    Функция проверки наличия фрагмента второй строки в первой строке.

    :param string: Первая строка
    :type string: str

    :param lst: Итератор с элементами второй строки
    :type lst: list

    :param i: Счетчик глубины рекурсии
    :type i: int

    :param mask: Флаг наличия звездочки в предыдущем символе
    :type mask: bool

    :return:
    """
    try:
        elem = next(lst)
    except StopIteration:

        if string == '' or mask:
            return True
        return False
    else:
        if elem == '':
            return cut(string, lst, i+1, True)

        left, _, string = string.partition(elem)
        if i == 0 and left != '':
            return False
        if string != '':
            return cut(string, lst, i+1, False)
        return True


main()
