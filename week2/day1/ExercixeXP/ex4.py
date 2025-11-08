class Zoo():
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals =[]
        self.sort_animals={}

    def add_animal(self,*args):
        if args not in self.animals:
            for an in args:
                self.animals.append(an) 

    def get_animals(self):
        for an in self.animals:
            print(an)

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)


    def sorted_animals(self):
        sorted_animals = sorted(self.animals)
        animal_keys=list(map(lambda an:an[0],sorted_animals))
        print(animal_keys)
        for animal in animal_keys:
            self.sort_animals[animal]=list(filter(lambda an:an[0]==animal ,sorted_animals))
        print(self.sort_animals)



    def get_groups(self):
        for key,animal in self.sort_animals.items():
            print(f"{key} : {animal}")


z=Zoo("ain_sebaa")


z.add_animal("Monkey","Lion","Baboon","Zebra","Cougar","Cat")
z.get_animals()

print("************************************")
z.sell_animal("king")
z.get_animals()

print("************************************")
z.sorted_animals()
z.get_groups()

