def abbreviate(words):
    result = ""
    subwords = words.replace("-", " ").replace("_", "").split(" ")
    for word in subwords:
        if word:
            result+=word[0]
    print(subwords)
    return result.upper()
