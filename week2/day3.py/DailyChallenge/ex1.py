import math

PI=math.pi

class Circle():
    def __init__(self,radius:float):
        if radius >0 :
            self.__radius=radius 
        else:
            raise ValueError("the value entred must be positive ")
        
    def get_radius(self):
        return self.__radius
    
    def set_radius(self,radius:float):
        self.__radius=radius
        
    def circle_area(self):
        radius:float=self.__radius
        return PI*radius**2
    
    def __str__(self):
       return f"attribute of {self.__class__.__name__} : 'radius' , 'area' "
    
    def __repr__(self):   # ✅ this must be exactly like this
        return f"Circle(radius={self.__radius:.2f}, area={self.circle_area():.2f})"
    
    def __add__(self,other:Circle):
        if isinstance(other,Circle):
         return self.__radius+other.get_radius()
        else:
            raise ValueError("the object passed must be Circle type")

    def __gt__(self,other:Circle):
        if isinstance(other,Circle):
          return self.__radius > other.get_radius()
        else:
            raise ValueError("the object passed must be Circle type")
        
    def __eq__(self,other:Circle):
        if isinstance(other,Circle):
          return self.__radius == other.get_radius()
        else:
            raise ValueError("the object passed must be Circle type")

     
    
cir_1=Circle(radius=15)
cir_2=Circle(radius=17)
print(cir_1)
print(cir_1.get_radius())

print(cir_1+cir_2)
print(cir_1>cir_2)
print(cir_1==cir_2)
v=list(sorted([cir_1,cir_2]))
print(v)




