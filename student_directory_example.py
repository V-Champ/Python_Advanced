#In Python, self refers to the current instance of the class.
 #It is used to access variables and methods that belong to the class.
#self---(.this in cpp/capl)
#__init__ ---A constructor method that runs when an object is created
class student:
    def __init__(self, name):#When a new Student is created, it should have a name, and I’ll store it in self.name.”
        self.name =name
s1 = student("vineetha") #init is called here
s2 = student("Sachin")
s3 = student("Sadhiv")#Here, self.name stores the name for each individual student object
print(s1.name)
print(s2.name)
print(s3.name)
#__init__ is a special method in Python classes. It’s called automatically when you create a new object from a class. 
#It’s used to initialize the object with specific values.