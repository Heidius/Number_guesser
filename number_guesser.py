import random

top_of_range = input("Introduce a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number largar than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randrange(0, top_of_range) # it could be -1 to 11 so would cover 0 to 10
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): #To make sure input = digit
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        print("Siuu!")
        break
    elif user_guess > random_number: #elif instead of else: to clean up the code a bit
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
#This is the same that ("You git it in" + str(guesses) + " guesses")