import random

def guess():
    random_number = random.randint(1,10)
    print(random_number)

    guess = 0
    while guess != random_number:
        guess = int(input("guess a number "))
        if guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        else:
            print("Correct")
            break


guess()
