def sum_of_multiples(limit, multiples):
    result = set()
    for number in multiples:
        if number != 0:
            for i in range(number, limit, number):
                result.add(i)
    return sum(result)