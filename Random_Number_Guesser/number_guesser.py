import random

top_of_range = input("Type a number: ") # This will be a string

if top_of_range.isdigit(): # Checks to make sure the number is actually a number
    top_of_range = int(top_of_range) # Converts the string to an integer

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")

else:
    print("Please type a number next time.")
    quit()

# Random number
# r = (random.randrange(0, 21)) # 0-20 needs to be one more than what you want
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess:")
    if user_guess.isdigit():  # Checks to make sure the number is actually a number
        user_guess = int(user_guess)  # Converts the string to an integer
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
print("You got it in", guesses, "guesses")