# Functions
**Functions** - is a group of related statements that perform a specific task. They help break our program into smaller
and modular chunks. That way, our code will be easier to organize.

## How do we create a functions? 
### Syntax:
`def function_name():`

**def keywoard** - is used to define a function. This allows you to create your own function.
#### Example:
```
def hello_function():
    print("Hello") #body of function
hello_function() #call the function
```

## Adding parameters 
**Parameter** - is a piece of information the function needs to do its job. The information is contained within ()
If your function does not get the argument it expects, running your code will lead to an error.
```
def hello_function(name): #name - parameter
    print("Hello " + name)
hello_function()
```

## Arguments
**Arguments** - is a piece of information that's passed from a function call to a function. This supplies the information the parameter requires.
```
def hello_function(name):
    print("Hello " + name) 
hello_function("Rose") #Rose - arguments
```

## Input Functions 
**input()** - allows us to ask users for some text input. Users can input data and our program will store it for them.

### Syntax:
`input("anything you want to say")`

**"Prompt"** - is the string that will be printed on the screen whenever the function is called. 
It also refers to the information that we'd want our users to enter

**Example: (inputting name)**
```
name = input("Enter your name: ") 
print("Hi!" + name)
```
**int() function + input() function**
int() - ensure that we get whole number

**Example:**
```
num1 = int(input("Enter your age: "))
print("What is your age? ")
```
```
def addnum(x,y): #def allows us to take a long block of code and shorten it so it can used again if needed
    total = x + y
    return (total)

x = int(input("First Number: "))
y = int(input("First Number: "))

print("Total: ", addnum(x,y))
```

# Data Types and Conversion
**Data Types** - are the different kinds of data we can store in a variable

**Types of data types**
1. Strings - are a sequence of characters such as word, phrase, or sentence. It's basically a plain text.
2. Numbers 
    -Integers 5
    -Float 5.0
3. Boolean - have a true or false value

## Data Conversion 
Built-in functions that convert one data type into another.
1. int() - converting it into an integer
Example:
```
print(int(74.63)) #Output - 74
```
2. float() - converting it into a float
Example:
```
print(float(34)) #Output - 34.0
```
3. str() - converting an number into a string
Example:
```
print(str(87))
```
4. tuple() -  converts strings into a tuple. Tuples are not mutable which they cannot be changed.
Example:
```
print(tuple("python")) #Output: ('p', 'y', 't', 'h', 'o', 'n')
```
5. list() - used to convert a string into a list. List are mutable which they can be changed.
Example:
```
print(list("programming")) ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
```

## Coding Exercise
You can view my [02Functions.py](https://github.com/AbbeyIT/Python-Beginner-Notes/blob/main/Coding-Exercise/02Functions.py) and [02InputFunctions.py](https://github.com/AbbeyIT/Python-Beginner-Notes/blob/main/Coding-Exercise/02InputFunctions.py) to see an example exercise for this topic.
