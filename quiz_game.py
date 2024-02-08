print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

user_reply = input("Are you ready for your first question? ")
if user_reply.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :)")

score = 0

# Question 1
answer_1 = input("What does CPU stand for? ")
if answer_1.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

# Question 2
answer_2 = input("What does AWS stand for? ")
if answer_2.lower() == 'amazon web services':
    print('Correct again!')
    score += 1
else:
    print("Sorry, that's incorrect")

# Question 3
answer_3 = input("What is the opposite of North? ")
if answer_3.lower() == "south":
    print('Another one correct! Good job!')
    score += 1
else:
    print("Sorry, that's incorrect")

print("You got", score, "questions correct!")
print("You got {:.2%}.".format(score / 3))
