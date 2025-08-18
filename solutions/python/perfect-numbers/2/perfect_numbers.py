def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not number > 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0 if number==1 else 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum+=i
            if i != number//i:
                sum+=number//i
    if number == sum:
        return "perfect"
    if number < sum:
        return "abundant"
    return "deficient"
