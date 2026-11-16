def are_anagrams(a, b):
    return sorted(a.lower()) == sorted(b.lower())