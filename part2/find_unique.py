def find_unique(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    
    result = []
    for item in items:
        if counts[item] == 1:
            result.append(item)
    return result