def steps(number):
    if not number > 0:
        raise ValueError("Only positive integers are allowed")
    no_of_steps = 0
    while (number != 1):
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        no_of_steps += 1
    return no_of_steps
