# define variables
Ages: list = []
total: int = 0
template: str = "How many people are buying tickets? "
count: int = 0  # to control nbr of family
per_nbr: int = 0
family_nbr: str = None
control_loop:int=0


# store the value incoming from the user
while control_loop<3:
    family_nbr = input(template)

    if family_nbr.isdigit() and len(family_nbr) <= 2:

        per_nbr = int(family_nbr)

        # this loop to draw family age
        while count < per_nbr:
            age = int(input(f"Enter the age of person {count+1}: "))
            Ages.append(age)
            count = count + 1

        # to calculate the price of every age
        for age in Ages:
            if age < 3:
                total = total
            elif 3 <= age <= 12:
                total += 10
            else:
                total += 15

        # to print total price
        print(f"total price is : {total}$")

    else:
        family_nbr = None
        template = "please enter degit number with 2 chiffre : "
        control_loop+=1

