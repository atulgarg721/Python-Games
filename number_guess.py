import random
name = input("Hello Player! please enter your name :")
print(f"Welcome {name}. Please enjoy the game. \n")
#get range from user
a = int(input("Enter the range starting value :"))
b = int(input("ENter the range ending value : "))
#random number from the range
num = random.choice(range(a,b))
tries = 0
guess= None
while True:
    guess = int(input("Enter your Guess number: "))
    if guess != num:
        if guess > num:
            print("Try Again, You have Guessed Too High")
        else:
            print("Try Again, You have Guessed Too Low")
        tries += 1
    else :
        print(f"Congratulations !! You have guess the number {num} in {tries} tries")
        break