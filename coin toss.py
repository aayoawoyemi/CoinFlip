import random

starting_balance = 100
current_balance = starting_balance

while current_balance > 0:
    print(f"Current Balance: ${current_balance}")

    bet_amount = int(input("Enter your bet amount: $"))

    if bet_amount > current_balance:
        print("You cannot bet more than your current balance. Please enter a valid bet.")
        continue  # Skip the rest of the loop and start a new iteration

    coin = ["Heads", "Tails"]
    toss = random.choice(coin)
    selection = input("Heads or Tails: ")

    if selection == toss:
        current_balance += bet_amount
        print(f"Success! Coin landed on {toss}")
        print(f"You won ${bet_amount}. Current Balance: ${current_balance}")
    else:
        current_balance -= bet_amount
        print(f"Failed. Coin landed on {toss}")
        print(f"You lost ${bet_amount}. Current Balance: ${current_balance}")

    play_again = input("Don't quit now... Want to go for another round? (yes/no): ").lower()
    if play_again != "yes":
        print("That's a Shame, Thanks for playing!")
        break  # Exit the loop if the user doesn't want to play again

# This part will be reached only when the user decides not to play again
print("Game over. Thank you for playing!")
