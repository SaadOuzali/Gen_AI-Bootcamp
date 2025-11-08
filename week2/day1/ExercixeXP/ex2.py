
class Dog():
    def __init__(self,name,height):
        self.name=name
        self.height=height

    def bark(self):
        print(f"dog name is {self.name}")
    
    def jump(self):
        x=self.height*2
        print(f"{self.name} jumps {x} cm high ")

sarahs_dog=Dog(name="sarahs",height=10)
davids_dog=Dog(name="davids",height=20)

sarahs_dog.bark()
sarahs_dog.jump()

davids_dog.bark()
davids_dog.jump()