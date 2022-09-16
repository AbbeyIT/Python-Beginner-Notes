# Conditional Statements

## If 
**If** is for decision making operations. This creates a conditional statement and the code will only run if the condition is met.

**Example:**
```
num = 10
if num = 10:
    print("Hi Python")
```

## Else
**Else** provides an alternative solution in case both the if and elif are false.

**Example:**
```
x = 10
if x <= 10:
    print("x is greater than or equal to 10")
else:
    print("x is smaller than 10")
```

## Elif
**Elif** gives an alternative condition so that the code can have another chance to run. Used to create multiple conditional statements.

**Example:**
```
food_cost 
if food_cost > 400:
    print("Insufficient fund")
elif food_cost == 400:
    print("Sufficienct fund")
else:
    print("You still have money left")
```

## Loops and Iterations

**Iteration** is when the same procedure is repeated over and over again. 

**Loops** used to run same line of codes several times until condition is met. Loops allow codes to recur, so that our lives will be much easier.

## For 
**For Loops** - repeats a sequence until the condition is satisfied. A sequence can be a list, tuple, dictionary set, or string.

**Example:**
```
colors = ["green", "blue", "black", "yellow"]
for x in colors:
    print(x)

for x in "string":
    print(x) 
```

**Continue Statement** - skips the value of the variable and proceedes with the rest of the item in the list.

**Example:**
```
colors = ["green", "blue", "black", "yellow"]
for x in colors:
    if x == "blue":
        continue
    print(x)
```

**Break Statement** - if you want to stop the loop completely

**Example:**
```
colors = ["green", "blue", "black", "yellow"]
for x in colors:
    print(x)
    if x == "black":
        break
```

**Range Functions** -  this provides a sequence of numbers starting from 0 and ending at a number you specify. The code is then looped through that many 
number of times

**Example:**
```
x = range(8) #by default range starts at 0
for y in x:
    print(y)
```

**Nested keywoard** - is a loop within a loop

**Example:**
```
colors = ["green", "blue", "black", "yellow"]
things = ["laptop", "hard drive" "keyboard", "mouse"]

for x in colors:
    for y in colors:
        print(x,y)
```

## While Loop 
**While Loop** - these are used to iterate statements until it becomes false

**Example:**
```
i = 1 
while i <= 10:
    print(i)
    i += 1
```

**Continue Statement**

**Example:**
```
i = 0 
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)
```

**Else Statement**

**Example:**
```
i = 1
while i < 7:
    print(i)
    i +=  1
else:
    print("i is no longer less than 7")
```

## Exercise
You can view my [04Conditional.py](https://github.com/AbbeyIT/Python-Beginner-Notes/blob/main/Coding-Exercise/04Conditional.py) and [04Loops.py](https://github.com/AbbeyIT/Python-Beginner-Notes/blob/main/Coding-Exercise/04Loops.py) to see an example exercise for this topic.
