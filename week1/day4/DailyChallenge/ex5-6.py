#ex5
def make_shirt(size="large",text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

#call the fucntion with different scenario

make_shirt(size="small", text="Hello!")
make_shirt(size="small")
make_shirt( text="Hello!")
make_shirt()

#ex6
magician_names:list =['Harry Houdini', 'David Blaine', 'Criss Angel']

#function that display magician name
def show_magicians(magician_names:list):
    if isinstance(magician_names,list):
     for name in magician_names:
        print(name)




#function that modify the list 
def make_great(magician_names:list):
   if isinstance(magician_names,list):
     for id,name in enumerate(magician_names):
        magician_names[id]="the great "+name
   

make_great(magician_names=magician_names)
show_magicians(magician_names=magician_names)