#Logic : you get a Guess character from user .if guess is not in the random word(word) a turn will be deducted and you will be shown remaining turns but if you have guessed the character correctly no turn deducted and you are asked for next character untill you guessed it all 



import random

name = input("Enter your Player Name :")
print(f"Welcome {name}. Best of Luck!")

turns = 12
words = ["Sam","Dictonary","rainbow","computer","science","english","mathematics","statistics","programming","water","board","geeks","for","reverse","player"]
# one random word from words list
word = random.choice(words)

print(f"Guess the {len(word)} Character word")
guesses = ""
while turns>0:
    #no. of times user failed
    failed = 0
    #Prints your guesses
    for char in word:
        if char in guesses :
            print(char,end="")
        else:
            print("_")
            failed += 1
    # if all character of the word are in guesses then it means that  you have guessed the word
    if failed == 0:
        print("\nYou win")
        print(f"The word is : {word}")
        break
    #Gets character from user
    Guess = input("Guess a character :")
    # add that guess in guesses
    guesses += Guess
    #main logic of checking character in word
    if Guess not in word:
        turns -= 1
        print("wrong")
        print(f"You have {turns} more guesses left")
        if turns ==0:
            print("You lose")