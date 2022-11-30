#IMPORTS
import time
import random

#INTRODUCTION
print("\n--------------------------BAGELS---------------------------\n")
print("I am thinking of a 3-digit number. Try to guess what it is.\n")
time.sleep(3)
print("Here are some clues: \n")
time.sleep(2)
print("""
When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.\n
""")
time.sleep(5)
print("I have thought of a number")

#random number generator
def rando():
    rando = str(random.randint(100,999))
    random_number = [int(x) for x in rando]
    return random_number

#function to handle user input collection
def take_guess():
    guess = input("Guess a 3 digit number:> ")
    if len(guess)==3:
        guess = [int(x) for x in guess]
        return guess
    else:
        print('invalid input')
        return None

#function to generate clues
def clues(guess,secretnum):
    if guess == secretnum:
        return "You got it"
    clue_list = []
    for i in range(len(secretnum)):
        if guess[i] == secretnum[i]:
            clue_list.append('Fermi')
        elif secretnum[i] in guess:
            clue_list.append('Pico')
    if len(clue_list) == 0:
        return "Bagels"
    else:
        clue_list.sort()
        return ' '.join(clue_list)

#GAME LOGIC
while True:
    guesses_left = 10
    random_number = rando()
    while guesses_left>0:            
        user_guess = None
        while user_guess==None:
            user_guess = take_guess()
        check = clues(user_guess,random_number)
        if check == "You got it":
            print("\n\nCONGRATULATIONS\n"+check+"!!!")
            time.sleep(3)
            break
        else:
            print(check)
            guesses_left-=1
            print(f"\nYou have {guesses_left} guesses left")
    
    if guesses_left==0:
        print("\nYou have run out of guesses :(\n")
    print("\nWant to play again?")
    if input("> ").upper() == 'N':
        break
    else:
        continue

