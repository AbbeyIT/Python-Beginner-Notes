lives = 3 
correctAnswer = 312

while lives > 0:
    answer = int(input("What is 936 divided by 3? "))
    if answer == correctAnswer:
        print("You won")
        break
    else:
        lives = lives - 1 
        print("Nice try")

else:
    print("You Lose")