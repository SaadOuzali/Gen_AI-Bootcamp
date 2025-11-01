#ex2
tu=(1,2,3,5,6)
#cannot add another integer tuple is immutable

#ex3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")
print(f" the word 'Apples' appear in the list: {basket.count("Apples")} \n")
basket.clear()
print(basket)



#ex4
nbr=[i*0.5 for i in range(3,11)]
print(nbr)



#ex5
#numbers from 1 to 20,inclusive
for i in range(1,21):
    print(i)

#print all number from 1 to 20 where the index is even.
for j in range (0,21,2):
    print(j)




