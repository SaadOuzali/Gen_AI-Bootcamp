import random


def get_random_temp():
    return random.uniform(-10,40)

def main():
    rand_temp=get_random_temp()
    print("The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp <= 0:
       print("Brrr, that’s freezing! Wear some extra layers today.")
    elif  0< rand_temp <=16 :
        print("Quite chilly! Don’t forget your coat.")
    elif 16< rand_temp <=16:
        print("Nice weather")
    elif 24<= rand_temp <=32:
        print("A bit warm, stay hydrated. ")
    else:
       pass