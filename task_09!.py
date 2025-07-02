def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        prioritet, vtoroi = dict1, dict2
    else:
        prioritet, vtoroi = dict2, dict1

    combined = {**vtoroi, **prioritet} 
    filtered = {keys: znachenie for keys, znachenie in combined.items() if znachenie >= 10}
    sorted_result = dict(sorted(filtered.items(), key=lambda item: item[1]))

    return sorted_result

d1 = {'a': 5, 'b': 15, 'c': 8}
d2 = {'b': 20, 'd': 30, 'e': 3}

print(connect_dicts(d1, d2))