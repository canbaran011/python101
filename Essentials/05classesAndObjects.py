class OneClass:
    variable = "aVARIABLE"

    def function(self):
        print("This is a message inside th class")

myobjectx = OneClass()  

# Accessing Object Variables

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yahooooo"

print(myobjectx.variable)
print(myobjecty.variable)

# Accessing Object Functions

myobjectx.function()

## Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.color = "red"
car1.value = 60000.00

car2.value = 10000.00
car2.name = "Jump"
car2.color = "blue"



# test code
print(car1.description())
print(car2.description())



