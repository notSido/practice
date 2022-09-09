import random



while True:
    user_action = str(input('Rock, Paper, or Scissors?: '))
    possible_actions = ['Rock','Paper','Scissors']
    computer_action = random.choice(possible_actions)
    def WinLoss():
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
        else:
            raise Exception('Invalid Input')    
    WinLoss()
    decision = input('Do you want to play again? Y/N: ')
    if decision == 'N':
        break
