#We can overload constructors based on the type or number of arguments passed to the __init__() method. 
#This will allow a single constructor method to handle various initialization scenarios based on the arguments provided.
class Student:
   def __init__(self, *args):
      if len(args) == 1:
         self.name = args[0]
        
      elif len(args) == 2:
         self.name = args[0]
         self.age = args[1]
        
      elif len(args) == 3:
         self.name = args[0]
         self.age = args[1]
         self.gender = args[2]
            
st1 = Student("Shrey")
print("Name:", st1.name)
st2 = Student("Ram", 25)
print(f"Name: {st2.name} and Age: {st2.age}")
st3 = Student("Shyam", 26, "M")
print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")