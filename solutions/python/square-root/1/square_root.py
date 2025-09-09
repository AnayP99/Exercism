def square_root(number):
    low = 0
    high = number
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        if mid * mid > number:
            high = mid - 1 
        else:
            low = mid + 1
