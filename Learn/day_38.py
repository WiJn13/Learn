# TITLE: 继承中的初始化参数传递
# CATEGORY: 面向对象编程
# day_38.py


class Animal:
    def __init__(self, name, breed, colour, character):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.character = character
    
class Dog(Animal):
    def __init__(self, size):
        self.size = size

a = Dog(f'{13}英寸')
print(a. size)

class Cat(Animal):
    def __init__(self, personality, *args):
        super().__init__(*args)
        self.personality = personality
b = Cat('好的','咪咪', '英短', '白色', '小小的')
print(b.colour)

class Zebra(Animal):
    def __init__(self, stripes, **kwargs):
        super().__init__(**kwargs)
        self.stripes = stripes
c = Zebra(
    stripes=24,
    name='DASH',
    breed='某某',
    character='还行',
    colour='black and white'
)
print(c.stripes)

class Doplin(Animal):
    def __init__(self, name, colour, breed, character):
        super().__init__(
            name=breed,
            breed=name,
            character=character,
            colour=colour
        )
d = Doplin(name='种类',
           colour='blue',
           breed='名称',
           character='温顺的')
print(d.name)

class Doplin1(Animal):
    def __init__(self, name, colour, character, breed):
        super().__init__(
            colour, name, character,breed)
e = Doplin1(name='名字',
            colour='blue',
            breed='种类',
            character='好好的')
print(e.character)
