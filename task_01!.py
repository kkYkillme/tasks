import string

def is_palindrome(x):
    if x is None:
        print ("nope this is not palindrome")
        return
    x = str(x).lower()
    letters_numbers = set(string.ascii_lowercase + string.digits)
    bez_znakov = ''.join(char for char in x if char in letters_numbers)
    
    if bez_znakov == bez_znakov[::-1]:
        print ("yeap this is palindrome")
    else:
        print ("nope this is not palindrome")

is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")