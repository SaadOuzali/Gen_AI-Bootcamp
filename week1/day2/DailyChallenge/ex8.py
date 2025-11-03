
template: str = "enter pizza toppings : "
topping_list: list = []
BASE_PRICE: int = 10
TOOPING_PRICE: int = 2.5


while True:
    pza_topping = input(template)
    if pza_topping == "quit":
        break
    else:
        topping_list.append(pza_topping)
        template = "Adding [topping] to your pizza : "

if len(topping_list) == 0:
    print(f"the total cost of the pizza : {BASE_PRICE}")
else:
    total_price = (len(topping_list) * TOOPING_PRICE) + BASE_PRICE
    print(f"the total cost of the pizza : {total_price} \n")
    print(f"your Topping is : {topping_list}")
