# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Modify the class before it's created
        print(f"Creating class: {name}")
        dct['greet'] = lambda self: f"Hello from {name}!"
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a class
class MyClass(metaclass=MyMeta):
    def __init__(self):
        self.data = "Sample Data"

# Instantiate the class
obj = MyClass()

# Call the dynamically added method
print(obj.greet())
