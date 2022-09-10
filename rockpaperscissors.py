import random

def main():
    while True:
        possible_actions = ['Rock','Paper','Scissors']
        user_action = str(input('Rock, Paper, or Scissors?: '))
        if user_action in possible_actions:
            computer_action = random.choice(possible_actions)
            checkWin(user_action, computer_action)
            decision = input('Do you want to play again? Y/N: ')
            if decision == "N":
                quit()
        else:
            print("Incorrect input, please try again")

def checkWin(user_action, computer_action):
    if user_action == computer_action:
        print(computer_action)
        print('Tie!')
    elif user_action == 'Rock' and computer_action == 'Paper':
        print(computer_action)
        print('You Lose!')
    elif user_action == 'Rock' and computer_action == 'Scissors':
        print(computer_action)
        print('You Win!')
    elif user_action == 'Paper' and computer_action == 'Scissors':
        print(computer_action)
        print('You Lose!')
    elif user_action == 'Paper' and computer_action == 'Rock':
        print(computer_action)
        print('You win!')
    elif user_action == 'Scissors' and computer_action == 'Rock':
        print(computer_action)
        print('You Lose!')
    elif user_action == 'Scissors' and computer_action == 'Paper':
        print(computer_action)
        print('You Win!')

main()