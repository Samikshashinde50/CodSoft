import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ["rock", "paper", "scissors"]

print("===== ROCK PAPER SCISSORS GAME =====")

while True:

    # User input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print("\n===== SCORE BOARD =====")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break