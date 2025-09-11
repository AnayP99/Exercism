def say(number):
    if not 0 <= number < 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    units = [
        "", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    multiplier = ["", "thousand", "million", "billion"]
    result = ""
    group = 0
    while number > 0:
        if number % 1000 != 0:
            value = number % 1000
            temp = ""
            if value >= 100:
                temp += units[value // 100] + " hundred"
                value %= 100
                if value > 0:
                    temp += " "
            if value >= 20:
                temp += tens[value // 10]
                value %= 10
                if value > 0:
                    temp += "-"
            if value > 0:
                temp += units[value]
            if group > 0:
                temp += " " + multiplier[group]
            temp += " "
            result = temp + result
        number //= 1000
        group += 1
    return result.strip()