def count_words(string):
    words = string.lower().split() 
    chetchik = {}

    for word in words:
        if word in chetchik:
            chetchik[word] += 1
        else:
            chetchik[word] = 1

    return chetchik

x = "привет, меня зовут мистер бист я привет меня зовут роналду"
print (count_words(x))