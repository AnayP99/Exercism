import re

def is_vowel(letter):
    return letter in 'aeiou'

def translate_word(word):
    # Rule 1: Starts with a vowel or "xr" or "yt"
    if word.startswith(('xr', 'yt')) or is_vowel(word[0]):
        return word + 'ay'

    # Rule 3: Starts with consonant(s) followed by "qu"
    match_qu = re.match(r'^([^aeiou]*qu)(.*)', word)
    if match_qu:
        return match_qu.group(2) + match_qu.group(1) + 'ay'

    # Rule 4: Starts with consonant(s) followed by 'y' (and 'y' not at the start)
    match_y = re.match(r'^([^aeiou]+)(y.*)', word)
    if match_y:
        return match_y.group(2) + match_y.group(1) + 'ay'

    # Rule 2: Starts with consonant(s)
    match_cons = re.match(r'^([^aeiou]+)(.*)', word)
    if match_cons:
        return match_cons.group(2) + match_cons.group(1) + 'ay'

    # Fallback (should not happen if rules above are correct)
    return word + 'ay'

def translate(phrase):
    return ' '.join(translate_word(word) for word in phrase.split())
