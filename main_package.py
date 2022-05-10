def to_decimal_from_binary(num: str) -> int:
    """
    Функция, которая переводит число num из двоичной системы счисления (оно записано в виде строки, тип str) в
    в десятичную. Например, 1001 -> 9: 1 * 2 ** 3 + 0 * 2 ** 2 + 0 * 2 ** 1 + 1 * 2 ** 0 = 9

    Parameters
    ----------
    num: str
        Число, которое нужно перевести в 10ую систему счисления

    Returns
    -------
    int
        Число в формате int, целое число - в десятичной записи
    """
    # ВОТ ЗДЕСЬ КОД, КОТОРЫЙ ПЕРЕВОДИТ num В ДЕСЯТИЧНОЕ ЦЕЛОЕ ЧИСЛО
    return num


print(to_decimal_from_binary('0'))  # -> 0
print(to_decimal_from_binary('1'))  # -> 1
print(to_decimal_from_binary('10'))  # -> 2
print(to_decimal_from_binary('11'))  # -> 3
print(to_decimal_from_binary('1100'))  # -> 12
print(to_decimal_from_binary('10000'))  # -> 16
print(to_decimal_from_binary('10010'))  # -> 18
