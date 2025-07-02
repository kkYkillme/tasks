def coincidence(liist=None, raange=None):
    if not liist or not raange:
        return []
    result = []
    for x in liist:
        if x in raange:
            result.append(x)
    return result
print(coincidence([5,"asf", 3, 2, 7, "ccc", 23], range(3, 12)))  