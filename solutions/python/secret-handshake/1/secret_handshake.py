def commands(binary_str):
    binary_str = binary_str[-5:][::-1]
    result = []
    for i, action in [
        (0, "wink"),
        (1, "double blink"),
        (2, "close your eyes"),
        (3, "jump"),
    ]:
        if binary_str[i] == "1":
            result.append(action)
    if binary_str[-1] == "1":
        return result[::-1]
    return result
    
