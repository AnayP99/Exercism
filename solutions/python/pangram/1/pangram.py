def is_pangram(sentence):
    sentence = sentence.lower()
    for alphabet in range (ord('a'), ord('z') + 1):
        if chr(alphabet) not in sentence:
            return False
    return True
