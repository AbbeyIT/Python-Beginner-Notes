def summationOf(*num):
    sum = 0
    for x in num:
        sum += x
    return sum
    
print(summationOf(1, 65, 4, 257, 12, 83))