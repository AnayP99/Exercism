def score(x, y):
    distance = (x*x + y*y) ** 0.5
    if distance <= 1:
        return 10
    if 5 < distance <= 10:
        return 1
    if 1 < distance <= 5:
        return 5
    return 0