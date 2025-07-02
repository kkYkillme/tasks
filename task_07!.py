def combine_anagrams(words_array):
    slovar = {}  

    for word in words_array:
        bukvi = ''.join(sorted(word.lower()))
        if bukvi in slovar:
            slovar[bukvi].append(word)
        else:
            slovar[bukvi] = [word]

    # Возвращаем только списки слов (группы анаграмм)
    return list(slovar.values())

words = ["sad", "dsa", "people", "hala", "aloha", "haloa"]
print(combine_anagrams(words))