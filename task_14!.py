class EvenNumbers:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield 2 * i
   
evens = EvenNumbers(5)
for num in evens:
    print(num)
