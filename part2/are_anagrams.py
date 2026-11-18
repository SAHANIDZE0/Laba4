def are_anagrams(a, b):
    """Принимает две строки, возвращает True, если они являются анаграммами, иначе False."""
    return sorted(a.lower()) == sorted(b.lower())