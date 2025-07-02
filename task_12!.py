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
    
    # 12 задание добавляем JellyBean
class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = None
        self.flavor = flavor

    @property # Геттер
    def flavor(self):
        return self._flavor
    @flavor.setter # Сеттер
    def flavor(self, value):
        if isinstance(value, str):
            self._flavor = value
        else:
            self._flavor = None

    def is_delicious(self):
        return self.flavor != "black licorice"
    
    
d1 = Dessert("пирог", 555)
print(d1.is_healthy())  
print(d1.is_delicious())

d2 = Dessert("бананчик", 100)
print(d2.is_healthy())

d3 = Dessert("йогурт", "фывфыв")
print(d3.calories)
print(d3.is_healthy())

d4 = JellyBean("jelly", 150, "strawberry")
print(d4.is_delicious())  # True
print(d4.is_healthy())

d5 = JellyBean("jelly", 150, "black licorice")
print(d5.is_delicious())  # False

d6 = JellyBean("jelly", 150, "123")
print(d6.is_delicious())  # False