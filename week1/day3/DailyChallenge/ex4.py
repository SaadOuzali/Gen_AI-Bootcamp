users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict1 = {name: index for index, name in enumerate(users)}
# result => {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
print(dict1)

# result => {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
dict2 = {index: name for index, name in enumerate(users)}
print(dict2)

# result => {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
sorted_dict = dict(sorted(dict1.items()))
