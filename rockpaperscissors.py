import random

user_action = str(input('Rock, Paper, or Scissors?: '))
possible_actions = ['rock','paper','scissors']
computer_action = random.choice(possible_actions)

print(computer_action)