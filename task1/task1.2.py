def main():
    request = input('Введите число, исходную и конечную системы счисления (Пример: 100101 01 0123456789):\n')
    request = request.split()
    try:
        num, num_base, base = request
        if len(base) < 2 or len(num_base) < 2 or not set(num) <= set(num_base):
            raise ValueError
    except ValueError:
        print('usage')
    else:
        if not "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".startswith(num_base.upper()):
            num = decoder(num, num_base)
        num = int(num, len(num_base))
        print(itoBase(num, base))


def itoBase(nb: int, base: str) -> str:
    """
    Функция конвертации числа из десятичной системы счисления в любую другую.

        :param nb: подаваемое число
        :type nb: int
        :param base: система счисления, передаваемая в виде элементов записанных в строку
        :type base: str

        :return: преобразованное, в нужную систему счисления, число.
        :rtype: str
    """
    if nb < len(base):
        return base[nb]
    else:
        return itoBase(nb // len(base), base) + base[nb % len(base)]


def decoder(num: str, base: str) -> str:
    """
    Функция приведения любой системы счисления в стандартную с основанием от 2 до 36

    :param num: подаваемое число
    :type num: str
    :param base: система счисления
    :type base: str

    :return: число в стандартной системе счисления с основанием от 2 до 36
    :rtype: str
    """
    to_base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    to_num = list(num)
    base = list(base)

    for i, elem in enumerate(to_num[:]):
        to_num[i] = to_base[base.index(elem)]

    return ''.join(to_num)


main()
