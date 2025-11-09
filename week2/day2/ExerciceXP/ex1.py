class Pets():
    def __init__(self, animals:list):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    # is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
    
class Siamese(Cat):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class Chartreux(Cat):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class Bengal(Cat):
    def __init__(self,**kwargs):

        super().__init__(**kwargs)


bengal_obj=Bengal(name="bengal",age=5)
chartreux_obj=Chartreux(name="chartreux",age=5)
siamese_obj=Siamese(name="siamese",age=5)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]


sara_pets=Pets(all_cats)
sara_pets.walk()