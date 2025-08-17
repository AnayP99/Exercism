def is_armstrong_number(number):
    no_of_digits = len(str(number))
    sum = 0
    n = number
    while (n > 0):
        digit = n%10
        sum += digit ** no_of_digits
        n//=10
    return sum == number
