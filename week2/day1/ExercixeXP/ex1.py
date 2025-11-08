

class Cat():
    def __init__(self,cat_name,cat_age):
        self.name=cat_name
        self.age=cat_age

    def find_oldest_cat(self,cat1:Cat,cat2:Cat):
        old=max([self,cat1,cat2],key=lambda c:c.age)
        
        print(f"the old cat is name: {old.name} and {old.age} years old")
        # elif cat1.age > cat2.age > sel

cat_1=Cat("kitty",4)
cat_2=Cat("kitty",5)
cat_3=Cat("kitty",8)

cat_1.find_oldest_cat(cat1=cat_2,cat2=cat_3)