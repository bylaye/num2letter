import base_french as bf

def decompose(number):
    tab = []
    if number == 0:
        return 0
    for unit in bf.UNIT:
        if number >= unit:
            multiplicand = number // unit
            number -= multiplicand * unit
            if multiplicand > 100:
                multiplicand_unit = multiple_100(multiplicand, unit)
                tab.append(multiplicand_unit)
            else:
                tab.append((multiplicand, unit))
        if number == 0:
            return tab
        if number <= 100:
            tab.append(number)
            return tab


def multiple_100(multiplicand, unit):
    out = []
    if multiplicand > 100:
        u, m = (multiplicand // 100), (multiplicand % 100)
    if u > 1:
        out.append(u)
    out.append(100)
    if m > 0:
        out.append(m)
    out.append(unit)
    return tuple(out)


def to_letter(number_decompose):
    if isinstance(number_decompose, int):
        return bf.num2letter[number_decompose]
    if isinstance(number_decompose, list):
        result = ''
        for val in number_decompose:
            if isinstance(val, tuple):
                if val[0] != 1:
                    result +=' '+bf.num2letter[val[0]]
                for v in list(val)[1:]:
                    result += ' '+bf.num2letter[v]
            else:
                result += ' '+bf.num2letter[val]
        return result

