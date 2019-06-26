class Cat:

	# inintializer
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __add__(self):
        return self.age 

# instatiate the Cat object
ken = Cat('ken', 7, 'brown')
duch = Cat('duch', 9, 'black-white')

print(ken.name, ken.age, ken.color)
print(ken.__add__ ())