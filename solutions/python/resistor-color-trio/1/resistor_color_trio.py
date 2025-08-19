def label(colors):
    codes = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
    colors = colors[:3]
    first_color, second_color, third_color = colors
    multiplier = codes.index(third_color)
    value = (codes.index(first_color) * 10 + codes.index(second_color)) * 10 ** multiplier
    if not value:
        return "0 ohms"
    if value % 10**9 == 0:
        suffix = "gigaohms"
        value /= 10**9
    elif value % 10**6 == 0:
        suffix = "megaohms"
        value /= 10**6
    elif value % 10**3 == 0:
        suffix = "kiloohms"
        value /= 10**3
    else:
        suffix = "ohms"
    return f"{int(value)} {suffix}"
    
    
