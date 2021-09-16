def main():
    request = input('Введите число и систему счисления (Пример: 13 0123456789abcdef):\n')
    request = request.split()
    try:
        num, base = request
        if len(base) < 2:
            raise ValueError
        num = int(num)
    except ValueError:
        print('usage')
    else:
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


main()
