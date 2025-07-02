def multiply_numbers(inputs):
    if not isinstance(inputs, str): 
        inputs = str(inputs)

    x = 1
    has_numbers = False
    
    for number in inputs:
        if number.isdigit():
            x = x * int(number)
            has_numbers = True
    return x if has_numbers else None


print (multiply_numbers("523"))
print (multiply_numbers("asd"))
print (multiply_numbers("1,5,3"))
print (multiply_numbers("2.7"))
