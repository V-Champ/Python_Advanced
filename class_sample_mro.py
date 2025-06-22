class base_class:
    def __init__(obj,name,age,place):
        obj.name =name
        obj.age =age
        obj.place =place
        #print("in constructor or object instance is created ")
    def display(obj):
        print("Name :       "+obj.name)
        print("age :        "+str(obj.age))
        print("Place :      "+obj.place)

class child_class(base_class):
    def __init__(this,name,age,place,course):
        super().__init__(name,age,place)
        print("in child class")
        this.course =course

    def display_child(this):
        print("course :   "+this.course)


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(A,C):
    pass

#main
x=base_class("vineetha",32,"Chennai")
y=base_class("sachin",33,"sirusei")
x.display()
print("----------------------------")
y.display()
z =child_class("Sadhiv",3,"pudupakkam","computer")
z.display()
z.display_child()

obj = D()
obj.show()
print(D.__mro__)
