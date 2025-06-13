#In Python, self refers to the current instance of the class.
 #It is used to access variables and methods that belong to the class.
class student:
    def __init__(self, name):
        self.name =name
s1 = student("vineetha")
s2 = student("Sachin")
s3 = student("Sadhiv")
print(s1.name)
print(s2.name)
print(s3.name)