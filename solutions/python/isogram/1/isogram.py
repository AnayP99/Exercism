def is_isogram(string):
    count_dict = {}
    string = string.lower()
    for char in string:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1
    for char, count in count_dict.items():
        if char != " " and char != "-" and count > 1:
            return False
    return True
