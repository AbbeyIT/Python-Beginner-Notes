# === Classes === #
"""
Object-oriented programming - is an approach that uses object and classes. It's convenient because OOP had the advantage of reusability. 
Object - created from a class. Objects contain and provide the information about a certain entity, such as their methods and properties. It is similar
to how a person possess certain attributes or skills. 
Classes - blueprint or templates for creating instances and objects. They help us organize our data and functions.
That way, classes could be reused or modified if necessary.
Example:
class newClass: 
    pass #placeholder so the program doesn't break
>If you dont write anythin in the class, it would result in an IndentationError
>If the class is the blueprint, the object is the actual thing based on the class, and the instance is the soft, or the digital copy of the class

- Instance -
>An instance is created when the class receives an argument. Because we add () to the name of the class, we have created an object. 
Syntax: 
instance = ClassName(argument)

- Class Variables -
Class variable - a variable declared within a class; values are constant across all instances of a class. It can be defined within a class but not 
within the methods of the class
Syntax:
class SampleClass:
    class_variable = "insert value here" 
instance = SampleClass(argument)
print(instance.class_variable) #access the object's class variable by using the "instance.variable" syntax
Example:
class Pets:
    looks = "Pretty"
rabbit = Pets()
print(hamster.looks)

- Instance Variable -
Instance Variables - they are specific to the objects the are attached to. They are also the variable that is defined within a method and is unique
to a certain instance. 
Example:
class Guest:
    pass
g_1 = Guest()
g_1.name() = #Instance Variable

- Attributes and Methods -
Attribute - variable stored in an instance or class 
Example:
class Guest:
    pass
g_1 = Guest()
g_1.name() = "Eve" #Eve is the attribute

Methods - functions stored in an instance or class
Example:
def __init__(self, name):
    self.name = name 

def introduce_Self(self):
    print("Hello I'm " + self.name)

Self - the first argument in a method is always the object that is calling the method. 
The only difference between the functions that we've been using and methods is that the methods needs an indent, since they are part of the class and 
cannot stand alone like regular function can.

Example:
class Guest:
    pass

g_1 = Guest() #Instance Variable
#attributes
g_1.first = "Eve" 
g_1.last = "Ha"
g_1.interest = "Dancing"

print(g_1.interest) #Output - "Dancing"
"""

# === Arithmetic Operators and Precedence === #
"""
- Arithmetic Operators - 
Arithmetic Operators - operators that deal with numeric values and used to perform mathematical operations
1. + (addition) 
2. - (substraction)
3. * (multiplication)
4. / (division)
5. % (Modulus Operator) - remainder
6. ** (Exponentiation Operator) - uses the second value as an exponent
Example:
print(7 ** 3)
7. // (Floor Division Operator) - rounds off the quotient

- Precedance - 
Precedence - is the order by which operations are performed
Operator 
()
**
*, /, //, %
>Exponential value have higher precedence over the basic arithmetic operators, like addition or substraction. However when we have an addition operator
encased with parentheses, this will be of higher precedence than the exponential values.
Example:
print((4-3)* 6 ** 2) #Output - 36
"""

# === Comparison and Logical Operators ===#
"""
Comparison Operators - compare two values. They indicate the difference between two values, such as if one is greater than or less than the other.
1. == - two values are the same
2. != - two values are not equal to each other
3. > - determines if the first value greater than to the other value 
4. < - determines if the first value smaller than to the other value
5. >= - determines if the first value greater than or equal to the other value
6. <= - determines if the first value smaller than or equal to the other value

Logical Operators - combine conditional statements
1. and - check if both statements are true
2. or - check if one of the statements is true
3. not - reverses the result  
"""