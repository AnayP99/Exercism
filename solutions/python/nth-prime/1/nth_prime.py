def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    n = 999999
    flags = [True for i in range(n+1)]
    flags[0] = flags[1] = False
    i = 2
    while(i*i <= n):
        if flags[i]:
            for j in range(i*i, n+1, i):
                flags[j] = False
        i+=1
    result = []
    for p in range(2, n+1):
        if flags[p]:
            result.append(p)
    return result[number-1]
