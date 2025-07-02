def max_odd(array):
    odd_number = None
    for number in array:
        if isinstance(number, (int, float)):
            _number = int(number)
            if _number % 2 == 1:
                if odd_number is None or _number > odd_number:
                    odd_number = _number
    return odd_number


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) 
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
