def is_valid(isbn):
    isbn = isbn.replace("-", "").lower()
    if len(isbn) != 10:
        return False
    if not isbn[:9].isdigit():
        return False
    if not (isbn[9].isdigit() or isbn[9] == "x"):
        return False
    sum = 0
    for i in range(10):
        if isbn[i] == "x":
            digit = 10
        else:
            digit = int(isbn[i])
        sum += digit * (10-i)
    return sum % 11 == 0
