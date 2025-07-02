class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = None
        self._calories = 0
        self.name = name
        self.calories = calories

    @property     #Геттер
    def name(self):
        return self._name
    @name.setter     # Сеттер
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            self._name = None

    @property     # Геттер
    def calories(self):
        return self._calories
    @calories.setter   # Сеттер
    def calories(self, value):
        try:
            val = float(value)
            if val < 0:
                val = 0
            self._calories = val
        except (ValueError, TypeError):
            self._calories = 0 

    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True
    
    
    
d1 = Dessert("пирог", 555)
print(d1.is_healthy())  
print(d1.is_delicious())

d2 = Dessert("бананчик", 100)
print(d2.is_healthy())

d3 = Dessert("йогурт", "фывфыв")
print(d3.calories)
print(d3.is_healthy())