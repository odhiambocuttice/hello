class Cat:

        # inintializer
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # # instance method
    def climb(self):
       return '{} {}'.format(self.name , self.age) 


r1 = Cat('muchi', 7, 'red')
r2 = Cat('jerry', 9, 'marron')

print(r1.climb())
