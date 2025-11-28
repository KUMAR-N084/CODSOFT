import random

# Rock Paper Scissors ASCII Art

# Rock
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [ROCK, PAPER, SCISSORS]

print('''Welcome to Rock, Paper, Scissors!
Instructions:
- Type 'rock', 'paper', or 'scissors' (or 0, 1, 2).
- Rock beats Scissors, Scissors beat Paper, Paper beats Rock.
- Invalid inputs will count as a loss for you.
- Scores will be tracked: Wins, Losses, and Draws.
- Type 'exit' at any time to quit.
Let's play!\n''')

# Initial scores
user_score = 0
computer_score = 0
draws = 0

while True:
    while True:
        user_input_str = input("What do you choose? Type 'rock/0', 'paper/1', 'scissors/2', or 'exit': ").lower().strip()
        if user_input_str == 'exit':
            print("Thanks for playing! Here's your final score:")
            print(f"Final Scores - You: {user_score} Wins, Computer: {computer_score} Wins, Draws: {draws}")
            print("Goodbye!")
            exit()
        elif user_input_str in ['rock', '0']:
            user_input = 0
            break
        elif user_input_str in ['paper', '1']:
            user_input = 1
            break
        elif user_input_str in ['scissors', '2']:
            user_input = 2
            break
        else:
            print("Invalid choice! Please enter 'rock/0', 'paper/1', 'scissors/2', or 'exit'.")

    print(f"You chose: {user_input}")
    print(game_images[user_input])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(game_images[computer_choice])

    if user_input == 0 and computer_choice == 2:
        print("Great job! Rock smashes Scissors. You win!")
        user_score += 1
    elif computer_choice == 0 and user_input == 2:
        print("Oh no! Rock smashes Scissors. You lose!")
        computer_score += 1
    elif computer_choice > user_input:
        print("Sorry! You lose this round.")
        computer_score += 1
    elif user_input > computer_choice:
        print("Awesome! You win this round!")
        user_score += 1
    elif computer_choice == user_input:
        print("It's a tie! Good match.")
        draws += 1

    # Display's current scores
    print(f"\nCurrent Scores - You: {user_score} Wins, Computer: {computer_score} Wins, Draws: {draws}\n")
