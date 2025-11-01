
template="Enter your name: "

while True:
    name = input(template)

    # Check if name is valid
    if not name.isdigit() and len(name) >= 3:
        print("Thank you!")
        break  
    else:
        #  print("give the correct name :")
        template="give the correct name :"
       
