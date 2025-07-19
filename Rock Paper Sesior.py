import random

def get_user_choice():
    while True:
        user = input("Choose Rock, Paper, or Scissors: ").lower()
        if user in ['rock', 'paper', 'scissors']:
            return user
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"You chose: {user.capitalize()}")
        print(f"Computer chose: {computer.capitalize()}")

        winner = determine_winner(user, computer)
        if winner == "tie":
            print("Result: It's a Tie!")
        elif winner == "user":
            print("Result: You Win!")
            user_score += 1
        else:
            print("Result: Computer Wins!")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("\nThanks for playing!")
            break

        round_number += 1

# Run the game
if __name__ == "__main__":
    print("=== Welcome to Rock-Paper-Scissors Game ===")
    play_game()