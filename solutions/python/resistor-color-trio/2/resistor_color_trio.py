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
    first = codes.index(colors[0])
    second = codes.index(colors[1])
    multiplier = codes.index(colors[2])
    
    value = (first * 10 + second) * 10 ** multiplier

    if value == 0:
        return "0 ohms"
    
    for factor, unit in [(10**9, "gigaohms"), (10**6, "megaohms"), (10**3, "kiloohms")]:
        if value % factor == 0:
            return f"{int(value//factor)} {unit}"
    return f"{int(value)} ohms"
