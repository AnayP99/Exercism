def find_anagrams(word, candidates):
    word = word.lower()
    result = []
    for candidate in candidates:
        anagram = candidate.lower()
        if word != anagram and sorted(word) == sorted(anagram):
            result.append(candidate)
    return result
    
