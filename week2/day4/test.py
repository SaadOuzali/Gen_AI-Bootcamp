import os,json



# json.dump()  ---->Writes Python object → JSON file.
# json.dumps() ---> Converts Python object → JSON string (keeps it in memory).






# __file__ is a special variable that holds the current file name
dir_path = os.path.dirname(os.path.abspath(__file__))
print("Directory path:", dir_path)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.txt")


#to write in file
with open(file=file_path, mode="w") as f:
    f.write(
        "Un texte est une séquence de signes linguistiques (écrite ou orale) qui forme un tout cohérent et qui est porteur de sens. Ce terme peut aussi faire référence à un ensemble de phrases et de mots qui constituent un écrit, une œuvre ou un fichier informatique. Il existe différents types de textes, comme les textes narratifs, descriptifs ou argumentatifs. "
    )  # writes text


#behind the scene the interpreter transform with (sugar syntax) to :
# f = open(file_path, "a")
# try: 
#     f.write("\nhhhhhhhhh")
# finally:
#     f.close()

#to append to a file not ovveride
with open(file=file_path, mode="a") as f:
    f.write("\nhhhhhhhhh")

#to read the content of file
with open(file_path, "r") as f:
    data = f.read()
    print(data)

my_family = {
    "parents" :['Beth', 'Jerry'],
    "children" :['Summer', 'Morty']
}


json_my_family = json.dumps(my_family)
print(json_my_family)


my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "my_file.json"


#the equivalent syntax of :
# file = open("data.json", "w")
# try:
#     json.dump(data, file, indent=4)
# finally:
#     file.close()
#is this:
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),json_file), 'w') as file_obj:
    json.dump(my_family, file_obj)