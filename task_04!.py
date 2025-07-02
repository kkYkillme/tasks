def sort_list(list):
    if not list:
        return list

    mini = min(list)
    maxi = max(list)

    # Меняем местами все min и max
    result = []
    for number in list:
        if number == mini:
            result.append(maxi)
        elif number == maxi:
            result.append(mini)
        else:
            result.append(number)

    result.append(mini)
    return result

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))