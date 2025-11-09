AGE:int=18

class Person():
    def __init__(self,first_name:str,age:int,last_name:str=""):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def is_18(self):
        return self.age >= AGE
    

class Family():
    def __init__(self,last_name:str,members:list[Person]=[]):
        self.last_name=last_name
        self.members=members

    def born(self,first_name, age):
        new_prs=Person(age=age,first_name=first_name,last_name=self.last_name)
        self.members.append(new_prs)

    def check_majority(self,first_name):
        get_person=list(filter(lambda prs:prs.first_name==first_name,self.members))
        if get_person[0].is_18():
            print("You are over 18, your parents Jane and John accept that you will go out with your friends")
        else:
            print("Sorry, you are not allowed to go out with your friends.")
        
