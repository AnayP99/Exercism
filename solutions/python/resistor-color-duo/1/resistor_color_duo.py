def value(colors):
    colors = colors[:2]
    first_color, second_color = colors
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
    color_code = f"{codes.index(first_color)}{codes.index(second_color)}"
    return int(color_code)
