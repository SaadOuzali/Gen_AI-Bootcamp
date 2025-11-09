class Dog():
    def __init__(self,name:str,age:int,weight:int):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self,other_dog:Dog):
        current_dog_val=self.run_speed()*self.weight
        other_dog_val=other_dog.run_speed()*other_dog.weight
        if current_dog_val > other_dog_val:
            return f"the winner is {self.name} is win"
        else:
            return f"the winner is {other_dog.name} "
        

dog1_obj=Dog("rex",5,30)
dog2_obj=Dog("john",8,20)

print(dog1_obj.bark())
print(dog1_obj.run_speed())
print(dog2_obj.run_speed())
print(dog1_obj.fight(dog2_obj))
