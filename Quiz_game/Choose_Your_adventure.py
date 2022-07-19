print("Welcome to my Computer quiz!")

playing = input("Do you want to play a game? ")
playing = str.lower(playing)
if playing != 'yes':
    quit()
print("Okay lets play (:")

# Set the score
score = 0

# Question 1
answer1 = input ("What does CPU stand for?").lower()


if answer1 == "central processing unit":
    score += 1 # score = score + 1
    print("You are correct")
else:
    print("You are incorrect.")

# Question 2
answer2 = input ("What does GPU stand for? ").lower()
answer2 = str.lower(answer2)

if answer2 == "graphics processing unit":
    score += 1  # score = score + 1
    print("You are correct")
else:
    print("You are incorrect.")

# Question 3
answer3 = input ("What does RAM stand for? ").lower()

if answer3 == "random access memory":
    score += 1  # score = score + 1
    print("You are correct")
else:
    print("You are incorrect.")

# Question 4
answer4 = input ("What does PSU stand for? ").lower()

if answer4 == "power supply":
    score += 1  # score = score + 1
    print("You are correct")
else:
    print("You are incorrect.")

print("You got " + str((score/4) * 100) + "%")