import random

user_input = input("enter your input: ")
print(user_input)
computer_choice = ["Stone", "Paper", "Scissor"]
system_input = random.choice(computer_choice)
print(system_input)

if user_input == system_input:
  print("Its a Tie")
elif (user_input == "Stone" and system_input == "Scissor") or (user_input == "Paper" and system_input == "Stone") or (user_input == "Scissor" and system_input == "Paper"):
  print("You are the Winner")
else:
  print ("System is the winner")
