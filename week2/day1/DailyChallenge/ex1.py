class Farm():
    def __init__(self,farm_name,animals={} ):
        self.farm_name=farm_name
        self.animals =animals
        self

    def add_animal_v1(self,animal_type,count=1):
        if animal_type in self.animals:
          self.animals[animal_type]+=1
        else:
            self.animals[animal_type]=count


    def add_animal_v2(self,**kwargs):
        print(kwargs)
        self.animals=kwargs
       

    def get_info(self):
        print(f"{self.farm_name} farm")
        for key,value in self.animals.items():
            print(f"{key} : {value}")
        print("\t E-I-E-I-0!")


    def get_animal_types(self):
        return list(sorted(self.animals.items()))


farm=Farm("McDonald")
farm.add_animal_v1("horse")
farm.add_animal_v1("horse")
farm.add_animal_v1("horse")
farm.add_animal_v1('cow', 5)
farm.add_animal_v1('goat', 12)
print(farm.animals)
farm.get_info()
print(farm.get_animal_types())

farm.add_animal_v2(horse=3,cow=5,goat=12)
farm.get_info()
print(farm.get_animal_types())