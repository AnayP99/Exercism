def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        colors = ["black"] + colors
    value_bands = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    tolerance_bands = {
        "grey": "0.05",
        "violet": "0.1",
        "blue": "0.25",
        "green": "0.5",
        "brown": "1",
        "red": "2",
        "gold": "5",
        "silver": "10"
    }
    first = value_bands[colors[0]]
    second = value_bands[colors[1]]
    third = value_bands[colors[2]]
    multiplier = value_bands[colors[3]]
    tolerance = tolerance_bands[colors[4]]

    resistance = (first*100 + second*10 + third) * 10**multiplier
    for value, unit in [(10**6, "megaohms"), (10**3, "kiloohms")]:
        if resistance >= value:
            formatted = resistance/value
            if formatted.is_integer():
                formatted = int(formatted)
            return f"{formatted} {unit} ±{tolerance}%"
    return f"{resistance} ohms ±{tolerance}%"