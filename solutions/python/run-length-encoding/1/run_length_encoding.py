def decode(string):
    if not string:
        return ""
    result = ""
    count = ""
    for char in string:
        if char.isdigit():
            count+=char
        else:
            if count:
                result += char * int(count)
                count = ""
            else:
                result += char
    return result

def encode(string):
    if not string:
        return ""
    result = ""
    count=1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count+=1
        else:
            if count > 1:
                result+=str(count) + string[i-1]
            else:
                result+=string[i-1]
            count = 1
    if count > 1:
        result+= str(count) + string[-1]
    else:
        result+= string[-1]
    return result
