def roman(number):
    base = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    result = ""
    i = len(base) - 1
    while number > 0:
        div = number // base[i]
        result += romans[i] * div
        number %= base[i]
        i -= 1
    return result

