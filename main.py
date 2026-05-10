import random

def main_game():
    name = input("Enter Your Name: ").title()
    options_map = {'r': 'Rock 🪨', 'p': 'Paper 📃', 's': 'Scissors ✂️'}
    choices = list(options_map.keys())

    while True:
        user_choice = input(f"\n{name}, choose Rock, Paper, or Scissors (r/p/s): ").lower()
        
        if user_choice not in choices:
            print("Invalid Choice! Please try again.")
            continue

        bot_choice = random.choice(choices)
        
        print(f"{name} chose: {options_map[user_choice]}")
        print(f"Bot chose: {options_map[bot_choice]}")

        # Logic for results
        if user_choice == bot_choice:
            print("⁂ It's a Tie!")
        elif (user_choice == 'r' and bot_choice == 's') or \
             (user_choice == 'p' and bot_choice == 'r') or \
             (user_choice == 's' and bot_choice == 'p'):
            print(f"🏆 Congratulations {name}, You Won!")
        else:
            print(f"Don't worry {name}, Bot won this round! 😞")

        # Play again?
        repeat = input("\nDo you want to play again? (y/n): ").lower()
        if repeat != 'y':
            print("Thanks for playing! See you soon!")
            break

main_game()
