import re
from collections import Counter

def count_words(subtitle: str) -> dict:
    subtitle = subtitle.lower()

    # Match words with optional inner apostrophes, but not starting/ending with apostrophe
    # Explanation:
    # [a-z0-9]+         → start with one or more letters/digits
    # (?:'[a-z0-9]+)*   → followed by zero or more 'word' parts (e.g., 're, 's, 've)
    # This prevents leading/trailing apostrophes from being part of the word
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", subtitle)

    return dict(Counter(words))
