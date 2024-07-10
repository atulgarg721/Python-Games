import random

name = input("Enter your Player Name :")
print(f"Welcome {name}. Best of Luck!")

turns = 12
words = ["Sam","Dictonary","rainbow","computer","science","english","mathematics","statistics","programming","water","board","geeks","for","reverse","player"]
# one random word from words list
word = random.choice(words)

print(f"Guess the {len(word)} word Characters")
guesses = ""
while turns>0:
    #no. of times user failed
    failed = 0
    for char in word:
        if char in guesses :
            print(char,end="")
        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print("\nYou win")
        print(f"The word is : {word}")
        break
    Guess = input("Guess a character :")
    guesses += Guess
    if Guess not in word:
        turns -= 1
        print("wrong")
        print(f"You have {turns} more guesses left")
        if turns ==0:
            print("You lose")
