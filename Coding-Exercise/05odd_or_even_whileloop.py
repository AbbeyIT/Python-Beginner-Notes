num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

while i <len(num):
    if(num[i] % 2 == 0):
        print("Even Number: " + str(num[i]))
    else:
        print("Odd Number: " + str(num[i]))
    i += 1