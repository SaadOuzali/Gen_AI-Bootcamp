# define variables
total: int = 0
template: str = "How many people are buying tickets ?  "
per_nbr: int = 0
family_nbr: str = None
family_dict:dict={}
prs_price_dict:dict={}

# store the value incoming from the user

family_nbr = input(template)
    
if family_nbr.isdigit() and len(family_nbr) <= 2:

        per_nbr = int(family_nbr)

        # this loop to draw family age
        while count < per_nbr:
            age = int(input(f"Enter the age of person {count+1}: "))
            prs_name = input(f"Enter the name of person {count+1}: ")
            family_dict[prs_name]=age
            count = count + 1
        else:
            print(family_dict)
            
        # to calculate the price of every age
        for key,value in family_dict.items():
             if value < 3:
                 total = total
                 prs_price_dict[key]="0$"
             elif 3 <= value <= 12:
                 total += 10
                 prs_price_dict[key]="10$"
             else:
                 total += 15
                 prs_price_dict[key]="15$"
        else:
            print(f"the price of every person :{prs_price_dict} ")
            print(f"total price is : {total}$")
        


