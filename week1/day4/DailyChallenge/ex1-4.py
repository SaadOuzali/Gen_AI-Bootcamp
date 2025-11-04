import random


def display_message():
    print("I am learning about functions in Python.")


display_message()


#ex2
def favorite_book(title:str):
    print(f"One of my favorite books is {title.title()}")
    
#call the fnct
favorite_book("Alice in Wonderland")


#ex3
def describe_city(country,city="Unknown"):
    print(f"{city} is in {country}")

#call the function 
describe_city("Reykjavik", "Iceland")
describe_city("london", )
    

#ex4
def check_num(num:int):
   if 1<= num <=100 :
    rand_var= random.randint(1, 100)
    if num == rand_var:
       print("Success !")
    else:
       print(f"Your number: {num}, Random number: {rand_var}")
   else:
      print("please enter a number between 1 and 100")

#call the fnct
check_num(400)


